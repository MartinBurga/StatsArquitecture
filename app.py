from flask import Flask
import config
from extensions import mongo

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = config.MONGO_URI

    mongo.init_app(app)

    # HTML routes
    from api.controllers.homeRoutes import home_bp
    from api.controllers.leaderboardRoutes import leaderboard_bp
    from api.controllers.profileRoutes import profile_bp

    # API routes
    from api.controllers.apiPlayerRoutes import api_player_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(leaderboard_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(api_player_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
