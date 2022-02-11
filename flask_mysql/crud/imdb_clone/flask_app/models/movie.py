from flask_app.config.mysqlconnection import connectToMySQL

class Movie:
    db = "actors_and_movies_schema"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.release_date = data['release_date']
        # will need cover_art_img attribute later
        self.description = data['description']

        self.created_at = data['created_at']
        self.updated_at = data['id']

    # test_method to verify functionality, will change later
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM movies"

        results = connectToMySQL(cls.db).query_db(query)

        return results