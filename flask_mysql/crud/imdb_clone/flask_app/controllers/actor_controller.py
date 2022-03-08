import os
from flask_app import app
# from venv import create --- verify what this one does
from flask import render_template, request, redirect
from flask_app.models.actor import Actor
from flask_app.models.movie import Movie


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/actors')
def all_actors():
    actors = Actor.get_all()

    return render_template('all_actors.html', actors=actors)

@app.route('/actors/<int:actor_id>')
def one_actor(actor_id):
    data = {
        'id' : actor_id
    }

    actor = Actor.get_actor_with_roles(data)
    all_movies = Movie.get_all()

    return render_template('one_actor.html', actor=actor, all_movies=all_movies)

@app.route('/actors/create', methods=['POST'])
def create_actor():
    data = {
        'name' : request.form['name'],
        'age' : request.form['age']
    }

    new_actor_id = Actor.create(data)

    return redirect(f'/actors/{new_actor_id}')

@app.route('/actors/<int:actor_id>/edit')
def edit_actor(actor_id):
    data = {
        'id' : actor_id
    }

    actor = Actor.get_actor_with_roles(data)
    all_movies = Movie.get_all()

    return render_template('edit_actor.html', actor=actor, all_movies=all_movies)

@app.route('/actors/update', methods=['POST'])
def update_actor():
    data = {
        'actor_id' : request.form['actor_id'],
        'name' : request.form['name'],
        'age' : request.form['age']
    }

    Actor.update(data)
    actor_id = data['actor_id']

    return redirect(f'/actors/{actor_id}')

@app.route('/actors/<int:id>/delete')
def delete_actor(id):
    data = {
        'id' : id
    }

    Actor.delete(data)

    return redirect('/actors')