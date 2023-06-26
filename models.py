from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Preceptor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Puede ser 'preceptor', 'padre' o 'tutor'

    def __repr__(self):
        return f"Usuario(id={self.id}, nombre={self.nombre}, email={self.email}, tipo={self.tipo})"

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Curso(id={self.id}, nombre={self.nombre})"

class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)
    estudiante = db.relationship('Estudiante', backref=db.backref('asistencias', lazy=True))
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    presente = db.Column(db.Boolean, nullable=False)
    justificado = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Asistencia(id={self.id}, estudiante={self.estudiante}, fecha={self.fecha}, presente={self.presente}, justificado={self.justificado})"