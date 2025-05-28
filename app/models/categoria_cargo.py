"""
This module defines the `CategoriaCargo` class.

The class represents a category of job positions.
"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class CategoriaCargo(db.Model):
    """
    Represents a category of job positions in the system.
    """
    __tablename__ = 'categoria_cargo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
