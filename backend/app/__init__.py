from flask import Flask
from flask_cors import CORS
from app.database import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow frontend to communicate with backend
    app.config["UPLOAD_FOLDER"] = "uploads/"

    init_db()

    from app.routes import main
    app.register_blueprint(main)

    return app
