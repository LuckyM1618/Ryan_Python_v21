from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL

class Cast:
    db = "actors_and_movies_schema"

    def __init__(self, data):
        self.id = data['id']

        self.movie_id = data['movie_id']
        self.title = data['title']
        self.release_date = data['release_date']

        self.actor_id = data['actor_id']
        self.name = data['name']
        self.role = data['role']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO cast (movie_id, actor_id, role, created_at, updated_at) VALUES (%(movie_id)s, %(actor_id)s, %(role)s, NOW(), NOW());
        """

        return connectToMySQL(cls.db).query_db(query,data)