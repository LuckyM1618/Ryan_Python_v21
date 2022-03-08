from flask_app import app
# from venv import create --- verify what this one does
from flask import render_template, request, redirect
from flask_app.models.movie import Movie
from flask_app.models.actor import Actor

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
    all_actors = Actor.get_all()

    return render_template('one_movie.html', movie=movie, all_actors=all_actors)

@app.route('/movies/create', methods=['POST'])
def create_movie():
    data = {
        'title' : request.form['title'],
        'release_date' : request.form['release_date'],
        'description' : request.form['description'],
    }

    new_movie_id = Movie.create(data)

    return redirect(f'/movies/{new_movie_id}')

@app.route('/movies/<int:movie_id>/edit')
def edit_movie(movie_id):
    data = {
        'id' : movie_id
    }

    movie = Movie.get_movie_with_cast(data)
    all_actors = Actor.get_all()

    return render_template('edit_movie.html', movie = movie, all_actors = all_actors)

@app.route('/movies/update', methods=['POST'])
def update_movie():
    data = {
        'movie_id' : request.form['movie_id'],
        'title' : request.form['title'],
        'release_date' : request.form['release_date'],
        'description' : request.form['description'],
    }

    Movie.update(data)
    movie_id = data['movie_id']

    return redirect(f'/movies/{movie_id}')

@app.route('/movies/<int:id>/delete')
def delete_movie(id):
    data = {
        'id' : id
    }

    Movie.delete(data)

    return redirect('/movies')