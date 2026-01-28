from flask import Blueprint, render_template
from domain.services.playerStatsService import PlayerStatsService

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def index():
    username = "Niyumme"  # luego esto será dinámico (login)

    dashboard = PlayerStatsService.get_player_dashboard(username)

    if not dashboard:
        return "Usuario no encontrado", 404

    leaderboard = PlayerStatsService.get_leaderboard()

    return render_template(
        "index.html",
        user=dashboard["user"],
        kd=dashboard["kd"],
        headshot_pct=dashboard["headshot_pct"],
        leaderboard=leaderboard,
        current_user=username,
        active_tab="home"
    )
