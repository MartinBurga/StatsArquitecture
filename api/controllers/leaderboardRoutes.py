from flask import Blueprint, render_template

leaderboard_bp = Blueprint("leaderboard", __name__)

@leaderboard_bp.route("/leaderboard")
def leaderboard():
    return render_template(
        "leaderboard.html",
        current_user="Niyumme",
        active_tab="leaderboard"
    )
