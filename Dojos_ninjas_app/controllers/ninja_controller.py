from flask import render_template, redirect, request
from Dojos_ninjas_app import app
from Dojos_ninjas_app.models import dojo_model,ninja_model

@app.route('/ninjas')
def ninjas():
    
    return render_template('ninja.html',dojos= dojo_model.Dojo.get_all())


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja_model.Ninja.save(request.form)
    return redirect('/')