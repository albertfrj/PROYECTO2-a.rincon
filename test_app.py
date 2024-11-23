import unittest
from app import app
from app.models.db import db
from app.models.producto import Producto
from app.models.ingrediente import Ingrediente

class TestHeladeria(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuración inicial para las pruebas."""
        cls.app = app
        cls.client = cls.app.test_client()
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        with cls.app.app_context():
            db.create_all()

    def setUp(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.create_all()
            ingrediente1 = Ingrediente(nombre="Chocolate", cantidad=10)
            ingrediente2 = Ingrediente(nombre="Vainilla", cantidad=10)
            ingrediente3 = Ingrediente(nombre="Fresa", cantidad=10)
            db.session.add(ingrediente1)
            db.session.add(ingrediente2)
            db.session.add(ingrediente3)
            db.session.commit()
            producto = Producto(
                nombre="Helado de Chocolate",
                precio=5.0,
                ingrediente1=ingrediente1,
                ingrediente2=ingrediente2,
                ingrediente3=ingrediente3
            )
            db.session.add(producto)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_vender_producto_con_inventario_suficiente(self):
        with self.app.app_context():
            producto = Producto.query.first() 

            response = self.client.post(f'/vender/{producto.id}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Producto vendido', response.data)
            self.assertEqual(Ingrediente.query.get(producto.ingrediente1.id).cantidad, 9)
            self.assertEqual(Ingrediente.query.get(producto.ingrediente2.id).cantidad, 9)
            self.assertEqual(Ingrediente.query.get(producto.ingrediente3.id).cantidad, 9)

    def test_vender_producto_sin_inventario(self):
        """Prueba para vender un producto cuando no hay suficiente inventario de ingredientes."""
        with self.app.app_context():
            producto = Producto.query.first()

   
            ingrediente1 = Ingrediente.query.get(producto.ingrediente1.id)
            ingrediente1.cantidad = 0 
            db.session.commit()

            response = self.client.post(f'/vender/{producto.id}')
            

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'No hay suficiente inventario de ingredientes', response.data)

    def test_producto_no_existente(self):

        response = self.client.post('/vender/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Producto no encontrado en la base de datos.', response.data)

if __name__ == '__main__':
    unittest.main()
