"""
This module defines the `Cargo` class.
"""

from dataclasses import dataclass
from app import db
from app.models.categoria_cargo import CategoriaCargo
from app.models.tipo_dedicacion import TipoDedicacion


@dataclass(init=False, repr=True, eq=True)
class Cargo(db.Model):
    """
    Represents a job position in the system.
    """
    __tablename__ = 'cargo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    puntos = db.Column(db.Integer, nullable=False)
    categoria_cargo_id = db.Column(
        db.Integer, db.ForeignKey('categoria_cargo.id')
    )
    categoria_cargo = db.relationship('CategoriaCargo', backref='cargos')
    tipo_dedicacion_id = db.Column(
        db.Integer, db.ForeignKey('tipo_dedicacion.id')
    )
    tipo_dedicacion = db.relationship('TipoDedicacion', backref='cargos')
