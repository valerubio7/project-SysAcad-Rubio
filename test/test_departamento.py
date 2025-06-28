import unittest
import os
from flask import current_app
from app import create_app
from app.models.departamento import Departamento
from app.services import DepartamentoService
from app import db

class DepartamentoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_departamento_creation(self):
        departamento = self.__nuevodepartamento()
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.nombre)
        self.assertEqual(departamento.nombre, "Matematicas")

    
    def test_crear(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear(departamento)
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.id)
        self.assertGreaterEqual(departamento.id, 1)
        self.assertEqual(departamento.nombre, "Matematicas")

    def test_busqueda(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear(departamento)
        r=DepartamentoService.buscar_por_id(departamento.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Matematicas")
        

    def test_buscar_todos(self):
        departamento1 = self.__nuevodepartamento()
        departamento2 = self.__nuevodepartamento("Fisica")
        DepartamentoService.crear(departamento1)
        DepartamentoService.crear(departamento2)
        departamentos = DepartamentoService.buscar_todos()
        self.assertIsNotNone(departamentos)
        self.assertEqual(len(departamentos), 2)

    def test_actualizar(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear(departamento)
        departamento.nombre = "Matematicas actualizado"
        departamento_actualizado = DepartamentoService.actualizar(departamento.id, departamento)
        self.assertEqual(departamento_actualizado.nombre, "Matematicas actualizado")
    
    def test_borrar(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear(departamento)
        DepartamentoService.borrar_por_id(departamento.id)
        resultado = DepartamentoService.buscar_por_id(departamento.id)
        self.assertIsNone(resultado)
        
    def __nuevodepartamento(self , nombre = "Matematicas"):
        departamento = Departamento()
        departamento.nombre = nombre
        return departamento

    def test_departamento_create(self):
        departamento = Departamento(nombre="Ciencias Básicas")
        db.session.add(departamento)
        db.session.commit()
        self.assertIsNotNone(departamento.id)

    def test_departamento_read(self):
        departamento = Departamento(nombre="Ingeniería")
        db.session.add(departamento)
        db.session.commit()
        found = Departamento.query.filter_by(nombre="Ingeniería").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.nombre, "Ingeniería")

    def test_departamento_update(self):
        departamento = Departamento(nombre="Electrónica")
        db.session.add(departamento)
        db.session.commit()
        departamento.nombre = "Informática"
        db.session.commit()
        updated = db.session.get(Departamento, departamento.id)
        self.assertEqual(updated.nombre, "Informática")

    def test_departamento_delete(self):
        departamento = Departamento(nombre="Química")
        db.session.add(departamento)
        db.session.commit()
        db.session.delete(departamento)
        db.session.commit()
        deleted = db.session.get(Departamento, departamento.id)
        self.assertIsNone(deleted)