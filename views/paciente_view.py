from flask import render_template

def list(pacientes):
    return render_template('paciente/index.html', pacientes=pacientes)

def create():
    return render_template('paciente/create.html')

def edit(paciente):
    return render_template('paciente/edit.html', paciente=paciente)

def historial(paciente, consultas):
    return render_template('paciente/historial.html', paciente=paciente, consultas=consultas)
