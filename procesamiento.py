import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta
from keras.models import load_model
from keras.losses import MeanAbsoluteError

def obtener_festivos(anio):
    url = f"https://date.nager.at/api/v3/publicholidays/{anio}/CO"

    response = requests.get(url)
    if response.status_code == 200:
        festivos = response.json()
        # Extraer solo las fechas de los festivos
        return [festivo['date'] for festivo in festivos]
    else:
        print(f"Error al obtener festivos para el año {anio}, código de estado {response.status_code}")
        return []

def clasificar_dia(fecha, festivos_colombia):
    if fecha in festivos_colombia:
        return 1
    else:
        return 0


def procesar_fechas(df):

    #Obtener anios de las fechas
    anios = df['Date'].dt.year.unique()

    # Obtener festivos para cada año
    festivos = []
    for anio in anios:
        festivos += obtener_festivos(anio)

    #Convertir a formato de fecha
    festivos = [datetime.strptime(festivo, "%Y-%m-%d").date() for festivo in festivos]

    #Clasificar si es festivo o no
    df['Festivo'] = df['Date'].apply(lambda x: clasificar_dia(x.date(), festivos))

    #Agregar columnas de día de la semana
    df['Dia'] = df['Date'].apply(lambda x: x.weekday())

    return df

def crear_matriz_modelo(df):
    # Crear una lista para almacenar cada fila de la matriz final
    matriz_final = []

    fechas =[]

    # Iteramos sobre el DataFrame para extraer ventanas de 60 días
    for i in range(len(df) - 60 + 1):

        ventana = df.iloc[i:i+60]

        # Reorganizamos la ventana en una sola fila con sufijos para cada día
        fila = {}
        for j in range(60):
            fila[f'fe-{j+1}'] = ventana.iloc[j]['Festivo']
            fila[f'd-{j+1}'] = ventana.iloc[j]['Dia']
            fila[f't-{j+1}'] = ventana.iloc[j]['Total']

        # Obtener la última fecha de la ventana de 60 días
        ultima_fecha = ventana.iloc[-1]['Date']

        # Crear las fechas de los siguientes 30 días
        fechas_30_dias = pd.date_range(start=ultima_fecha, periods=30, freq='D')

        # Guardar las fechas
        fechas.append(fechas_30_dias.tolist())

        #procesar las fechas
        fechas_30_dias = procesar_fechas(pd.DataFrame({'Date': fechas_30_dias}))


        # Añadir las columnas de festivo y día de la semana
        for j in range(30):
            fila[f'fe+{j+1}'] = fechas_30_dias.iloc[j]['Festivo']
            fila[f'd+{j+1}'] = fechas_30_dias.iloc[j]['Dia']

        # Añadimos la fila al conjunto de la matriz final
        matriz_final.append(fila)

    # Convertimos la lista de filas en un DataFrame final
    matriz_dias_df = pd.DataFrame(matriz_final)

    return matriz_dias_df, fechas


def procesar_csv(csv_path, region):

    #Definir las columnas de las horas
    horas = [f'Values_Hour{i:02d}' for i in range(1, 25)]

    #Leer el archivo CSV
    df = pd.read_csv(csv_path)

    #Filtrar por la región seleccionada
    df = df[df['Values_code'] == region]

    #Eliminar columnas innecesarias
    df = df.drop(columns=['Id', 'Values_code', 'Values_MarketType'])

    #Arreglar el formato de las fechas
    df['Date'] = pd.to_datetime(df['Date'])

    #Reemplazar los valores nulos por 0
    df = df.fillna(0)

    #Sumar las horas
    df['Total'] = df[horas].sum(axis=1)

    #Eliminar las columnas de las horas
    df = df.drop(columns=horas)

    #Agrupar por fecha
    df = df.groupby('Date').sum().reset_index()

    #Ordenar por fecha
    df = df.sort_values('Date').reset_index(drop=True)

    #Procesar las fechas
    df = procesar_fechas(df)

    return df

def procesar_dataframe(df, region):

    #Definir las columnas de las horas
    horas = [f'Values_Hour{i:02d}' for i in range(1, 25)]

    #Filtrar por la región seleccionada
    df = df[df['Values_code'] == region]

    #Eliminar columnas innecesarias
    df = df.drop(columns=['Id', 'Values_code', 'Values_MarketType'])

    #Arreglar el formato de las fechas
    df['Date'] = pd.to_datetime(df['Date'])

    #Reemplazar los valores nulos por 0
    df = df.fillna(0)

    #Sumar las horas
    df['Total'] = df[horas].sum(axis=1)

    #Eliminar las columnas de las horas
    df = df.drop(columns=horas)

    #Agrupar por fecha
    df = df.groupby('Date').sum().reset_index()

    #Ordenar por fecha
    df = df.sort_values('Date').reset_index(drop=True)

    #Procesar las fechas
    df = procesar_fechas(df)

    return df

def predecir_consumo(df, modelo):

    #Crear la matriz para el modelo
    matriz_dias_df, fechas = crear_matriz_modelo(df)

    #Realizar la predicción
    predicciones = modelo.predict(matriz_dias_df)

    return predicciones, fechas

def cargar_modelo(path_modelo):
    #Cargar el modelo
    modelCNN_loaded = load_model(path_modelo, custom_objects={'mae': MeanAbsoluteError()})

    return modelCNN_loaded






