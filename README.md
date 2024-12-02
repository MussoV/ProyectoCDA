# Pronóstico de Demanda Energética en Colombia

## Integrantes

1. Juliana Andrea Galeano Caicedo.
2. Juan Nicolás Estepa Guzmán.
3. Santiago Rodríguez Cruz.
4. Harvy José Benítez Amaya.

## Resumen

El Área de Gobierno y Monitoreo del Dato del Ministerio de Minas y Energía (MinEnergía), en colaboración con el Área de Gestión de la Información de la Unidad de Planeación Minero-Energética (UPME), enfrenta una problemática significativa: las limitaciones de los modelos actuales para realizar pronósticos precisos de demanda energética a corto plazo (1, 3 y 6 meses) desagregados a nivel regional. Estos modelos, al subestimar o sobreestimar la demanda, generan sobrecostos que afectan negativamente la planificación y operación del sistema energético colombiano. 

Existen claras oportunidades de mejora mediante el uso de Ciencia de Datos, que podría proporcionar pronósticos más precisos al incorporar variables exógenas y manejar eventos atípicos. Esto permitiría una gestión energética más eficiente y una reducción significativa en los costos de operación.

La estrategia del MinEnergía y UPME para pronosticar la demanda de energía incluye modelos estadísticos y econométricos que analizan datos históricos junto con factores económicos clave, como el PIB y la población. El modelo plantea diferentes escenarios de crecimiento, consultas con actores clave del sector y revisiones periódicas para ajustar los pronósticos a las cambiantes condiciones del país. Asimismo, incorpora tecnologías emergentes y realiza análisis regionales para mejorar la precisión de los pronósticos a nivel local.

## Tabla de contenidos

- [Contexto del Sector Eléctrico](#contexto-del-sector-eléctrico-colombiano)
- [Descripción de la Solución](#descripción-de-la-solución)
- [Requerimientos](#requerimientos)
- [Instrucciones de Ejecución](#instrucciones-de-ejecución)
- [Pruebas Automatizadas](#pruebas-automatizadas)
- [Conclusiones](#conclusiones)

## Contexto del Sector Eléctrico Colombiano

El sector eléctrico colombiano está regulado principalmente por las Leyes 142 y 143 de 1994, que establecen el régimen de prestación de servicios públicos desde la generación hasta la comercialización de energía eléctrica. También definen las funciones y la estructura de gobernanza de las entidades clave del sector, tales como:

- **Ministerio de Minas y Energía (MinEnergía)**: Formula políticas y regula el sector.
- **Unidad de Planeación Minero Energética (UPME)**: Responsable de la planificación y proyección de la oferta y demanda energética.
- **Comisión de Regulación de Energía y Gas (CREG)**: Regula tarifas y condiciones de acceso al sistema.
- **Operador del Sistema (XM)**: Encargado de la operación y gestión del mercado mayorista.
- **Empresas de Servicios Públicos**: Realizan la generación, transmisión, distribución y comercialización de energía.

Esta estructura busca garantizar un suministro eficiente, promover la competencia y asegurar el acceso universal a servicios de energía. La recolección y monitoreo de datos en tiempo real, facilitados por XM y expertos del mercado, son esenciales para la predicción precisa de la demanda energética a nivel nacional.

## Descripción de la Solución

Desarrollar un modelo de Red Neuronal Recurrente (RNN), que sea consumido mediante una API por XM, que utilice datos históricos y variables exógenas para predecir la demanda de energía a corto y mediano plazo en Colombia, mejorando la precisión de los pronósticos.

Se realizó la búsqueda de tres diferentes modelos, (**MLP, CNN y LSTM**), donde se plantea la búsqueda del mejor modelo para cada una de las regiones existentes dentro de la información brindada por la API de XM. Estos modelos encontrados se cargan a una aplicación donde a partir de entregar la información de **60 días en el pasado**, se entrega la predicción para **30 días en el futuro** con la posibilidad de escoger la región deseada a realizar la predicción.

Este resultado de la predicción se puede visualizar directamente en la aplicación, o se puede descargar un archivo con extensión .xlsx donde se entrega la fecha y el valor en **Gwh** para poder ser utilizada a futuro por quien lo desee.

## Requerimientos
El archivo `requirements.txt` especifica las librerías necesarias para ejecutar el proyecto. Este archivo se encuentra ubicado en la siguiente ruta:

requirements.txt

Para instalar los requerimientos, utiliza el siguiente comando:

```bash
pip install -r src/requirements.txt
```
Asegúrate de tener instalada la versión adecuada de Python compatible con las librerías listadas en el archivo.

### Librerías Empleadas

- `absl-py==2.1.0`
- `aiohappyeyeballs==2.4.3`
- `aiohttp==3.11.8`
- `aiosignal==1.3.1`
- `astunparse==1.6.3`
- `async-timeout==5.0.1`
- `asyncio==3.4.3`
- `attrs==24.2.0`
- `blinker==1.9.0`
- `certifi==2024.8.30`
- `charset-normalizer==3.4.0`
- `click==8.1.7`
- `colorama==0.4.6`
- `contourpy==1.3.1`
- `cycler==0.12.1`
- `DateTime==5.5`
- `et_xmlfile==2.0.0`
- `Flask==3.1.0`
- `flatbuffers==24.3.25`
- `fonttools==4.55.0`
- `frozenlist==1.5.0`
- `gast==0.6.0`
- `google-pasta==0.2.0`
- `grpcio==1.68.0`
- `h5py==3.12.1`
- `idna==3.10`
- `itsdangerous==2.2.0`
- `Jinja2==3.1.4`
- `keras==3.7.0`
- `keras-tunner==1.4.7`
- `kiwisolver==1.4.7`
- `libclang==18.1.1`
- `Markdown==3.7`
- `markdown-it-py==3.0.0`
- `MarkupSafe==3.0.2`
- `matplotlib==3.9.2`
- `mdurl==0.1.2`
- `ml-dtypes==0.4.1`
- `multidict==6.1.0`
- `namex==0.0.8`
- `nest-asyncio==1.6.0`
- `numpy==2.0.2`
- `openpyxl==3.1.5`
- `opt_einsum==3.4.0`
- `optree==0.13.1`
- `packaging==24.2`
- `pandas==2.2.3`
- `pillow==11.0.0`
- `propcache==0.2.0`
- `protobuf==5.28.3`
- `pydataxm==0.3.10`
- `Pygments==2.18.0`
- `pyparsing==3.2.0`
- `python-dateutil==2.9.0.post0`
- `pytz==2024.2`
- `requests==2.32.3`
- `rich==13.9.4`
- `six==1.16.0`
- `tensorboard==2.18.0`
- `tensorboard-data-server==0.7.2`
- `tensorflow==2.18.0`
- `tensorflow-io-gcs-filesystem==0.31.0`
- `tensorflow_intel==2.18.0`
- `termcolor==2.5.0`
- `typing_extensions==4.12.2`
- `tzdata==2024.2`
- `urllib3==2.2.3`
- `Werkzeug==3.1.3`
- `wrapt==1.17.0`
- `yarl==1.18.0`
- `zope.interface==7.2`

### Requerimientos Software

Python 3.10.11 o superior

## Instrucciones de Ejecución

1. Instalar las librerías del archivo "requirements.txt"
2. Ejecución del archivo "LimpiezaYEntendimiento.ipynb"
3. Ejecución del archivo "Modelos.ipynb" para generar cada uno de los mejores modelos y su información a consumir en la aplicación.
4. Ejecutar el archivo "main.py"
5. Abrir el entorno local con la ruta 127.0.0.1:5000 en cualquier navegador. (El puerto puede cambiar si al momento de su ejecución esta ocupado)
6. Seleccionar alguna región para utilizar su modelo.
7. Agregar un archivo en formato .csv con la información de 60 días previos al periodo de tiempo de un mes que se desea estimar. (En la carpeta uploads se encuentra un archivo de ejemplo para utilizar con cualquier modelo)

**Nota:** La ejecución de los modelos del paso **3** se puede demorar dado que son 87 en total por los tres tipos de modelos a calcular para conocer el mejor. Se recomienda omitir este paso para una revisión rápida. Si se desea ejecutar una prueba del calculo del mejor modelo de una región en específico, dirigirse a la sección [Pruebas Automatizadas](#pruebas-automatizadas) para realizarlo.

## Pruebas Automatizadas



## Conclusiones

1. Las regiones con mayor consumo medio de energía son Bogotá y Cundinamarca, con aproximadamente 21.9 millones de kWh, seguidas de Antioquia con 14.7 millones de kWh.
2. Otras regiones con consumo notable incluyen el Caribe Mar y el Caribe Sol, ambos superando los 13 millones de kWh.
3. Las regiones de Bajo Putumayo y Popayán - Puracé presentan los consumos medios más bajos, con menos de 100,000 kWh.
4. La variabilidad en el consumo de energía es considerable, siendo Bogotá y Cundinamarca las que muestran la mayor desviación estándar, lo que indica una fluctuación significativa en su demanda. En contraste, regiones como Chocó y Guaviare presentan un consumo más estable, con desviaciones estándar menores.
5. Las regiones sin clasificar tienen un consumo significativamente bajo, sugiriendo que los datos de estas áreas pueden no estar completamente representados o que la actividad económica es mínima.
6. Los sectores con mayor consumo de energía son predominantemente industriales, como las industrias manufactureras y la explotación de minas y canteras.
7. Sectores como el comercio al por mayor y al por menor, así como el transporte y almacenamiento, presentan un consumo energético moderado.
8. Las actividades artísticas y otras actividades de bajo impacto muestran un consumo de energía significativamente menor.
9. Los sectores con altos niveles de consumo de energía también presentan una gran variabilidad, indicando diferencias significativas en las prácticas operativas.
10. Los días “No Festivos” muestran una demanda más alta y variabilidad en comparación con los días “Festivos y Domingos”.
11. Los “Domingos y Festivos” tienen demandas promedio similares, lo que sugiere un patrón de consumo similar en esos días.
12. Es recomendable considerar la variabilidad en la demanda, especialmente en días “No Festivos”, para el análisis y la planificación futura de la oferta de energía. 
