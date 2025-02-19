from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuration settings can be added here
    app.config['SECRET_KEY'] = 'your_secret_key'

    with app.app_context():
        from .main import home
        app.add_url_rule('/', view_func=home)

    return app