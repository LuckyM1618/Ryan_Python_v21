from flask_app import app
# from venv import create --- verify what this one does
from flask import render_template
from flask_app.models.movie import Movie

@app.route('/movies')
def all_movies():
    movies = Movie.get_all()
    
    return render_template('all_movies.html', movies=movies)