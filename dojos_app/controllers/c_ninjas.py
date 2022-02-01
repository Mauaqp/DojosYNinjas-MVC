from flask import render_template, request, redirect, session, flash
from dojos_app import app
from dojos_app.models.m_ninjas import Ninja
from dojos_app.models.m_dojos import Dojo

@app.route( '/ninjas', methods=['GET'] )
def ninjas():
    listaDojos = Dojo.get_all()
    return render_template( "ninja.html", listaDojos = listaDojos)

#agregar ninjas
@app.route('/ninjas', methods=['POST'])
def registroNinja():
    Ninja.agregaNinja(request.form)
    return redirect('/')