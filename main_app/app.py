import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

# Render のポート番号を取得（デフォルト5000）
PORT = os.environ.get("PORT", 5000)
RENDER_URL = "https://numerology-flask.onrender.com"  # 🚀 Render のURLを設定

# フロントページ（診断選択ページ）
@app.route("/")
def home():
    return render_template("index.html")  # 診断選択ページを表示

# Numerology Flask へのリダイレクト
@app.route("/numerology")
def numerology():
    return redirect(f"{RENDER_URL}/numerology")  # Render のURLへリダイレクト

# Ton-Shin-Chi へのリダイレクト
@app.route("/ton-shin-chi")
def ton_shin_chi():
    return redirect(f"{RENDER_URL}/ton-shin-chi")  # Render のURLへリダイレクト

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT), debug=True)  # Render で動作するよう修正
