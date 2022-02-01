from dojos_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.create_time = data["create_time"]
        self.update_time = data["update_time"]
    
    @classmethod
    def agregaNinja( cls, data ):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojos_id, create_time , update_time) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(),NOW());"
        return connectToMySQL("esquema_dojos_y_ninjas").query_db( query, data )