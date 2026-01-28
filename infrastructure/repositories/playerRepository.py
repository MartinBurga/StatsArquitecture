from extensions import mongo

class PlayerRepository:

    @staticmethod
    def find_by_username(username: str):
        return mongo.db.Player.find_one(
            {"username": username},
            {"_id": 0}
        )

    @staticmethod
    def get_leaderboard_raw():
        return list(
        mongo.db.Player.find(
            {},
            {
                "_id": 0,
                "username": 1,
                "perfil.rango": 1,
                "estadisticas.combate.kills": 1,
                "estadisticas.combate.deaths": 1,
                "estadisticas.precision.impactos": 1,
                "estadisticas.precision.headshots": 1
            }
        ).sort("estadisticas.combate.kills", -1)
    )
    
