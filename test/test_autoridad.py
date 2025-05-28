import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.autoridad import Autoridad
from app.models.cargo import Cargo

class AutoridadTestCase(unittest.TestCase):
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

    def test_autoridad_creation(self):
        # Crear y guardar un cargo
        cargo = Cargo()
        cargo.nombre = "Decano"
        cargo.puntos = 1  # Asignar valor obligatorio
        db.session.add(cargo)
        db.session.commit()

        # Crear y guardar una autoridad
        autoridad = Autoridad()
        autoridad.nombre = "Pelo"
        autoridad.cargo = cargo
        autoridad.telefono = "123456789"
        autoridad.email = "123@gmail.com"
        db.session.add(autoridad)
        db.session.commit()

        # Validar que la autoridad fue creada correctamente
        self.assertIsNotNone(autoridad.id)
        self.assertEqual(autoridad.nombre, "Pelo")
        self.assertEqual(autoridad.cargo.nombre, "Decano")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "123@gmail.com")

        # Validar relación entre Autoridad y Cargo
        self.assertIsNotNone(autoridad.cargo)
        self.assertEqual(autoridad.cargo.id, cargo.id)