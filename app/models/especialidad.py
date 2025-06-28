"""
This module defines the `Especialidad` class.

"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Especialidad(db.Model):
    """
    Represents a specialty in the system.

    """
    __tablename__ = 'especialidades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    letra = db.Column(db.String(1), nullable=False)
    observacion = db.Column(db.String(255), nullable=True)
