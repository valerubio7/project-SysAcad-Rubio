from dataclasses import dataclass
from app import db
from app.models.especialidad import Especialidad
from app.models.plan import Plan
from app.models.materia import Materia

@dataclass(init=False, repr=True, eq=True)
class Orientacion(db.Model):
    __tablename__ = 'orientacion'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    observacion: str = db.Column(db.String(255), nullable=True)
    especialidad_id: int = db.Column(db.Integer, db.ForeignKey('especialidad.id'))
    especialidad = db.relationship('Especialidad', backref='orientaciones')
    plan_id: int = db.Column(db.Integer, db.ForeignKey('plan.id'))
    plan = db.relationship('Plan', backref='orientaciones')
    materia_id: int = db.Column(db.Integer, db.ForeignKey('materia.id'))
    materia = db.relationship('Materia', backref='orientaciones')