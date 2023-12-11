from database import db
from sqlalchemy.sql import func

# Para crear las tablas, desde el entorno de ejecución de Python, ejecutar:
# from database import app, db
# from estudiante import Estudiante
# app.app_context().push()
# db.create_all()

class Pais(db.Model):
    
    __tablename__ = 'paises'
#falta terminar esto     
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    capital = db.Column(db.String(100), nullable=False)
    bandera = db.Column(db.String(100), nullable=False)
    habitantes = db.Column(db.Integer, nullable=False)
    
     
    def __init__(self, nombre,edad, club):
        self.nombre = nombre
        self.edad = edad
        self.club = club

    def __repr__(self):
        return f'<Jugador {self.id}>: {self.nombre}, {self.club}'