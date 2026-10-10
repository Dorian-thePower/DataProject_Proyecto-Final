import pandas as pd
import numpy as np
pd.set_option('display.max_columns',None)

# ===============================
# ANALISIS DE DATOS
# ===============================

#Cargo el csv y creo un DataFrame.
df_analisis = pd.read_csv("../Datos_Processed/df_unido.csv")
df_analisis.head()

# Reviso a modo de descripción los valores minimos, máximos, desv.estandar y percentiles de cada columna 
df_analisis.describe().T

# Reviso los estados de los pedidos, cantidad total de productos e importes

df = pd.DataFrame(df_analisis)

# Agrupar por estado
resultado = (
    df.groupby("Estado")
      .agg(
          unidades=("Cantidad", "sum"),
          importe_total=("Importe", "sum"),
          coste=("Coste_envio", "sum")
      )
      .reset_index()
      .rename(columns={"Estado": "estado_pedido"})
)

# Crear la columna beneficio
resultado["beneficio"] = resultado["importe_total"] - resultado["coste"]

# Crear la columna margen de beneficio en %

resultado["margen_%"] = (
    (resultado["beneficio"] / resultado["importe_total"]) * 100
).round(2)


print(resultado)

# =========================================
# 1. ANALISIS DE CANTIDAD DE VENTAS POR AÑO
# =========================================

# Se analizan las ventas de todos los productos en todos los estados por años

df_productos = df_analisis[df_analisis['Estado'].isin(['Completado', 'Enviado','Cancelado', 'Pendiente'])].copy()

# Compruebo que la fecha es de formato DataTime y extraigo el año

df_productos['Fecha_venta'] = pd.to_datetime(df_productos['Fecha_venta'], errors='coerce')
df_productos['Año'] = df_productos['Fecha_venta'].dt.year

# Agrupo por año para obtener ventas totales de productos y el importe total por año

df_ventas_por_año = (
    df_productos.groupby('Año')
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum'),
    )
    .reset_index()
)

total_cantidad = df_ventas_por_año['Cantidad_Total'].sum()

df_ventas_por_año['% del Total'] = (
    df_ventas_por_año['Cantidad_Total'] / total_cantidad * 100
).round(2)

df_ventas_por_año

# Creo un grafico de lineas para visualizar el progreso de productos vendidos por Año.

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

plt.plot(
    df_ventas_por_año['Año'],
    df_ventas_por_año['Cantidad_Total'],
    marker='o',
    linewidth=2,
    color='darkorange'
)

for x, y in zip(df_ventas_por_año['Año'], df_ventas_por_año['Cantidad_Total']):
    plt.text(
        x,
        y + 40,         
        f"{y:,}",
        ha='center',
        fontsize=9
    )

plt.title('Productos Vendidos por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad Total de Productos')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# Creo un grafico de lineas para visualizar el progreso de ventas por Año.

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.plot(
    df_ventas_por_año['Año'],
    df_ventas_por_año['Importe_Total'],
    marker='o',
    linewidth=2,
    color='steelblue'
)

for x, y in zip(df_ventas_por_año['Año'], df_ventas_por_año['Importe_Total']):
    plt.text(
        x,
        y + 45,         
        f"{y:,}",
        ha='center',
        fontsize=9
    )

plt.title('Ventas por Año')
plt.xlabel('Año')
plt.ylabel('Importe Total')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()

# Creo un grafico de lineas para visualizar el progreso de ventas y productos vendidos por Año.

import matplotlib.pyplot as plt


años = df_ventas_por_año['Año']
cantidades = df_ventas_por_año['Cantidad_Total']
importes = df_ventas_por_año['Importe_Total']


fig, ax1 = plt.subplots(figsize=(10,6))


color1 = 'steelblue'
ax1.set_xlabel('Año')
ax1.set_ylabel('Importe Total (€)', color=color1)
ax1.plot(años, importes, marker='o', linewidth=2, color=color1, label='Importe Total')
ax1.tick_params(axis='y', labelcolor=color1)


ax2 = ax1.twinx()  
color2 = 'darkorange'
ax2.set_ylabel('Cantidad Total de Productos', color=color2)
ax2.plot(años, cantidades, marker='s', linewidth=2, color=color2, label='Cantidad Total')
ax2.tick_params(axis='y', labelcolor=color2)


plt.title('Evolución de Ventas y Productos Vendidos por Año')
ax1.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

#======================================
# 2. ANALISIS POR TIPO DE PRODUCTOS
#=====================================

# Creo un DataFrame con los productos mas vendidos por año, junto con la cantidad total de unidades vendidas y el importe total de ventas.

df_ventas_por_año = (
    df_productos.groupby('Año')
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum'),
        Producto=('Producto', 'first')
    )
    
)

df_ventas_por_año = df_ventas_por_año.reset_index()

df_ventas_por_año

# Reviso cual ha sido el producto mas vendido en cada año

import pandas as pd
import matplotlib.pyplot as plt

# Cantidad vendida por producto y año
ventas_producto_año = (
    df_productos
    .groupby(['Año', 'Producto'])['Cantidad']
    .sum()
    .reset_index()
)

# Obtener el producto con mayor cantidad en cada año
top_producto_año = ventas_producto_año.loc[
    ventas_producto_año.groupby('Año')['Cantidad'].idxmax()
]

top_producto_año = top_producto_año.sort_values('Año')

print(top_producto_año)

# Creo un gráfico de barras para visualizar los productos mas vendidos por año

plt.figure(figsize=(12, 6))

bars = plt.bar(
    top_producto_año['Año'].astype(str),
    top_producto_año['Cantidad'],
    color='steelblue'
)

plt.title('Producto más vendido por año')
plt.xlabel('Año')
plt.ylabel('Cantidad vendida')

# Etiqueta con el nombre del producto
for bar, producto in zip(bars, top_producto_año['Producto']):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 20,
        producto,
        ha='center',
        fontsize=10
    )

# Creo valores encima de columnas

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height()/2,
        f'{int(bar.get_height())}',
        ha='center',
        color='white',
        fontweight='bold'
    )

plt.tight_layout()
plt.show()

#======================================
# 3. ANALISIS POR TIENDAS
#======================================

# Creo un DataFrame con las tiendas que más han vendido, junto con la cantidad total de unidades vendidas y el importe total de ventas.

df_ventas_por_tienda = (
    df_productos.groupby('Id_canal')
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum'),
    )
    .sort_values('Cantidad_Total', ascending=False)
)
df_ventas_por_tienda

# Reviso la venta de productos por tienda y año
df_ventas_por_tienda_año = (
    df_productos.groupby(['Id_canal', 'Año'])
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum'),
    )
    .reset_index()
    .sort_values(['Id_canal', 'Año'])
)

df_ventas_por_tienda_año

# Creo un gráfico para mostrar la evolución de ventas por tienda y año

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

for canal in df_ventas_por_tienda_año['Id_canal'].unique():
    df_temp = df_ventas_por_tienda_año[df_ventas_por_tienda_año['Id_canal'] == canal]
    plt.plot(
        df_temp['Año'],
        df_temp['Importe_Total'],
        marker='o',
        linewidth=2,
        label=f'Tienda {canal}'
    )

plt.title('Evolución de Ventas por Tienda y Año')
plt.xlabel('Año')
plt.ylabel('Importe Total (€)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

#======================================
# 4. ANALISIS POR CANAL
#======================================

# Creo un DataFrame con las ventas totales por canal, junto con la cantidad total de unidades vendidas y el importe total de ventas.

df_ventas_por_canal = (
    df_productos.groupby('Canal')
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum'),
    )
    .sort_values('Cantidad_Total', ascending=False)
)
df_ventas_por_canal

#========================================
# 5. ANALISIS POR METODO DE ENVIO
#========================================

# Creo un DataFrame con las ventas totales por método de envío, junto con la cantidad total de unidades vendidas y el importe total de ventas.


df_ventas_por_metodo_envio = (
    df_productos.groupby('Metodo_envio')
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum'),
    )
    .sort_values('Cantidad_Total', ascending=False)
    .reset_index()
)

df_ventas_por_metodo_envio

#======================================
# 6. ANALISIS POR VALOR DE PEDIDO
#======================================

# Creo un DataFrame con las ventas totales segun el rango de valor de pedido, junto con la cantidad total de unidades vendidas y el importe total de ventas.


df_ventas_por_valor_pedido = (
    df_productos.groupby('Rango_valor_pedido')
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum'),
    )
    .sort_values('Cantidad_Total', ascending=False)
    .reset_index()
)

df_ventas_por_valor_pedido

# Creo un DataFrame con las ventas totales segun el rango de valor de pedido, junto con la cantidad total de unidades vendidas y el importe total de ventas.


df_ventas_por_valor_pedido = (
    df_productos.groupby('Rango_valor_pedido')
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum'),
    )
    .sort_values('Cantidad_Total', ascending=False)
    .reset_index()
)

df_ventas_por_valor_pedido

#==================================
# 7. ANALISIS POR COSTE DE ENVIO
#==================================

# Creo un DataFrame con los productos con mayor coste de envio por año, junto con la cantidad total de unidades vendidas y el importe total de ventas.

# Creo un valor para obtener el producto con mayor coste de envío por año
idx = df_productos.groupby('Año')['Coste_envio'].idxmax()

df_ventas_por_coste_envio = df_productos.loc[idx, ['Año', 'Producto', 'Cantidad', 'Coste_envio']]
df_ventas_por_coste_envio = df_ventas_por_coste_envio.rename(columns={
    'Cantidad': 'Cantidad_Total',
    'Coste_envio': 'Coste_Total'
})

df_ventas_por_coste_envio

# Creo un grafico de lineas para mostrar los productos con más costes de envio por año

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))

plt.plot(
    df_ventas_por_coste_envio['Año'],
    df_ventas_por_coste_envio['Coste_Total'],
    marker='o',
    linewidth=2,
    color='steelblue'
)

plt.xlabel('Año')
plt.ylabel('Coste de envío')
plt.title('Producto con mayor coste de envío por año')
plt.grid(True, linestyle='--', alpha=0.5)

# Más espacio para las etiquetas
plt.ylim(
    df_ventas_por_coste_envio['Coste_Total'].min() - 0.5,
    df_ventas_por_coste_envio['Coste_Total'].max() + 0.5
)

for x, y, producto in zip(
    df_ventas_por_coste_envio['Año'],
    df_ventas_por_coste_envio['Coste_Total'],
    df_ventas_por_coste_envio['Producto']
):
    plt.annotate(
        producto,
        (x, y),
        xytext=(0, 8),
        textcoords='offset points',
        ha='center'
    )

plt.tight_layout()
plt.show()

#==================================
# 8. ANALISIS DEMOGRÁFICO
#==================================

#======================
# 8.1 Analisis por Páis
#======================

# Creo un DataFrame para mostar los paises donde más productos se han vendido

df_ventas_por_pais = (
    df_productos.groupby('Pais')
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum'),
    )
    .sort_values('Cantidad_Total', ascending=False)
    .reset_index()
)

df_ventas_por_pais

df_ventas_por_pais = df_ventas_por_pais.sort_values('Importe_Total', ascending=True)
df_ventas_por_pais

# Creo un grafico de barras para mostrar los resultados

plt.figure(figsize=(10,6))

plt.barh(
    df_ventas_por_pais['Pais'],
    df_ventas_por_pais['Cantidad_Total'],
    color='steelblue'
)

plt.xlabel('Cantidad total')
plt.ylabel('País')
plt.title('Países donde más productos se han vendido')


for pais, cantidad, importe in zip(
    df_ventas_por_pais['Pais'],
    df_ventas_por_pais['Cantidad_Total'],
    df_ventas_por_pais['Importe_Total']
):
    etiqueta = f"{cantidad:,} unidades\n{importe:,.2f} €"
    
    plt.text(
        cantidad + (cantidad * 0.02),   
        pais,
        etiqueta,
        va='center',
        fontsize=9,
        color='black',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
    )

plt.tight_layout()
plt.show()

#=========================
# 8.2. Analisis por Región
#=========================

# Creo un DataFrame para ver los paises y sus regiones con la cantidad e importe de productos vendidos
df_ventas_por_pais_region = (
    df_productos.groupby(['Pais', 'Region'])
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum')
    )
    .reset_index()
    .sort_values(['Pais', 'Cantidad_Total'], ascending=[True, False])
)


df_ventas_por_pais_region

# 1. Creo un DataFrame para ver los paises y sus regiones con la cantidad e importe de productos vendidos

df_ventas_por_pais_region = (
    df_productos.groupby(['Pais', 'Region'])
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum')
    )
    .reset_index()
)

# 2. Ordeno los países por mayor cantidad total
totales_pais = (
    df_ventas_por_pais_region.groupby('Pais')['Cantidad_Total']
    .sum()
    .sort_values(ascending=False)
)

df_ventas_por_pais_region['Pais'] = pd.Categorical(
    df_ventas_por_pais_region['Pais'],
    categories=totales_pais.index,
    ordered=True
)

# 3. Ordeno las regiones dentro de cada país por mayor cantidad
df_ventas_por_pais_region = df_ventas_por_pais_region.sort_values(
    ['Pais','Cantidad_Total'],
    ascending=[True, False]
)

df_ventas_por_pais_region

df_ventas_por_pais_region = df_ventas_por_pais_region.sort_values(
    ['Pais','Cantidad_Total'],
    ascending=[False,True]
)

# Creo un grafico de barras para ver los resultados de paises y regiones con mas unidades vendidas

import matplotlib.pyplot as plt
import numpy as np

df = df_ventas_por_pais_region.copy()

paises = df['Pais'].unique()
regiones = df['Region'].unique()

colores = {
    regiones[0]: 'red',
    regiones[1]: 'orange',
    regiones[2]: 'green',
    regiones[3]: 'blue'
}

altura = 0.20  
plt.figure(figsize=(12, 8))

usadas_en_leyenda = set()

for i, pais in enumerate(paises):
    df_pais = (
        df[df['Pais'] == pais]
        .sort_values('Cantidad_Total', ascending=True) 
    )


    offsets = np.linspace(
        -altura * (len(df_pais) - 1) / 2,
        altura * (len(df_pais) - 1) / 2,
        len(df_pais)
    )

    for offset, (_, fila) in zip(offsets, df_pais.iterrows()):
        region = fila['Region']
        cantidad = fila['Cantidad_Total']

    
        color = colores.get(region, 'gray')

        plt.barh(
            i + offset,
            cantidad,
            height=altura,
            color=color,
            alpha=0.85,
            label=region if region not in usadas_en_leyenda else None
        )


        plt.text(
            cantidad + cantidad * 0.02,
            i + offset,
            f"{cantidad:,} u",
            va='center',
            fontsize=9,
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
        )

    usadas_en_leyenda.update(df_pais['Region'])

plt.yticks(range(len(paises)), paises)
plt.xlabel("Cantidad total")
plt.ylabel("País")
plt.title("Ventas por Región (Cantidad)")
plt.legend(title="Región", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()

#========================
# 8.3 Analisis por Ciudad
#========================

# 1. Creo un DataFrame para ver los paises y sus ciudades con la cantidad e importe de productos vendidos
df_ventas_por_pais_ciudad = (
    df_productos.groupby(['Pais', 'Ciudad'])
    .agg(
        Cantidad_Total=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum')
    )
    .reset_index()
)

# 2. Ordeno los países por mayor cantidad total
totales_pais = (
    df_ventas_por_pais_ciudad.groupby('Pais')['Cantidad_Total']
    .sum()
    .sort_values(ascending=False)
)

# 3. Convierto la columna Pais en categórica con el orden correcto
df_ventas_por_pais_ciudad['Pais'] = pd.Categorical(
    df_ventas_por_pais_ciudad['Pais'],
    categories=totales_pais.index,
    ordered=True
)

# 4. Ordeno las ciudades dentro de cada país por mayor cantidad
df_ventas_por_pais_ciudad = df_ventas_por_pais_ciudad.sort_values(
    ['Pais', 'Cantidad_Total'],
    ascending=[True, False]
)

df_ventas_por_pais_ciudad

# Creo un grafico de barras los paises y sus ciudades con la cantidad e importe de productos vendidos

import matplotlib.pyplot as plt
import numpy as np

df = df_ventas_por_pais_ciudad.copy()

# Orden descendente de países (ya viene ordenado por totales)
paises = df['Pais'].cat.categories[::-1] 
num_paises = len(paises)

plt.figure(figsize=(12, 10))

height = 0.15
y = np.arange(num_paises)

for i, pais in enumerate(paises):

    subset = df[df["Pais"] == pais].sort_values("Cantidad_Total", ascending=False)
    num_ciudades = len(subset)

    start = y[i] - (height * (num_ciudades - 1) / 2)

    for j, row in enumerate(subset.itertuples()):
        pos_y = start + (num_ciudades - 1 - j) * height

        plt.barh(pos_y, row.Cantidad_Total, height=height)
        plt.text(row.Cantidad_Total + 800, pos_y, row.Ciudad,
                 va='center', fontsize=10)

plt.yticks(y, paises)

plt.title("Ciudades por país con cantidad total de productos vendidos")
plt.xlabel("Cantidad total de productos vendidos")

plt.tight_layout()
plt.show()

#=================================
# 9. ANALISIS SOCIOECONOMICO
#=================================

#==================================
# 9.1 Analisis por Edad de Clientes
#==================================

# Creo un DataFrame para ver los clientes con la cantidad e importe de productos vendidos por rango de edades

# Mediante un buckle for selecciono la columna de edad disponible
age_col = None
for col in ['age']:
    if col in df_analisis.columns:
        age_col = col
        break

if age_col is None:
    # La columna disponible en el DataFrame se llama "Edad"
    posibles_columnas_edad = ['Edad', 'edad', 'Age', 'age']

    age_col = next(
        (col for col in posibles_columnas_edad if col in df_analisis.columns),
        None
    )

    if age_col is None:
        raise ValueError(
            f"No se encontró una columna de edad. "
            f"Columnas disponibles: {list(df_analisis.columns)}"
        )

    df_analisis[age_col] = pd.to_numeric(
        df_analisis[age_col],
        errors='coerce'
    )

# Creo una lista con edades y sus rangos y una variable que divida una variable numérica en intervalos (bins) y le asigne una etiqueta a cada intervalo.
edades = [0, 25, 35, 45, 55, 65, 75, 120]
rangos = ['18-25', '26-35', '36-45', '46-55', '56-65', '66-75', '76+']

df_analisis['Rango de edad'] = pd.cut(
    df_analisis[age_col],
    bins=edades,
    labels=rangos,
    include_lowest=True,
    right=True
)

# Agrego una tabla con las columnas Rango de edad, Total, Cantidad de productos, Importe de ventas

analisis_edad = (
    df_analisis.groupby('Rango de edad', dropna=False)
    .agg(
        Total=('Rango de edad', 'count'),
        Cantidad_total=('Cantidad', 'sum'),
        Importe_total=('Importe', 'sum')
        
    )
    .reset_index()
)


# Compruebo el resultado
analisis_edad = analisis_edad.sort_values('Rango de edad').reset_index(drop=True)
analisis_edad

# Gráfico de columnas para mostrar las ventas de productos a clientes por rango de edad
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(analisis_edad['Rango de edad'], analisis_edad['Cantidad_total'], color='skyblue')
plt.title('Ventas a Clientes por Rango de Edad')
plt.xlabel('Rango de edad')
plt.ylabel('Cantidad_total')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

#===================================
# 9.2 Analisis por Nivel de Ingresos
#===================================

# Creo un DataFrame para ver los productos vendidos a clientes por su nivel de ingresos

analisis_nivel_ingresos = (
    df_analisis.groupby('Nivel_ingresos')
    .agg(
        Cantidad_total=('Cantidad', 'sum'),
        Importe_total=('Importe', 'sum')
        
    )
    .reset_index()
)

analisis_nivel_ingresos = analisis_nivel_ingresos.sort_values('Cantidad_total', ascending=False)

analisis_nivel_ingresos

#============================
# 9.3 Analisis por Antiguedad
#============================

# Creo un DataFrame para ver los productos vendidos a clientes por su antiguedad
analisis_cliente_antiguedad = (
    df_analisis.groupby('Antiguedad')
    .agg(
        Cantidad_total=('Cantidad', 'sum'),
        Importe_total=('Importe', 'sum')
        
)
.reset_index()

)

analisis_cliente_antiguedad = analisis_cliente_antiguedad.sort_values('Cantidad_total', ascending=False)

analisis_cliente_antiguedad

#=========================
# 9.4 Analisis por Genero
#=========================

# Creo un DataFrame para ver los productos vendidos a clientes por su genero
analisis_cliente_genero = (
    df_analisis.groupby('Genero')
    .agg(
        Cantidad_total=('Cantidad', 'sum'),
        Importe_total=('Importe', 'sum')
        
)
.reset_index()

)

analisis_cliente_genero = analisis_cliente_genero.sort_values('Cantidad_total', ascending=False)

analisis_cliente_genero

#========================================================================
# 10. ANALISIS DE DISTRIBUCIÓN DE VENTAS POR RANGO DE VALOR, PAIS Y CANAL
#========================================================================

# Agrupar ventas por producto, rango de valor, país, región, ciudad y canal
df_ventas_rango_valor_pais_canal= (
    df_analisis
    .groupby([
        'Producto',
        'Rango_valor_pedido',
        'Pais',
        'Region',
        'Ciudad',
        'Canal'
    ])
    .agg(
        Cantidad_Vendida=('Cantidad', 'sum'),
        Importe_Total=('Importe', 'sum')
    )
    .reset_index()
    .sort_values(['Pais', 'Region', 'Ciudad', 'Producto'])
)

df_ventas_rango_valor_pais_canal

# Muestro los datos en un Dashboard

import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# 1. Preparación del dataset
# ============================

df_dash = (
    df_analisis
    .groupby([
        'Producto',
        'Rango_valor_pedido',
        'Pais',
        'Region',
        'Ciudad',
        'Canal'
    ])
    .agg(
        Cantidad_Vendida=('Cantidad', 'sum'),
        Importe_Vendido=('Importe', 'sum'),
        Num_Transacciones=('Id_venta', 'count')
    )
    .reset_index()
)

# ============================
# 2. Configuración general
# ============================

sns.set(style="whitegrid")
plt.figure(figsize=(22, 18))


# ============================
# Gráfico 1 : Ventas por Nivel y País
# ============================

plt.subplot(3, 2, 1)
nivel_pais = (
    df_dash.groupby(['Pais', 'Rango_valor_pedido'])['Cantidad_Vendida']
    .sum()
    .reset_index()
)

sns.barplot(
    data=nivel_pais,
    x='Pais',
    y='Cantidad_Vendida',
    hue='Rango_valor_pedido',
    palette='Set1'
)
plt.title("Ventas por Nivel de Producto y País")
plt.xticks(rotation=45)


# ============================
# Gráfico 2: Ventas por producto y rango
# ============================

plt.subplot(3, 2, 2)
sns.barplot(
    data=df_dash.groupby(['Producto', 'Rango_valor_pedido'])['Cantidad_Vendida'].sum().reset_index(),
    x='Producto',
    y='Cantidad_Vendida',
    hue='Rango_valor_pedido',
    palette='Set2'
)
plt.title("Ventas por Producto y Rango de Valor")
plt.xticks(rotation=45)


# ============================
# Gráfico 3: Ventas por Canal y País
# ============================

plt.subplot(3, 2, 3)
canal_pais = (
    df_dash.groupby(['Pais', 'Canal'])['Cantidad_Vendida']
    .sum()
    .reset_index()
)

sns.barplot(
    data=canal_pais,
    x='Pais',
    y='Cantidad_Vendida',
    hue='Canal',
    palette='coolwarm'
)
plt.title("Ventas por Canal y País")
plt.xticks(rotation=45)

