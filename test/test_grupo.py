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

    def test_grupo_create(self):
        grupo = Grupo(nombre="Grupo A")
        db.session.add(grupo)
        db.session.commit()
        self.assertIsNotNone(grupo.id)

    def test_grupo_read(self):
        grupo = Grupo(nombre="Grupo B")
        db.session.add(grupo)
        db.session.commit()
        found = Grupo.query.filter_by(nombre="Grupo B").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.nombre, "Grupo B")

    def test_grupo_update(self):
        grupo = Grupo(nombre="Grupo C")
        db.session.add(grupo)
        db.session.commit()
        grupo.nombre = "Grupo D"
        db.session.commit()
        updated = db.session.get(Grupo, grupo.id)
        self.assertEqual(updated.nombre, "Grupo D")

    def test_grupo_delete(self):
        grupo = Grupo(nombre="Grupo E")
        db.session.add(grupo)
        db.session.commit()
        db.session.delete(grupo)
        db.session.commit()
        deleted = db.session.get(Grupo, grupo.id)
        self.assertIsNone(deleted)