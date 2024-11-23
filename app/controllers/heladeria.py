from app.models.db import db
from app.models.producto import Producto

class Heladeria:
    def __init__(self):
        self.productos = Producto.query.all()

    def vender(self, producto_id):
        producto = Producto.query.get(producto_id)
        if not producto:
            return "Producto no encontrado en la base de datos."
        
        if not self.verificar_inventario_ingredientes(producto):
            return f"No hay suficiente inventario de ingredientes para {producto.nombre}."
        self.descontar_ingredientes(producto)
        return f"Producto {producto.nombre} vendido con éxito."
    
    def verificar_inventario_ingredientes(self, producto):
        ingredientes = [producto.ingrediente1, producto.ingrediente2, producto.ingrediente3]
        for ingrediente in ingredientes:
            if ingrediente.cantidad <= 0:
                return False
        return True
    
    def descontar_ingredientes(self, producto):
        ingredientes = [producto.ingrediente1, producto.ingrediente2, producto.ingrediente3]
        for ingrediente in ingredientes:
            ingrediente.cantidad -= 1
        db.session.commit()
