from flask import Flask, request, render_template, redirect, url_for, session
import pandas as pd
import joblib
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Cargar modelo entrenado
modelo = joblib.load('models/modelo_svm.joblib')  # Ruta a tu modelo

# Lista de regiones (ajustar según tu caso)
# Lista de regiones proporcionadas
regiones = [
    'ANTIOQUIA', 'ARAUCA', 'BAJO PUTUMAYO', 'BOGOTA - CUNDINAMARCA',
    'BOYACA', 'CALDAS', 'CALI - YUMBO - PUERTO TEJADA', 'CAQUETA',
    'CARIBE MAR', 'CARIBE SOL', 'CARTAGO', 'CASANARE', 'CAUCA',
    'CHOCO', 'GUAVIARE', 'HUILA', 'META', 'NARIÑO',
    'NORTE DE SANTANDER', 'PEREIRA', 'POPAYAN - PURACE', 'PUTUMAYO',
    'QUINDIO', 'RUITOQUE', 'SANTANDER', 'TOLIMA', 'TULUA',
    'VALLE DEL CAUCA', 'VALLE DEL SIBUNDOY', 'SIN CLASIFICAR'
]
  # 30 regiones, una por cada salida de la red

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

        # Leer el CSV y procesar
        df = pd.read_csv(csv_path)
        # Transformar datos y realizar predicción
        # Ajustar según las transformaciones realizadas en el entrenamiento
        predicciones = modelo.predict(df)  # `df` debe tener las columnas necesarias
        prediccion_region = predicciones[int(region.split()[-1]) - 1]  # Selección según índice

        return render_template('resultado.html', region=region, prediccion=prediccion_region)

    return render_template('predecir.html', regiones=regiones, mensaje_carga=mensaje_carga)

if __name__ == '__main__':
    # Asegurarse de que la carpeta de uploads exista
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
