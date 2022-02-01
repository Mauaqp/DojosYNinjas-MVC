from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models.m_ninjas import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.create_time = data["create_time"]
        self.update_time = data["update_time"]

