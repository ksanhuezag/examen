from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Asumiendo que tu formulario envía 'nombre', 'edad' y 'cantidad_tarros'
        nombre = request.form.get('nombre', '')
        edad = int(request.form.get('edad', 0))
        cantidad_tarros = int(request.form.get('cantidad_tarros', 0))
        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro
        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = 0.15
        else:
            descuento = 0.25
        total_con_descuento = total_sin_descuento * (1 - descuento)
        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento)
    # Si no es POST, es GET, así que solo muestra la página inicial de ejercicio 1
    return render_template('ejercicio1.html', nombre=None, total_sin_descuento=0, total_con_descuento=0)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    if request.method == 'POST':
        usuario = request.form.get('usuario', '')
        password = request.form.get('password', '')
        if usuario == "juan" and password == "admin":
            mensaje = "Bienvenido administrador Juan."
        elif usuario == "pepe" and password == "user":
            mensaje = "Bienvenido usuario Pepe."
        else:
            mensaje = "Datos incorrectos, intenta nuevamente."
    # Si no es POST, es GET, así que solo muestra la página inicial de ejercicio 2
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
