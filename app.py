from flask import Flask
from routes.main_routes import main_bp
from routes.numerology_routes import numerology_bp
from routes.tonshinchi_routes import tonshinchi_bp  # 🔹 追加

app = Flask(__name__)

# 🔹 各ルートを登録
app.register_blueprint(main_bp, url_prefix="/")
app.register_blueprint(numerology_bp, url_prefix="/numerology")
app.register_blueprint(tonshinchi_bp, url_prefix="/ton-shin-chi")  # 🔹 貪・瞋・痴 診断ルートを登録

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)  # Render 環境向けにPORT設定
