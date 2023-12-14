from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
usuario = os.environ.get("MYSQLDB_USUARIO")
password = os.environ.get("MYSQLDB_PASSWORD")
host = os.environ.get("MYSQLDB_HOST")
bd = os.environ.get("MYSQLDB_BD")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{usuario}:{password}@{host}/{bd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hardsecretkey'  # Para las sesiones flash

db = SQLAlchemy(app)
ma = Marshmallow(app)

class PaisSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'capital', 'bandera', 'habitantes', 'diaNacional')