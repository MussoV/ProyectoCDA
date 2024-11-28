from flask import Flask, request, render_template, redirect, url_for, session
import pandas as pd
import os
import procesamiento as pp

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Lista de regiones
regiones = [
    'ANTIOQUIA', 'ARAUCA', 'BAJO PUTUMAYO', 'BOGOTA - CUNDINAMARCA',
    'BOYACA', 'CALDAS', 'CALI - YUMBO - PUERTO TEJADA', 'CAQUETA',
    'CARIBE MAR', 'CARIBE SOL', 'CARTAGO', 'CASANARE', 'CAUCA',
    'CHOCO', 'GUAVIARE', 'HUILA', 'META', 'NARIÑO',
    'NORTE DE SANTANDER', 'PEREIRA', 'POPAYAN - PURACE', 'PUTUMAYO',
    'QUINDIO', 'RUITOQUE', 'SANTANDER', 'TOLIMA', 'TULUA',
    'VALLE DEL CAUCA', 'VALLE DEL SIBUNDOY', 'SIN CLASIFICAR'
]

# Regiones que usan el modelo alternativo
regiones_LNRS = ['ANTIOQUIA', 'ARAUCA']

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para cargar CSV
@app.route('/cargar', methods=['POST'])
def cargar_csv():
    if 'file' not in request.files:
        session['csv_cargado'] = False
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        session['csv_cargado'] = False
        return redirect(url_for('index'))

    # Guardar el archivo
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    session['csv_path'] = file_path
    session['csv_cargado'] = True
    return redirect(url_for('index'))

# Página de predicción
@app.route('/predecir', methods=['GET', 'POST'])
def predecir():
    mensaje_carga = "Archivo CSV cargado correctamente." if session.get('csv_cargado') else "No se ha cargado ningún archivo CSV."
    if request.method == 'POST':
        region = request.form.get('region')
        csv_path = session.get('csv_path')

        if not csv_path or not os.path.exists(csv_path):
            mensaje_carga = "No se ha cargado ningún archivo CSV válido."
            return render_template('predecir.html', regiones=regiones, mensaje_carga=mensaje_carga)

        # Preprocesar
        df = pp.procesar_csv(csv_path, region)

        # Seleccionar el modelo según la región
        if region in regiones_LNRS:
            modelo = pp.cargar_modelo('modelo_LNRS.pkl')  # Carga el modelo alternativo
        else:
            modelo = pp.cargar_modelo('modelo.pkl')  # Carga el modelo predeterminado

        # Predecir
        predicciones = pp.predecir_consumo(df, modelo)

        return render_template('resultado.html', region=region, prediccion=predicciones)

    return render_template('predecir.html', regiones=regiones, mensaje_carga=mensaje_carga)

if __name__ == '__main__':
    # Asegurarse de que la carpeta de uploads exista
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
