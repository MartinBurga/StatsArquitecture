from flask import Blueprint, render_template
from domain.services.playerStatsService import PlayerStatsService

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/perfil")
def perfil():
    data = PlayerStatsService.get_player_dashboard("Niyumme")

    if not data:
        return "Usuario no encontrado", 404

    return render_template(
        "profile.html",
        user=data["user"],
        kd=data["kd"],
        headshot_pct=data["headshot_pct"],
        active_tab="profile"
    )
