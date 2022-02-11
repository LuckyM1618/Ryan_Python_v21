from flask_app.config.mysqlconnection import connectToMySQL

class Actor:
    db = "actors_and_movies_schema"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.age = data=['age']
        # will need profile_img attribute later

        self.filmography = []

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # test_method to verify functionality, will change later
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM actors"

        results = connectToMySQL(cls.db).query_db(query)

        return results