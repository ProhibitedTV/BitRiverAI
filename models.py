from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hashes the password and sets it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the password matches the hashed password."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User id={self.id}, username={self.username}>'

class ChatHistory(db.Model):
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
