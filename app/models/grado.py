"""
This module defines the `Grado` class.

The class represents a grade or level in the system.
"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Grado(db.Model):
    """
    Represents a grade or level in the system.

    Attributes:
        id (int): The unique identifier for the grade.
        nombre (str): The name of the grade.
        descripcion (str): A description of the grade.
    """
    __tablename__ = 'grados'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(50), nullable=False)
    descripcion: str = db.Column(db.String(200), nullable=False)
