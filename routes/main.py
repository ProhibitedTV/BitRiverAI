from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
import requests

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    return redirect(url_for('main.dashboard'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', models=get_models())

@main_bp.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

def get_models():
    """Fetch available models from Ollama."""
    response = requests.get('http://localhost:11434/api/tags')
    if response.status_code == 200:
        return [model['name'] for model in response.json().get('models', [])]
    return []
