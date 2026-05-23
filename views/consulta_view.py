from flask import render_template

def list(consultas, fecha_inicio=None, fecha_fin=None):
    return render_template('consulta/index.html', consultas=consultas,
                           fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)

def create(medicos, pacientes):
    return render_template('consulta/create.html', medicos=medicos, pacientes=pacientes)

def edit(consulta, medicos, pacientes):
    return render_template('consulta/edit.html', consulta=consulta,
                           medicos=medicos, pacientes=pacientes)
