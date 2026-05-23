from flask import render_template

def list(medicos):
    return render_template('medico/index.html', medicos=medicos)

def create():
    return render_template('medico/create.html')

def edit(medico):
    return render_template('medico/edit.html', medico=medico)
