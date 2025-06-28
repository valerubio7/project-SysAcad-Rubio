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

    def test_cargo_create(self):
        cargo = Cargo(nombre="Titular", puntos=10)
        db.session.add(cargo)
        db.session.commit()
        self.assertIsNotNone(cargo.id)

    def test_cargo_read(self):
        cargo = Cargo(nombre="Adjunto", puntos=8)
        db.session.add(cargo)
        db.session.commit()
        found = Cargo.query.filter_by(nombre="Adjunto").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.puntos, 8)

    def test_cargo_update(self):
        cargo = Cargo(nombre="JTP", puntos=6)
        db.session.add(cargo)
        db.session.commit()
        cargo.puntos = 7
        db.session.commit()
        updated = db.session.get(Cargo, cargo.id)
        self.assertEqual(updated.puntos, 7)

    def test_cargo_delete(self):
        cargo = Cargo(nombre="Ayudante", puntos=4)
        db.session.add(cargo)
        db.session.commit()
        db.session.delete(cargo)
        db.session.commit()
        deleted = db.session.get(Cargo, cargo.id)
        self.assertIsNone(deleted)