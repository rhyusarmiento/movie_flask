from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), unique = False)
    year = db.Column(db.Integer, unique = False)
    rating = db.Column(db.Integer, unique = False)
    genre = db.Column(db.String(50), unique = False)
    starring = db.Column(db.String(50), unique = False)

    def __init__(self, title, year, rating, genre, starring):
        self.title = title
        self.year = year
        self.rating = rating
        self.genre = genre
        self.starring = starring


class MovieSchema(ma.Schema):
    class Meta:
        fields = ('title', 'content')

movie_schema = MovieSchema()
movie_schema = MovieSchema(many = True)

if __name__ == '__main__':
    app.run(debug = True)