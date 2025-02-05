from flask import Flask, render_template, request
from numerology_flask.numerology_logic import calculate_numerology  # 必要な関数をインポート

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        birthdate = request.form.get("birthdate")
        if not birthdate:
            return "エラー: 生年月日を入力してください！", 400

        # 数秘術の計算
        result = calculate_numerology(birthdate)

        return render_template("result.html", result=result, birthdate=birthdate)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
