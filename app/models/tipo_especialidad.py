"""
This module defines the `TipoEspecialidad` class.

"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class TipoEspecialidad(db.Model):
    """
    Represents a type of specialty in the system.

    Attributes:
        id (int): The unique identifier for the specialty type.
        nombre (str): The name of the specialty type.
    """
    __tablename__ = 'tipoespecialidades'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
