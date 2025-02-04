from flask import Blueprint, render_template
from flask_login import login_required

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['GET'])
@login_required
def chat_page():
    """
    Render the chat page.

    Returns:
        Response: Renders the chat.html template.
    """
    return render_template('chat.html')
