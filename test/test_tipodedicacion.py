import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.tipo_dedicacion import TipoDedicacion

class TipoDedicacionTestCase(unittest.TestCase):
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

    def test_tipodedicacion_create(self):
        tipo = TipoDedicacion(nombre="Exclusiva")
        db.session.add(tipo)
        db.session.commit()
        self.assertIsNotNone(tipo.id)

    def test_tipodedicacion_read(self):
        tipo = TipoDedicacion(nombre="Simple")
        db.session.add(tipo)
        db.session.commit()
        found = TipoDedicacion.query.filter_by(nombre="Simple").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.nombre, "Simple")

    def test_tipodedicacion_update(self):
        tipo = TipoDedicacion(nombre="Parcial")
        db.session.add(tipo)
        db.session.commit()
        tipo.nombre = "Completa"
        db.session.commit()
        updated = TipoDedicacion.query.get(tipo.id)
        self.assertEqual(updated.nombre, "Completa")

    def test_tipodedicacion_delete(self):
        tipo = TipoDedicacion(nombre="Temporal")
        db.session.add(tipo)
        db.session.commit()
        db.session.delete(tipo)
        db.session.commit()
        deleted = TipoDedicacion.query.get(tipo.id)
        self.assertIsNone(deleted)