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

    def test_plan_create(self):
        plan = Plan(nombre="Plan CRUD", fecha_inicio=date(2025, 1, 1), fecha_fin=date(2025, 12, 31), observacion="Test create")
        db.session.add(plan)
        db.session.commit()
        self.assertIsNotNone(plan.id)

    def test_plan_read(self):
        plan = Plan(nombre="Plan Read", fecha_inicio=date(2026, 1, 1), fecha_fin=date(2026, 12, 31), observacion="Test read")
        db.session.add(plan)
        db.session.commit()
        found = Plan.query.filter_by(nombre="Plan Read").first()
        self.assertIsNotNone(found)
        self.assertEqual(found.observacion, "Test read")

    def test_plan_update(self):
        plan = Plan(nombre="Plan Update", fecha_inicio=date(2027, 1, 1), fecha_fin=date(2027, 12, 31), observacion="Test update")
        db.session.add(plan)
        db.session.commit()
        plan.observacion = "Updated"
        db.session.commit()
        updated = db.session.get(Plan, plan.id)
        self.assertEqual(updated.observacion, "Updated")

    def test_plan_delete(self):
        plan = Plan(nombre="Plan Delete", fecha_inicio=date(2028, 1, 1), fecha_fin=date(2028, 12, 31), observacion="Test delete")
        db.session.add(plan)
        db.session.commit()
        db.session.delete(plan)
        db.session.commit()
        deleted = db.session.get(Plan, plan.id)
        self.assertIsNone(deleted)