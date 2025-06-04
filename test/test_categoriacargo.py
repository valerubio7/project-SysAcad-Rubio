import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.categoria_cargo import CategoriaCargo


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

    def test_categoriacargo_create(self):
        categoria = CategoriaCargo(nombre="Docente")
        db.session.add(categoria)
        db.session.commit()
        self.assertIsNotNone(categoria.id)

    def test_categoriacargo_read(self):
        categoria = CategoriaCargo(nombre="Investigador")
        db.session.add(categoria)
        db.session.commit()
        found = CategoriaCargo.query.filter_by(nombre="Investigador").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.nombre, "Investigador")

    def test_categoriacargo_update(self):
        categoria = CategoriaCargo(nombre="Extensionista")
        db.session.add(categoria)
        db.session.commit()
        categoria.nombre = "Administrativo"
        db.session.commit()
        updated = db.session.get(CategoriaCargo, categoria.id)
        self.assertEqual(updated.nombre, "Administrativo")

    def test_categoriacargo_delete(self):
        categoria = CategoriaCargo(nombre="Becario")
        db.session.add(categoria)
        db.session.commit()
        db.session.delete(categoria)
        db.session.commit()
        deleted = db.session.get(CategoriaCargo, categoria.id)
        self.assertIsNone(deleted)
