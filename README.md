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

## Contexto del Sector Eléctrico Colombiano
El sector eléctrico colombiano está regulado principalmente por las Leyes 142 y 143 de 1994, que establecen el régimen de prestación de servicios públicos desde la generación hasta la comercialización de energía eléctrica. También definen las funciones y la estructura de gobernanza de las entidades clave del sector, tales como:

- **Ministerio de Minas y Energía (MinEnergía)**: Formula políticas y regula el sector.
- **Unidad de Planeación Minero Energética (UPME)**: Responsable de la planificación y proyección de la oferta y demanda energética.
- **Comisión de Regulación de Energía y Gas (CREG)**: Regula tarifas y condiciones de acceso al sistema.
- **Operador del Sistema (XM)**: Encargado de la operación y gestión del mercado mayorista.
- **Empresas de Servicios Públicos**: Realizan la generación, transmisión, distribución y comercialización de energía.

Esta estructura busca garantizar un suministro eficiente, promover la competencia y asegurar el acceso universal a servicios de energía. La recolección y monitoreo de datos en tiempo real, facilitados por XM y expertos del mercado, son esenciales para la predicción precisa de la demanda energética a nivel nacional.

## Librerías
Este proyecto utiliza las siguientes librerías para análisis y visualización de datos:

- **pandas**: Para la manipulación y análisis de datos.
- **seaborn**: Para la creación de gráficos estadísticos.
- **matplotlib**: Para visualización de gráficos.
- **API XM**: Para la consulta de datos de generación y demanda en tiempo real.

## Instrucciones de Ejecución

1. Instalar la API de XM si no se tiene, ejecutar el comando !pip install pydataxm.
2. Ejecución del archivo "LimpiezaYEntendimiento 1.ipynb"

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
