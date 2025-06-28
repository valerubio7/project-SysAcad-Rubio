"""
This module defines the `Materia` class.

"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    """
    Represents a subject in the system.

    """
    __tablename__ = 'materia'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(20), nullable=False)
    observacion = db.Column(db.String(255), nullable=True)
