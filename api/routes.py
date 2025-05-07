from flask import render_template, request, jsonify
from models import Movie

def connect_routes(app, db):
    
    @app.route('/add_movie', methods=['POST'])
    def add_movie():
        movie_data = request.get_json()
    
        new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])
    
        db.session.add(new_movie)
        db.session.commit()
    
        return 'Done', 201
    
    @app.route('/movies')
    def movies():
        movie_list = Movie.query.all()
        movies = []
    
        for movie in movie_list:
            movies.append({'title' : movie.title, 'rating' : movie.rating})
    
        return jsonify({'movies' : movies})     

    @app.route('/')
    def home():
        return '<h2>Movie list</h2>'

