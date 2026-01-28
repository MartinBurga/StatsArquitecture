from pymongo import MongoClient
import json
import os

MONGO_URI = "mongodb+srv://ADMIN:UDLA@cluster0.0s8cq40.mongodb.net/ArquitecturaDB"

client = MongoClient(MONGO_URI)
db = client.get_database("ArquitecturaDB")
collection = db.Player 

def leaderboard_handler(event, context):
    players = list(db.Player.find({}, {"_id": 0}))
    leaderboard = []

    for p in players:
        kills = p["estadisticas"]["combate"]["kills"]
        deaths = p["estadisticas"]["combate"]["deaths"]
        hs = p["estadisticas"]["precision"]["headshots"]
        shots = p["estadisticas"]["precision"]["impactos"]

        leaderboard.append({
            "username": p["username"],
            "kills": kills,
            "deaths": deaths,
            "kd": round(kills / max(deaths, 1), 2),
            "hs_percent": round((hs / max(shots, 1)) * 100, 2)
        })

    return {
        "statusCode": 200,
        "body": json.dumps(leaderboard),
        "headers": {"Content-Type": "application/json"}
    }


## Para visualizar en localhost usar localhost:3000/dev/leaderboard