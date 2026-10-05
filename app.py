def inicio():
    return render_template('suma.html') # O la plantilla que desees usar de inicio
from flask import Flask, render_template, request

app = Flask(__name__)

# --- RUTA PARA LA SUMA ---
@app.route('/suma', methods=['GET', 'POST'])
def suma():
    resultado = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        resultado = numero1 + numero2
    return render_template('suma.html', resultado=resultado)

# --- RUTA PARA LA RESTA ---
@app.route('/resta', methods=['GET', 'POST'])
def resta():
    resultado = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        resultado = numero1 - numero2
    return render_template('resta.html', resultado=resultado)

# --- RUTA PARA LA MULTIPLICACIÓN ---
@app.route('/multiplicacion', methods=['GET', 'POST'])
def multiplicacion():
    resultado = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        resultado = numero1 * numero2
    return render_template('multiplicacion.html', resultado=resultado)

# --- RUTA PARA LA DIVISIÓN ---
@app.route('/division', methods=['GET', 'POST'])
def division():
    resultado = None
    error = None
    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        
        if numero2 == 0:
            error = 'No es posible dividir entre cero.'
        else:
            resultado = numero1 / numero2
            
    return render_template(
        'division.html', 
        resultado=resultado, 
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)

