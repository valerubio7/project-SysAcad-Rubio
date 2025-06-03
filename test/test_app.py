import unittest
from flask import current_app
from app import create_app
import os

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_create_config(self):
        # CREATE: Verifica que se puede crear una configuración personalizada
        self.app.config['CUSTOM_KEY'] = 'custom_value'
        self.assertEqual(self.app.config['CUSTOM_KEY'], 'custom_value')

    def test_read_config(self):
        # READ: Verifica que se puede leer una configuración existente
        self.assertEqual(self.app.config['TESTING'], True)  # En modo test, debe ser True

    def test_update_config(self):
        # UPDATE: Verifica que se puede actualizar una configuración
        self.app.config['CUSTOM_KEY'] = 'initial_value'
        self.app.config['CUSTOM_KEY'] = 'updated_value'
        self.assertEqual(self.app.config['CUSTOM_KEY'], 'updated_value')

    def test_delete_config(self):
        # DELETE: Verifica que se puede eliminar una configuración
        self.app.config['CUSTOM_KEY'] = 'to_delete'
        del self.app.config['CUSTOM_KEY']
        self.assertNotIn('CUSTOM_KEY', self.app.config)

if __name__ == '__main__':
    unittest.main()
