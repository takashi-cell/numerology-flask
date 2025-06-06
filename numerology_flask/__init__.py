from flask import Flask

from numerology_flask.routes.main_routes import main_bp
from numerology_flask.routes.numerology_routes import numerology_bp
from numerology_flask.routes.tonshinchi_routes import tonshinchi_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(numerology_bp, url_prefix="/numerology")
    app.register_blueprint(tonshinchi_bp, url_prefix="/ton-shin-chi")
    return app

