from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
import requests
from models import db, ChatHistory
from .main import get_models

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['GET'])
@login_required
def chat_page():
    """
    Render the chat page with available models.

    Returns:
        Response: Renders the chat.html template with the list of models.
    """
    return render_template('chat.html', models=get_models())

@chat_bp.route('/chat', methods=['POST'])
@login_required
def chat():
    """
    Handle chat requests and save chat history.

    Receives a model and prompt from the client, queries the model for a response,
    saves the chat history, and returns the response.

    Returns:
        Response: JSON response containing the model's reply.
    """
    model = request.json.get('model')
    prompt = request.json.get('prompt')
    response = query_ollama(model, prompt)

    # Save chat history
    chat_history = ChatHistory(user_id=current_user.id, model=model, prompt=prompt, response=response)
    db.session.add(chat_history)
    db.session.commit()

    return jsonify({'response': response})

@chat_bp.route('/chat/history', methods=['GET'])
@login_required
def chat_history():
    """
    Render the chat history page for the current user.

    Returns:
        Response: Renders the chat_history.html template with the user's chat history.
    """
    history = ChatHistory.query.filter_by(user_id=current_user.id).order_by(ChatHistory.timestamp.desc()).all()
    return render_template('chat_history.html', history=history)

@chat_bp.route('/chat/history/<int:chat_id>', methods=['DELETE'])
@login_required
def delete_chat(chat_id):
    """
    Handle chat deletion requests.

    Deletes a chat entry from the user's chat history.

    Args:
        chat_id (int): The ID of the chat entry to delete.

    Returns:
        Response: JSON response indicating success or failure.
    """
    chat = ChatHistory.query.get_or_404(chat_id)
    if chat.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    db.session.delete(chat)
    db.session.commit()
    return jsonify({'success': 'Chat deleted'})

def query_ollama(model, prompt):
    """
    Send a prompt to the selected model and get a response.

    Args:
        model (str): The name of the model to query.
        prompt (str): The prompt to send to the model.

    Returns:
        str: The response from the model or an error message.
    """
    url = 'http://localhost:11434/api/generate'
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get('response', 'Error: No response from model.')
    return 'Error querying model.'
