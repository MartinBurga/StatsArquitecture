from flask import Blueprint, jsonify
from domain.services.playerStatsService import PlayerStatsService

api_player_bp = Blueprint("api_player", __name__, url_prefix="/api")

@api_player_bp.route("/leaderboard")
def leaderboard_api():
    leaderboard = PlayerStatsService.get_leaderboard()
    return jsonify(leaderboard)
