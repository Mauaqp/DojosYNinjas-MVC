from flask import render_template, request, redirect, session, flash
from dojos_app import app
from dojos_app.models.m_dojos import Dojo

@app.route( '/', methods=['GET'] )
def inicio():
    listaDojos = Dojo.get_all()
    return render_template( "dojo.html", listaDojos = listaDojos)

#Registrar dojos
@app.route('/', methods=['POST'])
def registro ():
    Dojo.agregaDojo(request.form)
    return redirect( '/' )

#Mostrar lista de dojos
# @app.route('/', methods=['GET'])
# def mostrarListaDojos():
#     listaDojos = Dojo.get_all()
#     return render_template('dojo.html', listaDojos = listaDojos)