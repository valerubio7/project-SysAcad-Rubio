import unittest
import os
from flask import current_app
from app import create_app
from app.models import Universidad
from app.services import UniversidadService
from app import db

class UniversidadTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        self.app_context.pop()

    def test_universidad_creation(self):
        universidad = self.__nuevauniversidad()
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.nombre)
        self.assertEqual(universidad.nombre, "Universidad Nacional")
        self.assertEqual(universidad.sigla, "UN")

    def test_crear_universidad(self):
        universidad = self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad)
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad.id, 1)
        self.assertEqual(universidad.nombre, "Universidad Nacional")

    def test_universidad_busqueda(self):
        universidad = self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad)
        r=UniversidadService.buscar_por_id(universidad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Universidad Nacional")
        self.assertEqual(r.sigla, "UN")
    
    def test_buscar_universidades(self):
        universidad1 = self.__nuevauniversidad()
        universidad2 = self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad1)
        UniversidadService.crear_universidad(universidad2)
        universidades = UniversidadService.buscar_todos()
        self.assertIsNotNone(universidades)
        self.assertEqual(len(universidades), 2)

    def test_actualizar_universidad(self):
        universidad = self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad)
        universidad.nombre = "Universidad Actualizada"
        universidad_actualizada = UniversidadService.actualizar_universidad(universidad.id,universidad)
        self.assertEqual(universidad_actualizada.nombre, "Universidad Actualizada")

    def test_borrar_universidad(self):
        universidad = self.__nuevauniversidad()
        UniversidadService.crear_universidad(universidad)
        UniversidadService.borrar_por_id(universidad.id)
        resultado = UniversidadService.buscar_por_id(universidad.id)
        self.assertIsNone(resultado)

    def test_universidad_create(self):
        universidad = Universidad(nombre="UTN", sigla="UTN")
        db.session.add(universidad)
        db.session.commit()
        self.assertIsNotNone(universidad.id)

    def test_universidad_read(self):
        universidad = Universidad(nombre="UBA", sigla="UBA")
        db.session.add(universidad)
        db.session.commit()
        found = Universidad.query.filter_by(nombre="UBA").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.sigla, "UBA")

    def test_universidad_update(self):
        universidad = Universidad(nombre="UNLP", sigla="UNLP")
        db.session.add(universidad)
        db.session.commit()
        universidad.sigla = "UNLZ"
        db.session.commit()
        updated = db.session.get(Universidad, universidad.id)
        self.assertEqual(updated.sigla, "UNLZ")

    def test_universidad_delete(self):
        universidad = Universidad(nombre="UNC", sigla="UNC")
        db.session.add(universidad)
        db.session.commit()
        db.session.delete(universidad)
        db.session.commit()
        deleted = db.session.get(Universidad, universidad.id)
        self.assertIsNone(deleted)

    def __nuevauniversidad(self):
        universidad = Universidad()
        universidad.nombre = "Universidad Nacional"
        universidad.sigla = "UN"
        return universidad