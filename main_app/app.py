import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

# Render の環境変数 PORT からポートを取得（デフォルト 10000）
PORT = int(os.getenv("PORT", 10000))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/numerology")
def numerology():
    return redirect("https://numerology-flask.onrender.com/")

@app.route("/ton-shin-chi")
def ton_shin_chi():
    return redirect("https://ton-shin-chi.onrender.com/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
