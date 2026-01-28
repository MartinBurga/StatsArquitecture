from infrastructure.repositories.playerRepository import PlayerRepository

class PlayerStatsService:

    @staticmethod
    def get_player_dashboard(username: str):
        user = PlayerRepository.find_by_username(username)
        if not user:
            return None

        return PlayerStatsService._build_player_stats(user)

    @staticmethod
    def get_leaderboard():
        raw_players = PlayerRepository.get_leaderboard_raw()
        leaderboard = []

        for p in raw_players:
            kills = p.get("estadisticas", {}).get("combate", {}).get("kills", 0)
            deaths = p.get("estadisticas", {}).get("combate", {}).get("deaths", 0)

            impactos = p.get("estadisticas", {}).get("precision", {}).get("impactos", 0)
            headshots = p.get("estadisticas", {}).get("precision", {}).get("headshots", 0)

            hs_percent = round((headshots / max(impactos, 1)) * 100, 2)

            leaderboard.append({
                "username": p["username"],
                "rango": p.get("perfil", {}).get("rango", "Sin rango"),
                "kills": kills,
                "kd": round(kills / max(deaths, 1), 2),
                "hs_percent": hs_percent
            })

        return leaderboard


    @staticmethod
    def _build_player_stats(user: dict):
        kills = user["estadisticas"]["combate"]["kills"]
        deaths = user["estadisticas"]["combate"]["deaths"]
        impactos = user["estadisticas"]["precision"]["impactos"]
        headshots = user["estadisticas"]["precision"]["headshots"]

        return {
            "user": user,
            "kd": round(kills / max(deaths, 1), 2),
            "headshot_pct": round((headshots / max(impactos, 1)) * 100, 2)
        }

    @staticmethod
    def _build_leaderboard_entry(player: dict):
        kills = player["estadisticas"]["combate"]["kills"]
        deaths = player["estadisticas"]["combate"]["deaths"]

        return {
            "username": player["username"],
            "rango": player["perfil"]["rango"],
            "kills": kills,
            "kd": round(kills / max(deaths, 1), 2)
        }
