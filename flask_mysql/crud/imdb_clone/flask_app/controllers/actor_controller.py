from flask_app import app
# from venv import create --- verify what this one does
from flask import render_template
from flask_app.models.actor import Actor

@app.route('/actors')
def all_actors():
    actors = Actor.get_all()

    return render_template('all_actors.html', actors=actors)