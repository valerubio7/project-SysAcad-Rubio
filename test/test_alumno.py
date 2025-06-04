import unittest
import os
from flask import current_app
from app import create_app
from datetime import date
from app.models.tipodocumento import TipoDocumento
from app.models.alumno import Alumno
from app.services import AlumnoService
from app.services import TipoDocumentoService
from app import db
class AlumnoTestCase(unittest.TestCase):

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

    def test_alumno_creation(self):
        tipo_documento = TipoDocumento(dni="DNI")
        db.session.add(tipo_documento)
        db.session.commit()
        alumno = Alumno(nombre="Juan", apellido="Pérez", nrodocumento="12345678", tipo_documento_id=tipo_documento.id, fecha_nacimiento=date(2000, 1, 1), sexo="M", nro_legajo=1, fecha_ingreso=date(2020, 3, 1))
        db.session.add(alumno)
        db.session.commit()
        self.assertIsNotNone(alumno.id)

    def test_alumno_read(self):
        tipo_documento = TipoDocumento(dni="DNI")
        db.session.add(tipo_documento)
        db.session.commit()
        alumno = Alumno(nombre="Ana", apellido="García", nrodocumento="87654321", tipo_documento_id=tipo_documento.id, fecha_nacimiento=date(2001, 2, 2), sexo="F", nro_legajo=2, fecha_ingreso=date(2021, 3, 1))
        db.session.add(alumno)
        db.session.commit()
        found = Alumno.query.filter_by(nombre="Ana").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.apellido, "García")

    def test_alumno_update(self):
        tipo_documento = TipoDocumento(dni="DNI")
        db.session.add(tipo_documento)
        db.session.commit()
        alumno = Alumno(nombre="Luis", apellido="Martínez", nrodocumento="11223344", tipo_documento_id=tipo_documento.id, fecha_nacimiento=date(2002, 3, 3), sexo="M", nro_legajo=3, fecha_ingreso=date(2022, 3, 1))
        db.session.add(alumno)
        db.session.commit()
        alumno.apellido = "López"
        db.session.commit()
        updated = db.session.get(Alumno, alumno.id)
        self.assertEqual(updated.apellido, "López")

    def test_alumno_delete(self):
        tipo_documento = TipoDocumento(dni="DNI")
        db.session.add(tipo_documento)
        db.session.commit()
        alumno = Alumno(nombre="Sofía", apellido="Fernández", nrodocumento="44332211", tipo_documento_id=tipo_documento.id, fecha_nacimiento=date(2003, 4, 4), sexo="F", nro_legajo=4, fecha_ingreso=date(2023, 3, 1))
        db.session.add(alumno)
        db.session.commit()
        db.session.delete(alumno)
        db.session.commit()
        deleted = db.session.get(Alumno, alumno.id)
        self.assertIsNone(deleted)

    def test_crear(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear(alumno)
        self.assertIsNotNone(alumno)
        self.assertIsNotNone(alumno.nombre)
        self.assertGreaterEqual(alumno.id, 1)
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.tipo_documento.pasaporte, "nacnal")

    def test_busqueda(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear(alumno)
        r=AlumnoService.buscar_por_id(alumno.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Juan")
        self.assertEqual(r.apellido, "Pérez")

    def test_buscar_todos(self):
        alumno1 = self.__nuevoalumno()
        alumno2 = self.__nuevoalumno(nombre="Pedro", apellido="Gómez", nrodocumento="12345678", tipo_documento=None, fecha_nacimiento=date(1995,5,5), sexo="M", nro_legajo=654321, fecha_ingreso=date(2021,1,1), dni= "na", libreta_civica="l", libreta_enrolamiento="aci", pasaporte="nacn")
        AlumnoService.crear(alumno1)
        AlumnoService.crear(alumno2)
        alumnos = AlumnoService.buscar_todos()
        self.assertIsNotNone(alumnos)
        self.assertEqual(len(alumnos), 2)

    def test_actualizar(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear(alumno)
        alumno.nombre = "Juan actualizado"
        alumno_actualizado = AlumnoService.actualizar(alumno.id, alumno)
        self.assertEqual(alumno_actualizado.nombre, "Juan actualizado")
    
    def test_borrar(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear(alumno)
        AlumnoService.borrar_por_id(alumno.id)
        resultado = AlumnoService.buscar_por_id(alumno.id)
        self.assertIsNone(resultado)

    def __nuevoalumno(self, nombre="Juan", apellido="Pérez", nrodocumento="46291002" ,tipo_documento=None, fecha_nacimiento=date(1990,1,1), sexo="M", nro_legajo=123456, fecha_ingreso=date(2020,1,1),
                      dni= "nacnal", libreta_civica="nacional", libreta_enrolamiento="naci", pasaporte="nacnal"):
        tipo_documento = TipoDocumento()
        tipo_documento.pasaporte = pasaporte
        tipo_documento.dni = dni
        tipo_documento.libreta_civica = libreta_civica
        tipo_documento.libreta_enrolamiento = libreta_enrolamiento
        TipoDocumentoService.crear(tipo_documento)
        
        alumno = Alumno()
        alumno.nombre =  nombre
        alumno.apellido = apellido
        alumno.nrodocumento = nrodocumento
        alumno.tipo_documento = tipo_documento
        alumno.fecha_nacimiento = fecha_nacimiento
        alumno.sexo = sexo
        alumno.nro_legajo = nro_legajo
        alumno.fecha_ingreso = fecha_ingreso
        return alumno
