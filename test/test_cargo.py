import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo
from app.models.tipo_dedicacion import TipoDedicacion

class CargoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()  # Crear todas las tablas necesarias

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # Limpiar todas las tablas
        self.app_context.pop()

    def test_cargo_creation(self):
        cargo = Cargo()
        cargo.nombre = "profesor"
        cargo.puntos = 10

        categoria_cargo = CategoriaCargo()
        categoria_cargo.nombre = "Categoria A"
        db.session.add(categoria_cargo)
        db.session.commit()

        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre = "Full Time"
        db.session.add(tipo_dedicacion)
        db.session.commit()

        cargo.categoria_cargo = categoria_cargo
        cargo.tipo_dedicacion = tipo_dedicacion

        db.session.add(cargo)
        db.session.commit()

        self.assertIsNotNone(cargo.id)