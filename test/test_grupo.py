import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.grupo import Grupo

class GrupoTestCase(unittest.TestCase):
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

    def test_grupo_creation(self):
        grupo = Grupo()
        grupo.nombre = "Grupo A"

        # Save to database
        db.session.add(grupo)
        db.session.commit()

        # Verify it was saved
        self.assertIsNotNone(grupo.id)