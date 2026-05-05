from flask import Flask, jsonify, render_template
from flask_migrate import Migrate

from models import MapPets, db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("index.html")

    @app.route("/api", methods=["POST"])
    def api():
        pets = MapPets.query.all()
        return jsonify([
            {
                "Name": p.Name,
                "Picture": p.Picture,
                "Color": p.Color,
                "Longitude": p.Longitude,
                "Latitude": p.Latitude,
            }
            for p in pets
        ])

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
