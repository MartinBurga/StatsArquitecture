from flask import Flask, render_template
from flask_pymongo import PyMongo
import config

app = Flask(__name__)
app.config["MONGO_URI"] = config.MONGO_URI
mongo = PyMongo(app)

@app.route("/")
def index():
    players_col = mongo.db.Player

    user = players_col.find_one(
        {"username": "Niyumme"},
        {"_id": 0}
    )

    if not user:
        return "Usuario no encontrado", 404

    leaderboard_data = list(
        players_col.find(
            {},
            {
                "_id": 0,
                "username": 1,
                "perfil.rango": 1,
                "estadisticas.combate.kills": 1,
                "estadisticas.combate.deaths": 1
            }
        ).sort("estadisticas.combate.kills", -1)
    )

    kills = user["estadisticas"]["combate"]["kills"]
    deaths = user["estadisticas"]["combate"]["deaths"]
    impactos = user["estadisticas"]["precision"]["impactos"]
    headshots = user["estadisticas"]["precision"]["headshots"]

    kd = round(kills / max(deaths, 1), 2)
    headshot_pct = round((headshots / max(impactos, 1)) * 100, 2)

    return render_template(
        "index.html",
        user=user,
        leaderboard=leaderboard_data,
        kd=kd,
        headshot_pct=headshot_pct,
        current_user=user["username"],
        active_tab="home"
    )

@app.route("/leaderboard")
def leaderboard():
    players_col = mongo.db.Player

    players = list(
        players_col.find(
            {},
            {"_id": 0}
        ).sort("estadisticas.combate.kills", -1)
    )

    return render_template(
        "leaderboard.html",
        players=players,
        current_user="Niyumme",
        active_tab="leaderboard"
    )

@app.route("/perfil")
def perfil():
    players_col = mongo.db.Player

    user = players_col.find_one(
        {"username": "Niyumme"},
        {"_id": 0}
    )

    if not user:
        return "Usuario no encontrado", 404

    return render_template(
        "profile.html",
        user=user,
        active_tab="profile"
    )

if __name__ == "__main__":
    app.run(debug=True)
