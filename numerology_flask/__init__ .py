from flask import Flask
from numerology_flask.routes.main_routes import main_bp
from numerology_flask.routes.numerology_routes import numerology_bp
from numerology_flask.routes.tonshinchi_routes import tonshinchi_bp

app = Flask(__name__)

# Blueprint を登録
app.register_blueprint(main_bp)
app.register_blueprint(numerology_bp, url_prefix="/numerology")
app.register_blueprint(tonshinchi_bp, url_prefix="/ton-shin-chi")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
