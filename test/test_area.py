import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.area import Area

class AreaTestCase(unittest.TestCase):
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

    def test_area_creation(self):
        area = Area()
        area.nombre = "matematica"

        # Save to database
        db.session.add(area)
        db.session.commit()

        # Verify it was saved
        self.assertIsNotNone(area.id)