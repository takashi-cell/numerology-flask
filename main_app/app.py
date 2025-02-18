from flask import Flask, render_template, redirect

app = Flask(__name__)

# フロントページ（診断選択ページ）
@app.route("/")
def home():
    return render_template("index.html")  # 診断選択ページを表示

# Numerology Flask へのリダイレクト
@app.route("/numerology")
def numerology():
    return redirect("http://127.0.0.1:5001/")  # 数秘術のトップページへリダイレクト

# Ton-Shin-Chi へのリダイレクト
@app.route("/ton-shin-chi")
def ton_shin_chi():
    return redirect("http://127.0.0.1:5002/")  # 貪・瞋・痴診断のトップページへリダイレクト

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # メインアプリはポート5000で起動

