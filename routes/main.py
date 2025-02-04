from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
import requests

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    """
    Redirect to the dashboard page.

    Returns:
        Response: Redirects to the dashboard page.
    """
    return redirect(url_for('main.dashboard'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard page with available models.

    Returns:
        Response: Renders the dashboard.html template with the list of models.
    """
    return render_template('dashboard.html', models=get_models())

@main_bp.route('/settings')
@login_required
def settings():
    """
    Render the settings page.

    Returns:
        Response: Renders the settings.html template.
    """
    return render_template('settings.html')

@main_bp.route('/update_password', methods=['POST'])
@login_required
def update_password():
    """
    Handle password update requests.

    Receives the current password, new password, and confirmation password from the client,
    validates them, and updates the user's password if valid.

    Returns:
        Response: Redirects to the settings page with a success or error message.
    """
    current_password = request.form.get('current-password')
    new_password = request.form.get('new-password')
    confirm_password = request.form.get('confirm-password')

    if not current_user.check_password(current_password):
        flash('Current password is incorrect.', 'error')
        return redirect(url_for('main.settings'))

    if new_password != confirm_password:
        flash('New passwords do not match.', 'error')
        return redirect(url_for('main.settings'))

    current_user.set_password(new_password)
    db.session.commit()
    flash('Password updated successfully.', 'success')
    return redirect(url_for('main.settings'))

def get_models():
    """
    Fetch available models from Ollama.

    Returns:
        list: A list of model names.
    """
    response = requests.get('http://localhost:11434/api/tags')
    if response.status_code == 200:
        return [model['name'] for model in response.json().get('models', [])]
    return []
