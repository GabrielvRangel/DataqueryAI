from flask import Flask
from .routes import main_bp
from .services.database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    
    init_db(app)  # Inicializa a conexão com o banco de dados
    
    app.register_blueprint(main_bp)
    
    return app
