from flask import Flask, request, render_template, session,send_file
import os
import pandas as pd
import matplotlib.pyplot as plt
import tempfile
import base64
import io
from werkzeug.utils import secure_filename
import procesamiento as pp
from io import BytesIO
from pydataxm import *
import requests
import datetime as dt

# Crear una instancia de Flask
app = Flask(__name__)

# Definir el directorio de carga
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}  # Solo permitir archivos CSV

# Lista de regiones
regiones = [
    'ANTIOQUIA', 'BOGOTA - CUNDINAMARCA',
    'BOYACA', 'CALI - YUMBO - PUERTO TEJADA',
    'CARIBE MAR', 'CARIBE SOL', 'META',
    'NORTE DE SANTANDER', 'SANTANDER',
    'VALLE DEL CAUCA'
]

# Función para verificar que el archivo es del tipo correcto
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'csv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para cargar CSV
@app.route('/cargar', methods=['POST'])
def cargar_csv():
    return redirect(url_for('index'))

# Página de predicción
@app.route('/modelo', methods=['GET'])
def detalle_modelo():
    region = request.args.get('region', 'Región no especificada')

    return render_template('predecir.html', region=region)

# Ruta para predecir
@app.route('/predecir', methods=['POST'])
def predecir():
    region = request.args.get('region', 'Región no especificada')

    file = request.files['file']

    if file and allowed_file(file.filename):
        # Guardar el archivo en el servidor
        filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(filename)

        # Leer el archivo CSV usando pandas
        df = pd.read_csv(filename)

        # Cargar el modelo
        path_modelo = f'models/{region}.h5'
        modelo = pp.cargar_modelo(path_modelo)

        # Procesar el CSV
        df = pp.procesar_csv(filename, region)

        # Predecir
        predicciones, fechas = pp.predecir_consumo(df, modelo)

        # Guardar las predicciones y fechas en la sesión
        session['predicciones'] = predicciones.tolist()
        session['fechas'] = fechas

        predicciones_combinadas = []

        for i in range(len(fechas)):
            for fecha, pred in zip(fechas[i], predicciones[i]):
                predicciones_combinadas.append((str(fecha.date()), float(pred)))

        # Guardar en la sesión
        session['predicciones_combinadas'] = predicciones_combinadas

    return render_template('resultado.html', region=region)

# Ruta para predecir usandolos ultimos días de xm
@app.route('/predecirXM', methods=['POST'])
def predecirxm():
    region = request.args.get('region', 'Región no especificada')

    objetoAPI = pydataxm.ReadDB()

    df_demanda_xm = objetoAPI.request_data(
        "DemaComeNoReg",
        "CIIU",
        (dt.datetime.now() - dt.timedelta(days=60)).date(),  # Convierte a datetime y luego a date
        (dt.datetime.now() - dt.timedelta(days=1)).date(),  # Convierte a datetime y luego a date
    )

    df = pd.DataFrame(df_demanda_xm)

    # Cargar el modelo
    path_modelo = f'models/{region}.h5'
    modelo = pp.cargar_modelo(path_modelo)

    # Procesar el CSV
    df = pp.procesar_dataframe(df, region)

    # Predecir
    predicciones, fechas = pp.predecir_consumo(df, modelo)

    # Guardar las predicciones y fechas en la sesión
    session['predicciones'] = predicciones.tolist()
    session['fechas'] = fechas

    predicciones_combinadas = []

    for i in range(len(fechas)):
        for fecha, pred in zip(fechas[i], predicciones[i]):
            predicciones_combinadas.append((str(fecha.date()), float(pred)))

    # Guardar en la sesión
    session['predicciones_combinadas'] = predicciones_combinadas

    return render_template('resultado.html', region=region)

# Ruta para descargar las predicciones en un archivo CSV
@app.route('/descargar_excel')
def descargar_excel():
    predicciones = session.get('predicciones', [])
    fechas = session.get('fechas', [])

    if not predicciones or not fechas:
        return "No hay predicciones o fechas para descargar.", 400

    # Convertir las listas de listas en un DataFrame
    data = []

    # Recorrer las listas de fechas y predicciones
    for i in range(len(fechas)):
        # Emparejar las fechas con las predicciones correspondientes
        for fecha, pred in zip(fechas[i], predicciones[i]):
            data.append({
                'Fecha': fecha,
                'Predicción': pred
            })

    # Crear el DataFrame
    df = pd.DataFrame(data)

    df['Fecha'] = df['Fecha'].dt.tz_localize(None).dt.date

    # Crear el archivo Excel en memoria
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Predicciones')

    output.seek(0)

    # Usar send_file con el archivo en formato binario
    return send_file(output, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', as_attachment=True, download_name='predicciones.xlsx')

if __name__ == '__main__':
    # Asegurarse de que la carpeta de uploads exista
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
