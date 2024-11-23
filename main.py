from flask import Flask, render_template, redirect, url_for, flash
from app.models.db import db
from app.models.producto import Producto
from app.controllers.heladeria import Heladeria

app = Flask(__name__, template_folder='app/views')
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Cu4r3nt4@localhost/heladeria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

@app.route('/vender/<int:producto_id>')
def vender(producto_id):
    heladeria = Heladeria()
    resultado = heladeria.vender(producto_id)
    
    flash(resultado)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
