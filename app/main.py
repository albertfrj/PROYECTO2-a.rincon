from flask import Flask, render_template
from .db import db
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

# Instanciar el controlador
controlador = Controlador()

@app.route('/')
def index():
    menu = controlador.obtener_menu()
    return render_template('index.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
