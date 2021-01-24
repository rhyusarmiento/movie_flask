from flask import Flask, request, jsonify
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
        fields = ('title', 'year', 'rating', 'genre', 'starring')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many = True)

# Endpoint to create a new movie
@app.route('/movie', methods = ["POST"])
def add_movie():
    title = request.json['title']
    year = request.json['year']
    rating = request.json['rating']
    genre = request.json['genre']
    starring = request.json['starring']

    new_movie = Movie(title, year, rating, genre, starring)

    db.session.add(new_movie)
    db.session.commit()

    movie = Movie.query.get(new_movie.id)

    return movie_schema.jsonify(movie)

# Endpoint to query all movies
@app.route('/movies', methods = ["GET"])
def get_movies():
    all_movies = Movie.query.all()
    result = movies_schema.dump(all_movies)
    return jsonify(result)

# Endpoint to query a movie
@app.route('/movie/<id>', methods = ["GET"])
def get_movie(id):
    movie = Movie.query.get(id)
    return movie_schema.jsonify(movie)


if __name__ == '__main__':
    app.run(debug = True)