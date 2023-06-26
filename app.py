from datetime import datetime
from flask import Flask, request, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db 
from models import Preceptor, Curso, Asistencia



@app.route('/')
def saludo():
    return render_template('index.html')

@app.route('/iniciosesion', methods=['POST', 'GET'])
def inisiosesion():
    if request.method == 'POST':
        rol = request.form.get('Rol')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validar nombre, correo y contraseña
        if nombre == 'NombreCorrecto' and email == 'example@example.com' and password == 'password123':
            if rol == 'preceptor':
                # Redirigir a la página de funcionalidad para preceptores
                return redirect(url_for('pagina_preceptor'))
            elif rol == 'padre' or rol == 'tutor':
                # Redirigir a la página de funcionalidad para padres o tutores
                return redirect(url_for('pagina_padre_tutor'))
        else:
            return 'Credenciales incorrectas'

    return render_template('iniciosesion.html')

@app.route('/registrar_asistencia', methods=['POST'])
def registrar_asistencia():
    curso = request.form.get('curso')
    clase = request.form.get('clase')
    fecha = request.form.get('fecha')
    asistencia = request.form.getlist('asistencia')
    justificaciones = request.form.getlist('justificaciones')

    

    return 'Asistencia registrada correctamente'

@app.route('/pagina_preceptor')
def pagina_preceptor():
    # Obtener la lista de estudiantes asignados al preceptor (puedes reemplazar esta lista con los datos de tu base de datos)
    estudiantes = ['Estudiante 1', 'Estudiante 2', 'Estudiante 3']

    return render_template('pagina_preceptor.html', estudiantes=estudiantes)

@app.route('/informe_detalles', methods=['POST'])
def generar_informe_detalles():
    # Obtener el curso seleccionado por el preceptor
    curso = request.form.get('curso')

    
    return render_template('informe_detalles.html', curso=curso, informe=informe)

if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()