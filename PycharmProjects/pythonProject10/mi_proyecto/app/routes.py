from flask import render_template, request
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/procesar1', methods=['POST'])
def procesar_ejercicio1():
    notas = [int(request.form['nota1']), int(request.form['nota2']), int(request.form['nota3'])]
    asistencia = int(request.form['asistencia'])
    promedio = sum(notas) / len(notas)
    estado = 'Aprobado' if (promedio >= 40 and asistencia >= 75) else 'Reprobado'
    return render_template('resultado_ejercicio1.html', promedio=promedio, estado=estado)

@app.route('/procesar2', methods=['POST'])
def procesar_ejercicio2():
    nombres = [request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]
    nombre_largo = max(nombres, key=len)
    longitud = len(nombre_largo)
    return render_template('resultado_ejercicio2.html', nombre_largo=nombre_largo, longitud=longitud)
