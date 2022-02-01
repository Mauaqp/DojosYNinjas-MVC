from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models.m_ninjas import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.create_time = data["create_time"]
        self.update_time = data["update_time"]
        #lista para consulta y agregar ninjas
        self.ninjas = []

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
    
    #metodo para hacer join entre dojos y ninjas
    @classmethod
    def get_one_dojo_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query, data)
        dojo = cls(resultado[0])
        for row in resultado:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age' : row['age'],
                # Siempre poner atención en la correspondencia con las base de datos
                'create_time': row['ninjas.create_time'],
                'update_time': row['ninjas.update_time']
            }
            print(dojo)
            dojo.ninjas.append(Ninja(n))
        return dojo