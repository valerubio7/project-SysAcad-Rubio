import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.plan import Plan
from datetime import date


class PlanTestCase(unittest.TestCase):

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

    def test_plan_creation(self):
        plan = Plan()
        plan.nombre = "Plan A"
        plan.fecha_inicio = date(2023, 1, 1)  # Usar objetos de tipo date
        plan.fecha_fin = date(2023, 12, 31)  # Usar objetos de tipo date
        plan.observacion = "Observacion de prueba"

        db.session.add(plan)
        db.session.commit()

        self.assertIsNotNone(plan.id)
        self.assertEqual(plan.nombre, "Plan A")
        self.assertEqual(plan.fecha_inicio, date(2023, 1, 1))
        self.assertEqual(plan.fecha_fin, date(2023, 12, 31))
        self.assertEqual(plan.observacion, "Observacion de prueba")