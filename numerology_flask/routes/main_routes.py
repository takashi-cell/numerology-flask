from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)  # 🔹 ルートのBlueprintを作成

@main_bp.route("/")
def home():
    return render_template("main_index.html")  # 🔹 `templates/index.html` を表示
