import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
import requests
from config import config

app = Flask(__name__)

# Load the configuration based on the environment
env = os.getenv('FLASK_ENV', 'development')
app.config.from_object(config[env])

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@login_required
def index():
    # Render the chat interface
    return render_template('index.html', models=get_models())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/chat', methods=['POST'])
@login_required
def chat():
    model = request.json.get('model')
    prompt = request.json.get('prompt')
    response = query_ollama(model, prompt)
    return jsonify({'response': response})


def get_models():
    """Fetch available models from Ollama."""
    response = requests.get('http://localhost:11434/api/tags')
    if response.status_code == 200:
        return [model['name'] for model in response.json().get('models', [])]
    return []


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


if __name__ == '__main__':
    app.run()
