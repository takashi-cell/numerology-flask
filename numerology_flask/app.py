import os
from flask import Flask, render_template, request
import json
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from numerology_logic import calculate_numerology

app = Flask(__name__)

# Render の環境変数 PORT からポートを取得（デフォルト 10000）
PORT = int(os.getenv("PORT", 10000))

# 数秘術の意味を格納する辞書
num_meanings = {
    1: "男性数。独立。\n強い意志と行動力を持ち、目標に向かって進む能力がある。",
    2: "女性数。サポート・バックアップ。\n協調性があり、人と調和を築くことが得意。",
    3: "子供数。わくわく楽しく。\n創造的で表現力があり、芸術やコミュニケーションが得意。",
    4: "固定数。コツコツ堅実に裏どりして動く。貯金好き。",
    5: "移動数。いろんな所に行きたい。派手好き。",
    6: "家族数。家族仲良く。パートナーシップ、仲間と一緒。",
    7: "職人数。一点突破。一つの事を探求する。",
    8: "八方広がり数。営業職、成功数。",
    9: "ギフト数。完成したものを伝える。教える。",
    11: "直感力が鋭く、精神的なリーダー。",
    22: "強い現実化能力を持ち、大きな目標を実現する。",
    33: "無条件の愛を持ち、他者の幸福を第一に考える。"
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None  # 🔥 事前に None で初期化
    if request.method == "POST":
        birthdate = request.form.get("birthdate")
        if not birthdate:
            return "エラー: 生年月日を入力してください！", 400
        
        result = calculate_numerology(birthdate)

        # 🔍 過去数の特別処理（11 → 11のみ、22 → 22のみ）
        if result["past_number"]["number"] == 11:
            result["past_number"]["number"] = "11"
            result["past_number"]["meaning"] = num_meanings[11]
            print("DEBUG: 過去数が11なので、11の説明のみセット")

        elif result["past_number"]["number"] == 22:
            result["past_number"]["number"] = "22"
            result["past_number"]["meaning"] = num_meanings[22]
            print("DEBUG: 過去数が22なので、22の説明のみセット")

        # 🔍 デバッグ出力（最終確認）
        print("DEBUG: 修正後の過去数 =", result["past_number"]["number"])
        print("DEBUG: 修正後の過去数の意味 =", result["past_number"]["meaning"])

        return render_template("result.html", result=result, num_meanings=num_meanings)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)  # Render 環境変数 PORT を使用
