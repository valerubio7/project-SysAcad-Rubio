"""
This module defines the `TipoDocumento` class.

"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class TipoDocumento(db.Model):
    """
    Represents a type of document in the system.

    """
    __tablename__ = 'tipo_documento'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dni: str = db.Column(db.String(50), nullable=False)
    libreta_civica: str = db.Column(db.String(50), nullable=True)
    libreta_enrolamiento: str = db.Column(db.String(50), nullable=True)
    pasaporte: str = db.Column(db.String(50), nullable=True)
