import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.materia import Materia

class MateriaTestCase(unittest.TestCase):
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

    def test_materia_create(self):
        materia = Materia(nombre="Matemática", codigo="MAT101", observacion="Básica")
        db.session.add(materia)
        db.session.commit()
        self.assertIsNotNone(materia.id)

    def test_materia_read(self):
        materia = Materia(nombre="Física", codigo="FIS101", observacion="General")
        db.session.add(materia)
        db.session.commit()
        found = Materia.query.filter_by(nombre="Física").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.codigo, "FIS101")

    def test_materia_update(self):
        materia = Materia(nombre="Química", codigo="QUI101", observacion="Laboratorio")
        db.session.add(materia)
        db.session.commit()
        materia.observacion = "Teórica"
        db.session.commit()
        updated = db.session.get(Materia, materia.id)
        self.assertEqual(updated.observacion, "Teórica")

    def test_materia_delete(self):
        materia = Materia(nombre="Historia", codigo="HIS101", observacion="Sociales")
        db.session.add(materia)
        db.session.commit()
        db.session.delete(materia)
        db.session.commit()
        deleted = db.session.get(Materia, materia.id)
        self.assertIsNone(deleted)