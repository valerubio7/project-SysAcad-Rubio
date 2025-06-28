"""
This module defines the `Area` class, which represents an area in the system.

The `Area` class includes attributes to store the name of the area.
"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Area(db.Model):
    """
    Represents an area in the system.
    """
    __tablename__ = 'area'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
