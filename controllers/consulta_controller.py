from flask import request, redirect, url_for, Blueprint
from models.consulta_model import Consulta
from models.medico_model import Medico
from models.paciente_model import Paciente
import views.consulta_view as consulta_view
from datetime import datetime

consulta_bp = Blueprint('consulta', __name__, url_prefix="/consultas")

@consulta_bp.route("/")
def index():
    # Filtro por fecha opcional
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')
    if fecha_inicio and fecha_fin:
        try:
            fi = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            ff = datetime.strptime(fecha_fin + ' 23:59:59', '%Y-%m-%d %H:%M:%S')
            consultas = Consulta.get_by_fecha(fi, ff)
        except ValueError:
            consultas = Consulta.get_all()
    else:
        consultas = Consulta.get_all()
    return consulta_view.list(consultas, fecha_inicio, fecha_fin)

@consulta_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        fecha_str = request.form.get('fecha')
        if fecha_str:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
        else:
            fecha = datetime.now()
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']
        nueva_consulta = Consulta(fecha, diagnostico, tratamiento, id_medico, id_paciente)
        nueva_consulta.save()
        return redirect(url_for('consulta.index'))
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    return consulta_view.create(medicos, pacientes)

@consulta_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    consulta = Consulta.get_by_id(id)
    if request.method == 'POST':
        fecha_str = request.form.get('fecha')
        if fecha_str:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
        else:
            fecha = consulta.fecha
        consulta.update(
            fecha=fecha,
            diagnostico=request.form['diagnostico'],
            tratamiento=request.form['tratamiento'],
            id_medico=request.form['id_medico'],
            id_paciente=request.form['id_paciente']
        )
        return redirect(url_for('consulta.index'))
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    return consulta_view.edit(consulta, medicos, pacientes)

@consulta_bp.route("/delete/<int:id>")
def delete(id):
    consulta = Consulta.get_by_id(id)
    consulta.delete()
    return redirect(url_for('consulta.index'))
