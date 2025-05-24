from dataclasses import dataclass
from datetime import date
from app import db
from app.models.tipo_documento import TipoDocumento

@dataclass(init=False, repr=True, eq=True)
class Alumno(db.Model):
    __tablename__ = 'alumno'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(80), nullable=False)
    apellido: str = db.Column(db.String(80), nullable=False)
    nrodocumento: str = db.Column(db.String(20), nullable=False)
    tipo_documento_id: int = db.Column(db.Integer, db.ForeignKey('tipo_documento.id'))
    tipo_documento = db.relationship('TipoDocumento', backref='alumnos')
    fecha_nacimiento: date = db.Column(db.Date, nullable=False)
    sexo: str = db.Column(db.String(1), nullable=False)
    nro_legajo: int = db.Column(db.Integer, nullable=False)
    fecha_ingreso: date = db.Column(db.Date, nullable=False)