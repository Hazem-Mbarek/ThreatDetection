from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config')
    
    # Register blueprints
    from .routes import main
    app.register_blueprint(main)
    
    return app
