from flask import Flask, render_template, request
from .numerology_logic import *  # または必要な関数・クラスを明記

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        birthdate = request.form.get("birthdate")  # 数字のみのフォーム
        if not birthdate:
            return "エラー: 生年月日を入力してください！", 400  # ✅ 名前のチェックを削除

        # 数秘術の計算
        result = numerology_logic.calculate_numerology(birthdate)

        return render_template("result.html", result=result, birthdate=birthdate)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



