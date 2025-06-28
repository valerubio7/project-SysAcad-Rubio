import unittest
import os
from app import create_app, db

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

    def test_health_endpoint(self):
        response = self.client.get('/health')
        self.assertIn(response.status_code, [200, 404])  # Cambia según tu API

    # Agrega aquí más tests para tus recursos/endpoints

if __name__ == '__main__':
    unittest.main()
    