import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.orientacion import Orientacion
from app.models.especialidad import Especialidad
from app.models.plan import Plan
from app.models.materia import Materia
from alembic.command import upgrade
from alembic.config import Config


class OrientacionTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()  # Crear todas las tablas necesarias

        # Apply Alembic migrations
        alembic_cfg = Config("migrations/alembic.ini")
        upgrade(alembic_cfg, "head")

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # Limpiar todas las tablas
        self.app_context.pop()

    def test_orientacion_creation(self):
        especialidad = Especialidad()
        especialidad.nombre = "Especialidad A"
        db.session.add(especialidad)
        db.session.commit()

        plan = Plan()
        plan.nombre = "Plan A"
        db.session.add(plan)
        db.session.commit()

        materia = Materia()
        materia.nombre = "Materia A"
        db.session.add(materia)
        db.session.commit()

        orientacion = Orientacion()
        orientacion.nombre = "Orientacion A"
        orientacion.observacion = "Observacion de prueba"
        orientacion.especialidad = especialidad
        orientacion.plan = plan
        orientacion.materia = materia
        db.session.add(orientacion)
        db.session.commit()

        self.assertIsNotNone(orientacion.id)
        self.assertEqual(orientacion.nombre, "Orientacion A")
        self.assertEqual(orientacion.observacion, "Observacion de prueba")
        self.assertEqual(orientacion.especialidad.nombre, "Especialidad A")
        self.assertEqual(orientacion.plan.nombre, "Plan A")
        self.assertEqual(orientacion.materia.nombre, "Materia A")