from flask import render_template, request, redirect, session, flash
from dojos_app import app
from dojos_app.models.m_dojos import Dojo

@app.route( '/', methods=['GET'] )
def inicio():
    return render_template( "dojo.html" )