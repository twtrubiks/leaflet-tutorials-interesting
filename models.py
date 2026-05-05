from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MapPets(db.Model):
    __tablename__ = "MapPets"

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Picture = db.Column(db.String(128))
    Color = db.Column(db.String(32))
    Longitude = db.Column(db.Float)
    Latitude = db.Column(db.Float)
