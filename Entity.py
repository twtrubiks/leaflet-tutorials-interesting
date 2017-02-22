from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class MapPets(db.Model):
    __tablename__ = 'MapPets'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Picture = db.Column(db.String(128))
    Color= db.Column(db.String(32))
    Longitude = db.Column(db.Integer)
    Latitude = db.Column(db.Integer)



if __name__ == '__main__':
    manager.run()
