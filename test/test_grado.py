import unittest
import os
from app import create_app
from app.models import Grado
from app.services import GradoService
from app import db


class GradoTestCase(unittest.TestCase):
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

    def test_grado_creation(self):
        grado = self.__nuevogrado()
        self.assertIsNotNone(grado)
        self.assertEqual(grado.nombre, "Primero")
        self.assertIsNotNone(grado.descripcion, "Descripción del primer grado")

    def test_crear_grado(self):
        grado = self.__nuevogrado()
        GradoService.crear_grado(grado)
        self.assertIsNotNone(grado)
        self.assertIsNotNone(grado.id)
        self.assertGreaterEqual(grado.id, 1)
        self.assertEqual(grado.nombre, "Primero")

    def test_grado_busqueda(self):
        grado = self.__nuevogrado()
        GradoService.crear_grado(grado)
        r=GradoService.buscar_por_id(grado.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Primero")
        self.assertEqual(r.descripcion, "Descripción del primer grado")

    
    def test_buscar_grados(self):
        grado1 = self.__nuevogrado()
        grado2 = self.__nuevogrado()
        GradoService.crear_grado(grado1)
        GradoService.crear_grado(grado2)
        grados = GradoService.buscar_todos()
        self.assertIsNotNone(grados)
        self.assertGreaterEqual(len(grados), 2)

    def test_actualizar_grado(self):
        grado= self.__nuevogrado()
        GradoService.crear_grado(grado)
        grado.nombre = "Segundo"
        grado.descripcion = "Descripción del segundo grado"

    def test_borrar_grado(self):
        universidad = self.__nuevogrado()
        GradoService.crear_grado(universidad)
        GradoService.borrar_por_id(universidad.id)
        resultado = GradoService.buscar_por_id(universidad.id)
        self.assertIsNone(resultado)

    def test_grado_create(self):
        grado = Grado(nombre="Licenciatura", descripcion="Título de grado")
        db.session.add(grado)
        db.session.commit()
        self.assertIsNotNone(grado.id)

    def test_grado_read(self):
        grado = Grado(nombre="Ingeniería", descripcion="Título de ingeniería")
        db.session.add(grado)
        db.session.commit()
        found = Grado.query.filter_by(nombre="Ingeniería").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.nombre, "Ingeniería")

    def test_grado_update(self):
        grado = Grado(nombre="Tecnicatura", descripcion="Título de tecnicatura")
        db.session.add(grado)
        db.session.commit()
        grado.nombre = "Doctorado"
        db.session.commit()
        updated = db.session.get(Grado, grado.id)
        self.assertEqual(updated.nombre, "Doctorado")

    def test_grado_delete(self):
        grado = Grado(nombre="Maestría", descripcion="Título de maestría")
        db.session.add(grado)
        db.session.commit()
        db.session.delete(grado)
        db.session.commit()
        deleted = db.session.get(Grado, grado.id)
        self.assertIsNone(deleted)

    def __nuevogrado(self):
        grado = Grado()
        grado.nombre = "Primero"
        grado.descripcion = "Descripción del primer grado"
        return grado