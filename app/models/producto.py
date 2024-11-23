from app.models.db import db
from app.models.ingrediente import Ingrediente

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    ingrediente1_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable=False)
    ingrediente2_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable=False)
    ingrediente3_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable=False)
    ingrediente1 = db.relationship('Ingrediente', foreign_keys=[ingrediente1_id])
    ingrediente2 = db.relationship('Ingrediente', foreign_keys=[ingrediente2_id])
    ingrediente3 = db.relationship('Ingrediente', foreign_keys=[ingrediente3_id])
