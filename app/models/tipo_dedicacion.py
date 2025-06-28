"""
This module defines the `TipoDedicacion` class.

"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class TipoDedicacion(db.Model):
    """
    Represents a type of dedication in the system.

    """
    __tablename__ = 'tipo_dedicacion'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    observacion = db.Column(db.String(255), nullable=True)
