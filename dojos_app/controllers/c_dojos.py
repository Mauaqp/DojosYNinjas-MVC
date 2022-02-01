from flask import render_template, request, redirect, session, flash
from dojos_app import app
from dojos_app.models.m_dojos import Dojo

#ruta principal y método que muestra dojos
@app.route( '/', methods=['GET'] )
def inicio():
    listaDojos = Dojo.get_all()
    return render_template( "dojo.html", listaDojos = listaDojos)

#Registrar dojos
@app.route('/', methods=['POST'])
def registro ():
    Dojo.agregaDojo(request.form)
    return redirect( '/' )

#mostrar ninjas en el DOjo
@app.route('/dojos/<int:id>', methods=['GET'])
def mostrarDojo(id):
    data = {
        "id" : id
    }
    return render_template("show.html", dojo = Dojo.get_one_dojo_ninja(data))