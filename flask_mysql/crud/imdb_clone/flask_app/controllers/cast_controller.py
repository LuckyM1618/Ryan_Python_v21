from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.cast import Cast

@app.route('/cast/create', methods=['POST'])
def create():
    data = {
        'actor_id' : request.form['actor_id'],
        'movie_id' : request.form['movie_id'],
        'role' : request.form['role']
    }

    actor = request.form['actor_id']
    movie = request.form['movie_id']

    new_cast_id = Cast.create(data)

    # since there is no view one cast page, redirect back to the page that created it
    if request.form['return_to'] == 'actor':
        return_url = f'/actors/{actor}'
    elif request.form['return_to'] == 'movie':
        return_url = f'/movies/{movie}'

    return redirect(return_url)

@app.route('/cast/<int:id>/delete/<return_to>/<int:return_id>')
def delete(id, return_to, return_id):
    data = {
        'id' : id
    }

    Cast.delete(data)

    if return_to == 'actor':
        return_url = f'/actors/{return_id}'
    elif return_to == 'movie':
        return_url = f'/movies/{return_id}'

    return redirect(return_url)
