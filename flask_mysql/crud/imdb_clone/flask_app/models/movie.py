from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.cast import Cast

class Movie:
    db = "actors_and_movies_schema"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.release_date = data['release_date']
        # will need cover_art_img attribute later
        self.description = data['description']

        self.cast = []

        self.created_at = data['created_at']
        self.updated_at = data['id']

    # test_method to verify functionality, will change later
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM movies"

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod
    def get_movie_with_cast(cls, data):
        # query = "SELECT * FROM movies WHERE id = %(id)s;"
        query = """
        SELECT * FROM movies
        LEFT JOIN cast
        ON cast.movie_id = movies.id
        LEFT JOIN actors
        ON actors.id = cast.actor_id
        WHERE movies.id = %(id)s
        """

        results = connectToMySQL(cls.db).query_db(query, data)

        movie = cls(results[0])
        for row in results:
            role_data = {
                "id" : row['cast.id'],

                "movie_id" : row['movie_id'],
                "title" : row['title'],
                "release_date" : row['release_date'],

                "actor_id" : row['actor_id'],
                "name" : row['name'],
                "role" : row['role'],

                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            movie.cast.append(Cast(role_data))

        return movie

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO movies (title, release_date, description, created_at, updated_at)
        VALUES (%(title)s, %(release_date)s, %(description)s, NOW(), NOW());
        """

        return connectToMySQL(cls.db).query_db(query,data)