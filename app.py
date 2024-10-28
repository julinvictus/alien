from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    spaceship_name = db.Column(db.String(100), nullable=False)
    hero_name = db.Column(db.String(100), nullable=False)
    hero_actor_name = db.Column(db.String(100), nullable=False)
    synthetic_name = db.Column(db.String(100), nullable=False)
    planet_name = db.Column(db.String(100), nullable=False)
    xenomorph_name = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    director_name = db.Column(db.String(100), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'movie name': self.movie_name, 
            'year': self.year,
            'spaceship name': self.spaceship_name,
            'hero name': self.hero_name,
            'hero actor name': self.hero_actor_name,
            'synthetic name': self.synthetic_name,
            'planet name': self.planet_name,
            'xenomorph name': self.xenomorph_name,
            'release year': self.release_year,
            'director name': self.director_name,
        }

db.create_all()

# create a test route
@app.route('/test', methods=['GET'])
def test():
	return make_response(jsonify({'message': 'test route'}), 200)


# create a movie
@app.route('/movies', methods=['POST'])
def create_movie():
	try:
		data = request.get_json()
		new_movie = Movie(
			movie_name=data['movie_name'], 
			year=data['year'],
			spaceship_name=data['spaceship_name'],
			hero_name=data['hero_name'],
			hero_actor_name=data['hero_actor_name'],
			synthetic_name=data['synthetic_name'],
			planet_name=data['planet_name'],
			xenomorph_name=data['xenomorph_name'],
			release_year=data['release_year'],
			director_name=data['director_name'],
        )
		db.session.add(new_movie)
		db.session.commit()
		return make_response(jsonify({'message': 'movie created'}), 201)
	except:
		return make_response(jsonify({'message': 'error creating movie'}), 500)

# get all movies
@app.route('/movies', methods=['GET'])
def get_users():
	try:
		movies = Movie.query.all()
		return make_response(jsonify([movie.json() for movie in movies]), 200)
	except e:
		return make_response(jsonify({'message': 'error getting movies'}), 500)

# get a movie by id
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
	try:
		movie = Movie.query.filter_by(id=id).first()
		if movie:
			return make_response(jsonify({'movie': movie.json()}), 200)
		return make_response(jsonify({'message': 'movie not found'}), 404)
	except e:
		return make_response(jsonify({'message': 'error getting movie'}), 500)

# update a movie
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
	try:
		movie = Movie.query.filter_by(id=id).first()
		if movie:
			data = request.get_json()
			movie.movie_name=data['movie_name']      
			movie.year=data['year']
			movie.spaceship_name=data['spaceship_name']
			movie.hero_name=data['hero_name']
			movie.hero_actor_name=data['hero_actor_name']
			movie.synthetic_name=data['synthetic_name']
			movie.planet_name=data['planet_name']
			movie.xenomorph_name=data['xenomorph_name']
			movie.release_year=data['release_year']
			movie.director_name=data['director_name']
			db.session.commit()
			return make_response(jsonify({'message': 'movie updated'}), 200)
		return make_response(jsonify({'message': 'movie not found'}), 404)
	except e:
		return make_response(jsonify({'message': 'error updating movie'}), 500)

# delete a movie
@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
	try:
		movie = Movie.query.filter_by(id=id).first()
		if movie:
			db.session.delete(movie)
			db.session.commit()
			return make_response(jsonify({'message': 'movie deleted'}), 200)
		return make_response(jsonify({'message': 'movie not found'}), 404)
	except e:
		return make_response(jsonify({'message': 'error deleting movie'}), 500)