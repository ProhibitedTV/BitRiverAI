# BitRiver AI

BitRiver AI is a futuristic, AI-driven application with a hacker-inspired design. It leverages Flask and a modern tech stack to provide a dynamic chat interface, authentication, and more. The project is inspired by matrix-style aesthetics and offers a visually engaging experience.

## Features

- **User Authentication**: Secure login and registration system using Flask-Login.
- **Chat Interface**: Dynamic chat system with AI model integration for interactive responses.
- **Responsive Design**: Matrix-style UI that works seamlessly on desktops and mobile devices.
- **Model Selection**: Choose from available AI models to tailor the chat experience.
- **Customizable Backend**: Easily expand functionality with Flask's modular architecture.
- **AI Image Generation**: Generate AI images using Stable Diffusion WebUI.

## Setup and Installation

Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ProhibitedTV/BitRiverAI.git
    cd BitRiverAI
    ```

2. **Install Dependencies**:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set Up the Database**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

4. **Run the Flask Application**:
    ```bash
    flask run
    ```

5. **Run the Gradio Application**:
    Navigate to the `gradio-app` directory and run the Gradio application:
    ```bash
    python app.py
    ```

## Integration with BitRiverAIServices

This project is meant to be used in conjunction with our other repository, [BitRiverAIServices](https://github.com/ProhibitedTV/BitRiverAIServices). The basic idea is that this Flask application runs, the services run separately, and the whole thing is served as a website. Ensure that both repositories are set up and running to get the full functionality.

## Project Structure
```
BitRiverAI/
├── flask-app/             # Flask application folder
│   ├── Dockerfile         # Dockerfile for Flask app
│   ├── app.py             # Main application file
│   ├── config.py          # Configuration settings
│   ├── migrations/        # Database migration files
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   ├── versions/
│   │   │   └── 8982d6bb2f01_initial_migration.py
│   │   └── README
│   ├── models.py          # Database models
│   ├── requirements.txt   # Project dependencies
│   ├── static/            # Static files (CSS, JS)
│   │   ├── css/
│   │   │   ├── styles.css
│   │   │   ├── login.css
│   │   │   └── index.css
│   │   └── js/
│   │       ├── chat.js
│   │       ├── index.js
│   │       └── matrix.js
│   ├── templates/         # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   └── register.html
│   ├── instance/          # Database instance
│   │   └── site.db
│   ├── .gitignore         # Git ignore file
│   └── README.md          # Project documentation
├── gradio-app/            # Gradio application folder
│   ├── app.py             # Main application file
│   ├── requirements.txt   # Project dependencies
│   └── ...                # Other Gradio app files
└── README.md              # Project documentation
```
## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Migrate
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite

## Contributing

We welcome contributions! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or feedback, feel free to reach out:
- **Email**: admin@bitriver.tv
- **GitHub**: [ProhibitedTV](https://github.com/ProhibitedTV)
