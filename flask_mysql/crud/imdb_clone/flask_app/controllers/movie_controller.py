from flask_app import app
# from venv import create --- verify what this one does
from flask import render_template, request, redirect
from flask_app.models.movie import Movie

@app.route('/movies')
def all_movies():
    movies = Movie.get_all()
    
    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<int:movie_id>')
def one_movie(movie_id):
    data = {
        'id' : movie_id
    }

    movie = Movie.get_movie_with_cast(data)

    return render_template('one_movie.html', movie=movie)

@app.route('/movies/create', methods=['POST'])
def create_movie():
    data = {
        'title' : request.form['title'],
        'release_date' : request.form['release_date'],
        'description' : request.form['description'],
    }

    new_movie_id = Movie.create(data)

    return redirect(f'/movies/{new_movie_id}')