import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.categoriacargo import CategoriaCargo


class CategoriaCargoTestCase(unittest.TestCase):
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

    def test_categoriacargo_creation(self):
        categoria = CategoriaCargo()
        categoria.nombre = "Docente"

        db.session.add(categoria)
        db.session.commit()

        self.assertIsNotNone(categoria.id)
        self.assertEqual(categoria.nombre, "Docente")
