from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required, current_user
import requests
from models import db, ChatHistory
from .main import get_models

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['GET'])
@login_required
def chat_page():
    return render_template('chat.html', models=get_models())

@chat_bp.route('/chat', methods=['POST'])
@login_required
def chat():
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
    history = ChatHistory.query.filter_by(user_id=current_user.id).order_by(ChatHistory.timestamp.desc()).all()
    return render_template('chat_history.html', history=history)

def query_ollama(model, prompt):
    """Send a prompt to the selected model."""
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
