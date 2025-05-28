"""
This module defines the `Orientacion` class.

"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Orientacion(db.Model):
    """
    Represents an orientation in the system.

    """
    __tablename__ = 'orientacion'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    observacion: str = db.Column(db.String(255), nullable=True)
    especialidad_id: int = db.Column(
        db.Integer, db.ForeignKey('especialidades.id')
    )
    especialidad = db.relationship('Especialidad', backref='orientaciones')
    plan_id: int = db.Column(db.Integer, db.ForeignKey('plan.id'))
    plan = db.relationship('Plan', backref='orientaciones')
    materia_id: int = db.Column(db.Integer, db.ForeignKey('materia.id'))
    materia = db.relationship('Materia', backref='orientaciones')
