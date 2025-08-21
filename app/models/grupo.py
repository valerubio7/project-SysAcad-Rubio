"""
This module defines the `Grupo` class.

The class represents a group in the system.
"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Grupo(db.Model):
    """
    Represents a group in the system.
    """
    __tablename__ = 'grupo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
