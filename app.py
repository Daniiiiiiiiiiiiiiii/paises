from flask import Flask, render_template, flash, request, Response, jsonify, redirect, url_for
from database import app, db, PaisSchema
from paises import Pais

pais_schema = PaisSchema()
pais_schema = PaisSchema(many=True)

app.app_context().push()
db.create_all()

@app.route('/')
def home():
    pais = Pais.query.all()
    paisesLeidos = pais_schema.dump(pais)
    
    return render_template('index.html', jugador = paisesLeidos)

#Method Post
@app.route('/paises', methods=['POST'])
def addPais():
    nombre = request.form['nombre']
    capital = request.form['capital']
    bandera = request.form['bandera']
    #falta el blob
    habitantes = request.form['habitantes']
    diaNacional = request.form['diaNacional']

    if nombre and capital and bandera and habitantes and diaNacional:
        nuevo_pais = Pais(nombre, capital, bandera, habitantes, diaNacional)
        db.session.add(nuevo_pais)
        db.session.commit()
        response = jsonify({
            'nombre' : nombre,
            'capital' : capital,
            'bandera' : bandera,
            'habitantes' : habitantes,
            'diaNacional' : diaNacional,
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
    #falta el blob
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