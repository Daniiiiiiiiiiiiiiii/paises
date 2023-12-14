from flask import Flask, render_template, flash, request, Response, jsonify, redirect, url_for
from database import app, db, PaisSchema
from paises import Pais
from werkzeug.utils import secure_filename
from random import sample
import os

pais_schema = PaisSchema()
pais_schema = PaisSchema(many=True)

app.app_context().push()
db.create_all()

@app.route('/')
def home():
    pais = Pais.query.all()
    paisesLeidos = pais_schema.dump(pais)
    
    return render_template('index.html', pais = paisesLeidos)

#Method Post
@app.route('/paises', methods=['POST'])
def addPais():
    if request.method == 'POST':
        nombre = request.form['nombre']
        capital = request.form['capital']
        bandera_blob = request.files['bandera']
        habitantes = request.form['habitantes']
        diaNacional = request.form['diaNacional']

        # Script para archivo
        basepath = os.path.dirname(__file__)  # La ruta donde se encuentra el archivo actual
        filename = secure_filename(bandera_blob.filename)  # Nombre original del archivo

        # Capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
        extension = os.path.splitext(filename)[1]
        nuevoNombreFile = "BanderaDe" + nombre + extension

        upload_path = os.path.join(basepath, 'static/images', nuevoNombreFile)
        bandera_blob.save(upload_path)

        # Leer el contenido del archivo como bytes
        with open(upload_path, 'rb') as file:
            blob_data = file.read()

        bandera_url = "Bandera-de-" + nombre + extension

        if nombre and capital and bandera_url and blob_data and habitantes and diaNacional:
            nuevo_pais = Pais(
                nombre=nombre,
                capital=capital,
                bandera_url=bandera_url,
                bandera_blob=blob_data,  
                habitantes=habitantes,
                diaNacional=diaNacional
            )

            db.session.add(nuevo_pais)
            db.session.commit()

            response = jsonify({
                'nombre': nombre,
                'capital': capital,
                'bandera_url': "BanderaDe" + nombre + extension,
                'bandera_blob': nuevoNombreFile,
                'habitantes': habitantes,
                'diaNacional': diaNacional
            })

            return redirect(url_for('home'))
        else:
            return notFound()
#Method delete
@app.route('/delete/<id>')
def deletePais(id):
    pais = Pais.query.get(id)
    db.session.delete(pais)
    db.session.commit()
    
    flash('Pais ' + id + ' eliminado correctamente')
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<id>', methods=['POST'])
def editPais(id):    
    
    nombre = request.form['nombre']
    capital = request.form['capital']
    bandera = request.form['bandera']
    habitantes = request.form['habitantes']
    diaNacional = request.form['diaNacional']
    
    if nombre and capital and bandera and habitantes and diaNacional:
        pais = Pais.query.get(id)
  # return student_schema.jsonify(student)
        pais.nombre = nombre
        pais.capital = capital
        pais.bandera = bandera
        pais.habitantes = habitantes
        pais.diaNacional = diaNacional
        
        db.session.commit()
        
        response = jsonify({'message' : 'Pais ' + id + ' actualizado correctamente'})
        flash('Pais ' + id + ' modificado correctamente')
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response   
if __name__ == "__main__":
   app.run(debug=True)