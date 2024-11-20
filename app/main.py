from flask import Flask, render_template
from app.db import db, Producto, Ingrediente
from app.controlador import Controlador
import sys
import os

# Agregar la carpeta raíz del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Inicializar Flask
app = Flask(__name__, template_folder='views')

# Configurar conexión a MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Cu4r3nt4@localhost/heladeria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

with app.app_context():
    # Crear productos
    helado_chocolate = Producto(nombre="Helado de Chocolate", precio=5.0)
    helado_vainilla = Producto(nombre="Helado de Vainilla", precio=4.5)

    # Crear ingredientes
    cacao = Ingrediente(nombre="Cacao", producto=helado_chocolate)
    leche = Ingrediente(nombre="Leche", producto=helado_vainilla)

    # Guardar en la base de datos
    db.session.add_all([helado_chocolate, helado_vainilla, cacao, leche])
    db.session.commit()


controlador = Controlador()

@app.route('/')
def index():
    menu = controlador.obtener_menu()
    return render_template('index.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
