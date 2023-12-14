from database import db
from sqlalchemy.sql import func
from datetime import date

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
    bandera_url = db.Column(db.String(100), nullable=False)
    # bandera_blob = db.Column(db.LargeBinary, nullable=False)
    bandera_blob = db.Column(db.BLOB)
    habitantes = db.Column(db.Integer, nullable=False)
    diaNacional = db.Column(db.Date, nullable=False)
    
     
    def __init__(self, nombre, capital, bandera_url, bandera_blob, habitantes, diaNacional):
        self.nombre = nombre
        self.capital = capital
        self.bandera_url = bandera_url
        self.bandera_blob = bandera_blob
        self.habitantes = habitantes
        self.diaNacional = diaNacional




    def __repr__(self):
        return f'<Pais {self.id}>: {self.nombre}, {self.capital}, {self.bandera_url}, {self.bandera_blob}, {self.habitantes}, {self.diaNacional}'