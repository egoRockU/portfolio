import os
from flask import Flask
from .routes import main
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['GITHUB_TOKEN'] = os.getenv('GITHUB_TOKEN')
    app.secret_key = 'THEME_SECRET_KEY'

    app.register_blueprint(main)

    return app