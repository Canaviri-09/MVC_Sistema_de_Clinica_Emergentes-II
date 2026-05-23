from flask import Flask, request
from database import db

app = Flask(__name__)

# Configuración de la Base de Datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinica.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar la base de datos primero
db.init_app(app)

# Importamos los controladores AQUÍ, una vez que 'db' ya está inicializado
from controllers import usuario_controller, medico_controller, paciente_controller, consulta_controller

# Registro de Blueprints
app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(medico_controller.medico_bp)
app.register_blueprint(paciente_controller.paciente_bp)
app.register_blueprint(consulta_controller.consulta_bp)

# Context processor para manejar la clase 'active' en la navegación
@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path.startswith(path) else ''
    return dict(is_active=is_active)

# Ruta de inicio
@app.route('/')
def home():
    from models.medico_model import Medico
    from models.paciente_model import Paciente
    from models.consulta_model import Consulta
    total_medicos = len(Medico.get_all())
    total_pacientes = len(Paciente.get_all())
    total_consultas = len(Consulta.get_all())
    from flask import render_template
    return render_template('index.html',
                           total_medicos=total_medicos,
                           total_pacientes=total_pacientes,
                           total_consultas=total_consultas)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
