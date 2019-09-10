from flask import Flask
  
from ._const import KEY

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__,static_url_path='/static')
    app.debug = debug
    app.config['SECRET_KEY'] = KEY
    app.config["CACHE_TYPE"] = "null"

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
