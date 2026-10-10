# DataProject – Proyecto Final

## Análisis Exploratorio de Ventas (EDA)

Este proyecto presenta un análisis exploratorio de datos (EDA) sobre ventas realizadas entre 2015 y 2022, con el objetivo de analizar la evolución del negocio, identificar tendencias y evaluar el rendimiento comercial desde diferentes perspectivas.

---

## 1. Descripción del proyecto

El análisis estudia la evolución de las ventas utilizando variables demográficas, socioeconómicas, canales de venta, métodos de envío, productos, países, regiones y periodos temporales.

Los resultados permiten:

- Analizar la evolución de las ventas entre 2015 y 2022.
- Comparar el comportamiento comercial por país y región.
- Evaluar el rendimiento por canal de venta.
- Identificar perfiles de clientes y segmentos con mayor contribución.
- Detectar oportunidades de mejora en procesos operativos y comerciales.

---

## 2. Estructura del proyecto

```text
DataProject/
│
├── Datos_Raw/
│   ├── sales.csv
│   └── customers.xlsx
│
├── Data/
│   └── Processed/
│       └── df_unido.csv
│
├── Notebooks/
│   ├── ETL_Datos.ipynb
│   └── Analisis_Datos.ipynb
│
├── Datos_Processed/
│   └── Analisis_Datos.py
│
└── README.md
```

---

## 3. Datos de origen

Los datos utilizados proceden de:

- `sales.csv`
- `customers.xlsx`

---

## 4. Proceso ETL y limpieza de datos

Las principales tareas realizadas durante la transformación de datos fueron:

- Carga de ficheros mediante Pandas.
- Creación de los DataFrames `df_sales` y `df_customer`.
- Limpieza de valores duplicados, vacíos y nulos.
- Conversión y normalización de datos al español.
- Unión de tablas mediante `merge()` usando `Id_cliente`.
- Eliminación de columnas no relevantes.
- Normalización de importes, descuentos y cantidades.
- Conversión de fechas al formato `dd/mm/aaaa`.
- Sustitución de valores nulos mediante reglas de negocio y medianas.
- Normalización de género, nivel de ingresos, región y zona de envío.
- Creación de la variable `Antigüedad` a partir de `Fecha_registro`.
- Exportación del resultado final a CSV.

---

## 5. Dataset final

### Características generales

- Registros: **56.608**
- Columnas: **24**
- Periodo: **2015 - 2022**

### Variables principales

- Id_cliente
- Id_venta
- Fecha_venta
- Importe
- Producto
- Cantidad
- Descuento
- Canal
- Región
- Estado
- Zona_envio
- Metodo_envio
- Peso_paquete
- Rango_valor_pedido
- Coste_envio
- País
- Género
- Edad
- Nivel_ingresos
- Ciudad
- Antigüedad

---

## 6. Análisis estadístico

### Importe de venta

- Media: 503,41 €
- Mediana: 504,01 €

Distribución muy equilibrada sin valores extremos significativos.

### Cantidad de productos

- Media: 5,52 unidades
- Mediana: 6 unidades

Predominio de compras multiproducto.

### Descuentos

- Media: 3,06 €
- Mediana: 0 €

Los descuentos se utilizan de forma puntual y no forman parte de la estrategia habitual.

### Peso de paquetes

- Media: 8,13 kg
- Mediana: 7,50 kg

Distribución estable y homogénea.

### Coste de envío

- Media: 12,06 €
- Mediana: 10,75 €

Representa aproximadamente el 2,4% del importe medio de venta.

### Edad de clientes

- Media: 49,22 años
- Mediana: 49 años

Perfil predominante de clientes de mediana edad.

### Antigüedad de clientes

- Media: 7,80 años
- Mediana: 8 años

Elevado nivel de fidelización.

---

## 7. Dashboard en Power BI

### Página Dashboard

**KPIs principales**

- Clientes
- Pedidos
- Unidades vendidas
- Ventas
- Coste de envío
- Ingresos
- Margen

**Visualizaciones**

- Ventas por año
- Ventas por producto
- Cantidad de productos
- Pedidos por producto
- Ventas por país

### Página Análisis

- Distribución de pedidos por estado y año
- Ingresos por producto
- Ranking de cancelaciones
- Ingresos por ciudad
- Ratio costes/ventas por tienda
- Pedidos por rango de edad

### Página Detalles

Tabla dinámica configurable mediante filtros y selección de métricas.

---

## 8. Principales hallazgos

### Evolución temporal

- Mejor año: 2021
- Ventas: 3.319.767 €
- Unidades vendidas: 36.127

### Productos

- Producto líder: Dispositivo J
- Ingresos generados: 2.568.156 €
- Tasa de cancelación: 26,48%

### Canales y tiendas

- Canal líder: En Línea
- Tienda líder: Tienda 1
- Mejor ratio coste/venta: Tienda 4 (1,64%)

### Países y regiones

- EE. UU.: 46,53% de las ventas.
- Ciudad líder: Los Ángeles.
- Región líder: Oeste.

### Perfil de cliente

- Segmento con mayor volumen de compras: 46-55 años.
- Distribución equilibrada entre géneros e ingresos.

---

## 9. Resultados generales

### Indicadores globales

- Ventas: 25.872.236 €
- Pedidos completados: 12.950
- Tasa de finalización: 25,22%

### Ventas por región

| Región | Ventas |
|----------|------------|
| Oeste | 6,51 M€ |
| Este | 6,47 M€ |
| Norte | 6,45 M€ |
| Sur | 6,43 M€ |

La estructura comercial presenta una distribución equilibrada del negocio.

### Distribución por género

- Hombres: 51,5%
- Mujeres: 48,5%

### Distribución por ingresos

- Ingresos medios: 2,28 M€
- Ingresos altos: 2,07 M€
- Ingresos bajos: 1,96 M€

### Canales de venta

- M-Commerce: 1,65 M€
- Minorista: 1,64 M€
- En Línea: 1,62 M€
- En Tienda: 1,58 M€

---

## 10. Conclusiones

El negocio presenta una elevada estabilidad comercial, geográfica y demográfica. No existe dependencia significativa de una región, canal o producto concreto.

La principal oportunidad de mejora se encuentra en la optimización de la conversión de pedidos y la reducción de cancelaciones, ya que únicamente el 25,22% de los pedidos alcanzan el estado de completado.

La estrategia omnicanal, la diversificación de productos y la cobertura logística equilibrada reducen el riesgo operativo y proporcionan una base sólida para el crecimiento futuro.
