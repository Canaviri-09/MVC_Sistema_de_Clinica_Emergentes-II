from flask import request, redirect, url_for, Blueprint
from models.paciente_model import Paciente
import views.paciente_view as paciente_view

paciente_bp = Blueprint('paciente', __name__, url_prefix="/pacientes")

@paciente_bp.route("/")
def index():
    pacientes = Paciente.get_all()
    return paciente_view.list(pacientes)

@paciente_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        nuevo_paciente = Paciente(nombre, edad, direccion, telefono)
        nuevo_paciente.save()
        return redirect(url_for('paciente.index'))
    return paciente_view.create()

@paciente_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    paciente = Paciente.get_by_id(id)
    if request.method == 'POST':
        paciente.update(
            nombre=request.form['nombre'],
            edad=int(request.form['edad']),
            direccion=request.form['direccion'],
            telefono=request.form['telefono']
        )
        return redirect(url_for('paciente.index'))
    return paciente_view.edit(paciente)

@paciente_bp.route("/delete/<int:id>")
def delete(id):
    paciente = Paciente.get_by_id(id)
    paciente.delete()
    return redirect(url_for('paciente.index'))

@paciente_bp.route("/historial/<int:id>")
def historial(id):
    paciente = Paciente.get_by_id(id)
    from models.consulta_model import Consulta
    consultas = Consulta.get_by_paciente(id)
    return paciente_view.historial(paciente, consultas)
