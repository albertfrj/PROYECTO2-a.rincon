from app.db import Producto

class Controlador:
    def obtener_menu(self):
        return Producto.query.all()
