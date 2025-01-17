# BitRiver AI

BitRiver AI is a futuristic, AI-driven application with a hacker-inspired design. It leverages Flask and a modern tech stack to provide a dynamic chat interface, authentication, and more. The project is inspired by matrix-style aesthetics and offers a visually engaging experience.

## Features

- **User Authentication**: Secure login and registration system using Flask-Login.
- **Chat Interface**: Dynamic chat system with AI model integration for interactive responses.
- **Responsive Design**: Matrix-style UI that works seamlessly on desktops and mobile devices.
- **Model Selection**: Choose from available AI models to tailor the chat experience.
- **Customizable Backend**: Easily expand functionality with Flask's modular architecture.

## Setup and Installation

Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ProhibitedTV/BitRiverAI.git
    cd BitRiverAI
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. **Run the Application**:
    ```bash
    flask run
    ```

6. **Access the Application**:
    Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure
```
BitRiverAI/
├── app.py                 # Main application file
├── config.py              # Configuration settings
├── migrations/            # Database migration files
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   ├── versions/
│   │   └── 8982d6bb2f01_initial_migration.py
│   └── README
├── models.py              # Database models
├── requirements.txt       # Project dependencies
├── static/                # Static files (CSS, JS)
│   ├── css/
│   │   ├── styles.css
│   │   ├── login.css
│   │   └── index.css
│   └── js/
│       ├── chat.js
│       ├── index.js
│       └── matrix.js
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   └── register.html
├── instance/              # Database instance
│   └── site.db
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
└── venv/                  # Virtual environment (excluded by .gitignore)
```
## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Migrate
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite

## Screenshots

_Add screenshots or gifs showcasing your app here._

## Contributing

We welcome contributions! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or feedback, feel free to reach out:
- **Email**: admin@bitriver.tv
- **GitHub**: [ProhibitedTV](https://github.com/ProhibitedTV)
