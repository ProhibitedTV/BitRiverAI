from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login.

    GET: Render the login page.
    POST: Authenticate the user and log them in if credentials are valid.

    Returns:
        Response: Redirects to the main index page on successful login, otherwise reloads the login page.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):  # Use hashed password check
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.index'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """
    Handle user logout.

    Logs out the current user and redirects to the login page.

    Returns:
        Response: Redirects to the login page.
    """
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration.

    GET: Render the registration page.
    POST: Create a new user account if the provided username and email are unique.

    Returns:
        Response: Redirects to the login page on successful registration, otherwise reloads the registration page.
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']  # Ensure email is captured
        password = request.form['password']

        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
        else:
            new_user = User(username=username, email=email)
            new_user.set_password(password)  # Hash password before saving
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('auth.login'))
    return render_template('register.html')
