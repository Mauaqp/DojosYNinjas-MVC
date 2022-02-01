from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models.m_ninjas import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.create_time = data["create_time"]
        self.update_time = data["update_time"]
        #lista para consulta y agregar ninjas
        self.dojos = []

    @classmethod
    def agregaDojo (cls, data):
        query = "INSERT INTO dojos ( nombre , create_time , update_time ) VALUES (%(dojo_name)s,NOW(),NOW());"
        return connectToMySQL("esquema_dojos_y_ninjas").query_db(query, data)

    @classmethod
    def get_all (cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("esquema_dojos_y_ninjas").query_db(query)
        listaDojos = []
        for d in results:
            listaDojos.append(cls(d))
        return listaDojos