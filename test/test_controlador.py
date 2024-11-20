import unittest
from app.controlador import Controlador

class TestControlador(unittest.TestCase):
    def test_obtener_menu(self):
        controlador = Controlador()
        menu = controlador.obtener_menu()
        self.assertIsNotNone(menu)
        self.assertIsInstance(menu, list)
