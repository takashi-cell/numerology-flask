from flask import Blueprint, render_template, request
import json

# 🔹 Blueprint を作成
tonshinchi_bp = Blueprint("tonshinchi", __name__)

# 診断の質問リスト
questions = [
    {"id": "q1", "text": "欲しいものがあると、できるだけ早く手に入れたくなる", "category": "貪"},
    {"id": "q2", "text": "物事が計画通りに進まないと、強いストレスを感じる", "category": "瞋"},
    {"id": "q3", "text": "重要な選択でも「まあ何とかなる」と深く考えずに決める", "category": "痴"},
    {"id": "q4", "text": "お金やモノを持っていると安心するが、手放すのは苦手だ", "category": "貪"},
    {"id": "q5", "text": "他人のミスや失敗をなかなか許せないことが多い", "category": "瞋"},
    {"id": "q6", "text": "過去の失敗や後悔を気にしすぎて、なかなか行動に移せない", "category": "痴"},
    {"id": "q7", "text": "名誉や地位を得ることが、成功の証だと思う", "category": "貪"},
    {"id": "q8", "text": "怒りを感じると、なかなか冷静になれない", "category": "瞋"},
    {"id": "q9", "text": "迷ったときは、とりあえず周りの意見に従うことが多い", "category": "痴"},
    {"id": "q10", "text": "もし全てを捨てて新しい生活を始めるなら、不安で仕方ない", "category": "貪"},
]

# 🔹 `@tonshinchi_bp.route` に変更
@tonshinchi_bp.route("/", methods=["GET", "POST"])
def tonshinchi_index():
    if request.method == "POST":
        answers = request.form
        score = {"貪": 0, "瞋": 0, "痴": 0}

        for question in questions:
            question_id = question["id"]
            category = question["category"]
            if answers.get(question_id) == "はい":
                score[category] += 1

        dominant_trait = max(score, key=score.get)

        descriptions = {
            "貪": "物欲や執着心が強く、何かを求め続ける傾向があります。",
            "瞋": "怒りっぽく感情の起伏が激しくなることがあります。",
            "痴": "判断に迷いやすく、なかなか決断ができないことが多いです。",
        }

        result = {
            "dominant_trait": dominant_trait,
            "description": descriptions[dominant_trait],
            "貪": score["貪"],
            "瞋": score["瞋"],
            "痴": score["痴"]
        }

        # **JSON を適切に変換**
        scores_json = json.dumps({"貪": score["貪"], "瞋": score["瞋"], "痴": score["痴"]})

        # **デバッグ用のログをターミナルに出力**
        print("DEBUG: scores_json =", scores_json)

        return render_template("result.html", result=result, scores_json=scores_json)

    return render_template("tonshinchi_index.html", questions=questions)
