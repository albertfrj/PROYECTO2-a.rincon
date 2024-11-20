class Controlador:
    def __init__(self):
        self.heladeria = None  # Aquí conectaremos con el modelo más adelante
    
    def cargar_heladeria(self, heladeria):
        self.heladeria = heladeria

    def obtener_menu(self):
        return self.heladeria.obtener_menu() if self.heladeria else []
