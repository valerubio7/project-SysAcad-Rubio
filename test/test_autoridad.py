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

    def test_autoridad_read(self):
        cargo = Cargo(nombre="Vicedecano", puntos=2)
        db.session.add(cargo)
        db.session.commit()
        autoridad = Autoridad(nombre="Juan", cargo=cargo, telefono="987654321", email="juan@gmail.com")
        db.session.add(autoridad)
        db.session.commit()
        found = Autoridad.query.filter_by(nombre="Juan").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.telefono, "987654321")
        self.assertEqual(found.cargo.nombre, "Vicedecano")

    def test_autoridad_update(self):
        cargo = Cargo(nombre="Secretario", puntos=3)
        db.session.add(cargo)
        db.session.commit()
        autoridad = Autoridad(nombre="Ana", cargo=cargo, telefono="111222333", email="ana@gmail.com")
        db.session.add(autoridad)
        db.session.commit()
        autoridad.telefono = "444555666"
        db.session.commit()
        updated = db.session.get(Autoridad, autoridad.id)
        self.assertEqual(updated.telefono, "444555666")

    def test_autoridad_delete(self):
        cargo = Cargo(nombre="Prosecretario", puntos=4)
        db.session.add(cargo)
        db.session.commit()
        autoridad = Autoridad(nombre="Luis", cargo=cargo, telefono="555666777", email="luis@gmail.com")
        db.session.add(autoridad)
        db.session.commit()
        db.session.delete(autoridad)
        db.session.commit()
        deleted = db.session.get(Autoridad, autoridad.id)
        self.assertIsNone(deleted)