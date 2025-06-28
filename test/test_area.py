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

    def test_area_read(self):
        area = Area(nombre="fisica")
        db.session.add(area)
        db.session.commit()
        found = Area.query.filter_by(nombre="fisica").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.nombre, "fisica")

    def test_area_update(self):
        area = Area(nombre="quimica")
        db.session.add(area)
        db.session.commit()
        area.nombre = "biologia"
        db.session.commit()
        updated = db.session.get(Area, area.id)
        self.assertEqual(updated.nombre, "biologia")

    def test_area_delete(self):
        area = Area(nombre="geografia")
        db.session.add(area)
        db.session.commit()
        db.session.delete(area)
        db.session.commit()
        deleted = db.session.get(Area, area.id)
        self.assertIsNone(deleted)