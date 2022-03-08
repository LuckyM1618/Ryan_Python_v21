from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.cast import Cast

class Actor:
    db = "actors_and_movies_schema"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.profile_img = data['profile_img']

        self.roles = []

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # test_method to verify functionality, will change later
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM actors;"

        results = connectToMySQL(cls.db).query_db(query)

        return results

    @classmethod
    def get_actor_with_roles(cls, data):
        query = """
        SELECT * FROM actors
        LEFT JOIN cast
        ON cast.actor_id = actors.id
        LEFT JOIN movies
        ON movies.id = cast.movie_id
        WHERE actors.id = %(id)s
        """

        results = connectToMySQL(cls.db).query_db(query, data)

        actor = cls(results[0])
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
            actor.roles.append(Cast(role_data))

        return actor

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO actors (name, age, created_at, updated_at)
        VALUES (%(name)s, %(age)s, NOW(), NOW());
        """

        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls, data):
        query = "UPDATE actors SET name = %(name)s, age = %(age)s, updated_at = NOW() WHERE id = %(actor_id)s;"

        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM actors WHERE (id = %(id)s);"

        return connectToMySQL(cls.db).query_db(query,data)
