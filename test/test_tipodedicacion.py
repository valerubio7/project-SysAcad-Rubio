import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.tipodedicacion import TipoDedicacion

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

    def test_tipodedicacion_creation(self):
        tipodedicacion = TipoDedicacion()
        tipodedicacion.nombre = "Dedicacion Completa"
        tipodedicacion.observacion = "Observacion de prueba"

        # Save to database
        db.session.add(tipodedicacion)
        db.session.commit()

        # Verify it was saved
        self.assertIsNotNone(tipodedicacion.id)