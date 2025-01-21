from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required
import requests
import logging

poetrygen_bp = Blueprint('poetrygen', __name__)

@poetrygen_bp.route('/poetrygen', methods=['GET'])
@login_required
def poetrygen_page():
    """
    Render the poetry generator page with available models.

    Returns:
        Response: Renders the poetrygen.html template with the list of models.
    """
    models = get_models()
    return render_template('poetrygen.html', models=models)

@poetrygen_bp.route('/generate-poetry', methods=['POST'])
@login_required
def generate_poetry():
    """
    Handle poetry generation requests.

    Receives a model and prompt from the client, queries the model for a response,
    and returns the generated poetry.

    Returns:
        Response: JSON response containing the generated poetry.
    """
    model = request.json.get('model')
    prompt = request.json.get('prompt')
    logging.info(f"Generating poetry with model: {model}, prompt: {prompt}")
    response = query_ollama(model, prompt)
    logging.info(f"Received response: {response}")
    return jsonify({'poetry': response})

def get_models():
    """
    Fetch available models from Ollama.

    Returns:
        list: A list of model names.
    """
    response = requests.get('http://localhost:11434/api/tags')
    if response.status_code == 200:
        models = [model['name'] for model in response.json().get('models', [])]
        logging.info(f"Fetched models: {models}")
        return models
    logging.error(f"Error fetching models: {response.status_code} - {response.text}")
    return []

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
    logging.info(f"Sending payload to Ollama: {payload}")
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get('response', 'Error: No response from model.')
    logging.error(f"Error querying model: {response.status_code} - {response.text}")
    return 'Error querying model.'
