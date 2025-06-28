"""
This module defines the `Facultad` class.

"""

from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Facultad(db.Model):
    """
    Represents a faculty in the system.

    """
    __tablename__ = 'facultad'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    abreviatura = db.Column(db.String(10), nullable=False)
    directorio = db.Column(db.String(255), nullable=False)
    sigla = db.Column(db.String(10), nullable=True)
    codigopostal = db.Column(db.String(10), nullable=True)
    ciudad = db.Column(db.String(100), nullable=True)
    domicilio = db.Column(db.String(255), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)
    contacto = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
