import unittest
import os
from app import create_app, db
from flask import current_app
from app.mapping import UniversidadMapping
from app.models.universidad import Universidad

# Función auxiliar para crear una universidad de prueba

def nuevauniversidad():
    universidad = Universidad()
    universidad.nombre = "Universidad Nacional"
    universidad.sigla = "UN"
    db.session.add(universidad)
    db.session.commit()
    return universidad

class AppResourcesTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        self.app_context.pop()
    def test_obtener_por_id(self):
        universidad = nuevauniversidad()
        universidad_mapping = UniversidadMapping()
        response = self.client.get(f'/api/v1/universidades/{universidad.id}')
        universidad_obtenida = universidad_mapping.load(response.get_json())
        self.assertEqual(universidad_obtenida.id, universidad.id)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.get_json())

    def test_obtener_todos(self):
        universidad1 = nuevauniversidad()
        universidad2 = nuevauniversidad()
        universidad_mapping = UniversidadMapping()
        response = self.client.get('/api/v1/universidades')
        universidades = universidad_mapping.load(response.get_json(), many=True)
        self.assertGreaterEqual(len(universidades), 2)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.get_json())
