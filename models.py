from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """
    User model for storing user information.

    Attributes:
        id (int): The primary key for the user.
        username (str): The username of the user.
        email (str): The email of the user.
        password_hash (str): The hashed password of the user.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """
        Hashes the password and sets it.

        Args:
            password (str): The plain text password to hash.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks if the password matches the hashed password.

        Args:
            password (str): The plain text password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User id={self.id}, username={self.username}>'

class ChatHistory(db.Model):
    """
    ChatHistory model for storing chat interactions.

    Attributes:
        id (int): The primary key for the chat history entry.
        user_id (int): The ID of the user who initiated the chat.
        model (str): The name of the model used for the chat.
        prompt (str): The prompt sent to the model.
        response (str): The response received from the model.
        timestamp (datetime): The timestamp of the chat interaction.
    """
    __tablename__ = 'chat_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('chat_history', lazy=True))

    def __repr__(self):
        return f'<ChatHistory id={self.id}, user_id={self.user_id}, model={self.model}>'
