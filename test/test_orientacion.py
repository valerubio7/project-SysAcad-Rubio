import unittest
import os
import datetime
from flask import current_app
from app import create_app, db
from app.models.orientacion import Orientacion
from app.models.especialidad import Especialidad
from app.models.plan import Plan
from app.models.materia import Materia


class OrientacionTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()  # Crear todas las tablas necesarias
        # Eliminadas las migraciones Alembic para evitar conflicto de contextos

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # Limpiar todas las tablas
        self.app_context.pop()

    def test_orientacion_create(self):
        especialidad = Especialidad(nombre="Especialidad X", letra="X", observacion="Obs X")
        db.session.add(especialidad)
        db.session.commit()
        plan = Plan(nombre="Plan X", fecha_inicio="2025-01-01", fecha_fin="2025-12-31", observacion="Obs Plan")
        db.session.add(plan)
        db.session.commit()
        materia = Materia(nombre="Materia X", codigo="MATX", observacion="Obs Mat")
        db.session.add(materia)
        db.session.commit()
        orientacion = Orientacion(nombre="Orientación X", observacion="Obs Ori", especialidad=especialidad, plan=plan, materia=materia)
        db.session.add(orientacion)
        db.session.commit()
        self.assertIsNotNone(orientacion.id)

    def test_orientacion_read(self):
        especialidad = Especialidad(nombre="Especialidad Y", letra="Y", observacion="Obs Y")
        db.session.add(especialidad)
        db.session.commit()
        plan = Plan(nombre="Plan Y", fecha_inicio="2026-01-01", fecha_fin="2026-12-31", observacion="Obs Plan Y")
        db.session.add(plan)
        db.session.commit()
        materia = Materia(nombre="Materia Y", codigo="MATY", observacion="Obs Mat Y")
        db.session.add(materia)
        db.session.commit()
        orientacion = Orientacion(nombre="Orientación Y", observacion="Obs Ori Y", especialidad=especialidad, plan=plan, materia=materia)
        db.session.add(orientacion)
        db.session.commit()
        found = Orientacion.query.filter_by(nombre="Orientación Y").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.observacion, "Obs Ori Y")

    def test_orientacion_update(self):
        especialidad = Especialidad(nombre="Especialidad Z", letra="Z", observacion="Obs Z")
        db.session.add(especialidad)
        db.session.commit()
        plan = Plan(nombre="Plan Z", fecha_inicio="2027-01-01", fecha_fin="2027-12-31", observacion="Obs Plan Z")
        db.session.add(plan)
        db.session.commit()
        materia = Materia(nombre="Materia Z", codigo="MATZ", observacion="Obs Mat Z")
        db.session.add(materia)
        db.session.commit()
        orientacion = Orientacion(nombre="Orientación Z", observacion="Obs Ori Z", especialidad=especialidad, plan=plan, materia=materia)
        db.session.add(orientacion)
        db.session.commit()
        orientacion.observacion = "Obs Ori Z Actualizada"
        db.session.commit()
        updated = db.session.get(Orientacion, orientacion.id)
        self.assertEqual(updated.observacion, "Obs Ori Z Actualizada")

    def test_orientacion_delete(self):
        especialidad = Especialidad(nombre="Especialidad W", letra="W", observacion="Obs W")
        db.session.add(especialidad)
        db.session.commit()
        plan = Plan(nombre="Plan W", fecha_inicio="2028-01-01", fecha_fin="2028-12-31", observacion="Obs Plan W")
        db.session.add(plan)
        db.session.commit()
        materia = Materia(nombre="Materia W", codigo="MATW", observacion="Obs Mat W")
        db.session.add(materia)
        db.session.commit()
        orientacion = Orientacion(nombre="Orientación W", observacion="Obs Ori W", especialidad=especialidad, plan=plan, materia=materia)
        db.session.add(orientacion)
        db.session.commit()
        db.session.delete(orientacion)
        db.session.commit()
        deleted = db.session.get(Orientacion, orientacion.id)
        self.assertIsNone(deleted)