"""
This module defines the `Autoridad` class.

"""

from dataclasses import dataclass
from app import db
from app.models.cargo import Cargo


@dataclass(init=False, repr=True, eq=True)
class Autoridad(db.Model):
    """
    Represents an authority figure in the system.

    """
    __tablename__ = 'autoridad'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cargo_id = db.Column(db.Integer, db.ForeignKey('cargo.id'))
    cargo = db.relationship('Cargo', backref='autoridades')
