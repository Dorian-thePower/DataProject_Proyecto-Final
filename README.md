# 📊 DataProject – Proyecto Final

## 📈 Análisis exploratorio de ventas (EDA)

Este documento presenta el análisis exploratorio de datos de ventas en el periodo entre el 2015 y 2022 creados por libre elección, con el objetivo de analizar el progreso de las ventas.

---

# 📖 1. Descripción del proyecto

El proyecto analiza el progreso y el rendimiento de las ventas, usando los datos de los años entre el 2015 y 2022.

Se revisa la evolución de ventas, basándose en los datos demográficos, socioeconómicos, canales de ventas, métodos de envío y también por años para evaluar el rendimiento de ventas desde diferentes perspectivas.

Además, se comparan resultados por tipo de tienda y por país para tener una visión global.

---

# 📂 2. Estructura del proyecto

## 🗃️ 2.1 Datos de origen

Los datos utilizados proceden de los archivos **sales.csv** y **customers.xlsx**.

## 🔄 2.2 Transformación y limpieza de datos

- Se crea el notebook **ETL_Datos.ipynb** para realizar la transformación y limpieza de datos.
- En la carpeta **Datos_Raw** se cargan los archivos CSV y XLSX desde la ruta local y se convierten en DataFrames con Pandas.
- Los DataFrames se renombran como **df_sales** y **df_customer**.
- Se realiza transformación, conversión de datos a español y limpieza de valores duplicados, vacíos y nulos en el dataframe **df_sales**.
- Se unen ambos DataFrames mediante **merge()**, utilizando la columna **Id_cliente**, y se crea el DataFrame **df_unido**.
- Se establece la columna **Id_cliente** como índice.
- Se realiza transformación, conversión de datos a español y limpieza de valores duplicados, vacíos y nulos en el dataframe **df_unido**.
- Se eliminan las columnas no necesarias para el análisis: Provincia, Direccón, Teléfono, Correo, Cantidad_num.
- Se revisan los tipos de datos disponibles y se comprueba que no existan duplicados.
- Se realiza tratamiento y normalización de valores de la columna **Importe** en formato numérico.
- Se cambia el formato de las fechas a **dd/mm/aaaa** en las columnas **Fecha_venta** y **Fecha_registro**.
- Los valores nulos en las columnas **Fecha_venta** se cambian por los valores de **Fecha_registro** y viceversa; los valores nulos numéricos se sustituyen por la mediana.
- Se realiza tratamiento y normalización de valores de la columna **Descuento** en formato numérico decimal.
- Se realiza tratamiento y normalización de valores de la columna **Cantidad** en formato numérico entero.
- La columna **Edad** se convierte de decimal a entero.
- Se realiza tratamiento, limpieza y conversión de datos a español de las columnas **Genero** y **Nivel_ingresos**.
- Se normalizan los datos de estas columnas **Genero**, cambiando valores Desconocido por un género según el listado de nombres de clientes.
- Se normalizan los datos en la columna **Nivel_ingresos**, cambiando valores Desconocido por bajo, medio, alto según determinados rangos de edad.
- Se normalizan los datos en la columna **Region**, sustituyendo valores Desconocido según la región de la ciudad de la última venta del mismo cliente.
- Se normalizan los datos en la columna **Zona_envio**, sustituyendo valores Desconocido según la zona de envío de la ciudad de la última venta del mismo cliente.
- Se normalizan los valores de la columna **Nombre**, eliminando espacios y conversión en mayúsculas.
- Se crea nueva columna **Antigüedad** a partir de los datos de la columna **Fecha_registro**.
- El resultado final se convierte en CSV y se guarda en la carpeta **Data > Processed**.

---

# 📊 3. Análisis descriptivo de los datos

Los datos limpios y transformados se guardan en el notebook **Analisis_Datos.ipynb**, ubicado en la carpeta **Notebooks**, y en el archivo **Analisis_Datos.py**, ubicado en la carpeta **Datos_Processed**.

### 📌 El dataset contiene:

- 56.608 registros
- 24 columnas
- Periodo de ventas: 2015-2022

### 🧾 Principales campos utilizados en el análisis

- **Id_cliente:** Identificador del cliente
- **Id_venta:** identificador de la venta
- **Fecha_venta:** fecha de venta del producto
- **Importe:** importe de la venta del producto
- **Producto:** nombre del producto
- **Cantidad:** unidades vendidas
- **Descuento:** descuento aplicado
- **Canal:** canal de venta
- **Region:** región donde se vende
- **Estado:** estado del pedido
- **Zona_envio:** zona logística de envío
- **Metodo_envio:** método logístico de envío
- **Peso_paquete:** peso del paquete enviado
- **Rango_valor_pedido:** valor del pedido
- **Coste_envio:** coste de envío del pedido
- **Id_canal:** nombre de canal
- **Id_producto:** identificador del producto
- **Nombre:** nombre completo del cliente
- **Fecha_registro:** fecha de alta del cliente
- **Pais:** país donde se vende
- **Genero:** género del cliente
- **Edad:** edad del cliente
- **Nivel_ingresos:** nivel económico del cliente
- **Ciudad:** ciudad donde se vende
- **Antigüedad:** antigüedad del cliente

---

# 📈 4. Análisis estadístico de los datos

A partir del análisis de la tabla **df_analisis** realizado en Python, se identifican las siguientes conclusiones y tendencias relevantes.

## 💰 Importe de venta

**Media:** 503,41 €  
**Mediana (Q2):** 504,01 €

La media y la mediana presentan valores prácticamente idénticos, lo que evidencia una distribución muy equilibrada de los importes de venta.

Asimismo, considerando que el importe mínimo registrado es de 10 € y el máximo de 999 €, no se observan valores atípicos extremos ni concentraciones excesivas en rangos específicos. En consecuencia, puede afirmarse que los importes se distribuyen de forma homogénea a lo largo de toda la muestra.

## 📦 Cantidad de productos

**Media:** 5,52 unidades  
**Mediana (Q2):** 6 unidades

Los pedidos incluyen, en promedio, entre 5 y 6 unidades por compra, lo que sugiere una elevada presencia de compras multiproducto.

Esta característica puede representar una oportunidad para impulsar estrategias de venta cruzada (cross-selling).

## 🏷️ Descuentos

**Media:** 3,06 €  
**Mediana (Q2):** 0 €

La diferencia entre la media y la mediana indica una distribución claramente asimétrica.

Mientras que más del 50% de los pedidos no incluyen ningún descuento, existe un número reducido de operaciones con descuentos elevados que incrementan significativamente el valor medio. Por tanto, el uso de descuentos no parece formar parte de la estrategia comercial habitual, sino que responde a acciones puntuales o promociones específicas.

## 📦 Peso de los paquetes

**Media:** 8,13 kg  
**Mediana (Q2):** 7,50 kg

Los valores obtenidos reflejan un peso medio moderado y una distribución relativamente equilibrada, sin indicios de grandes variaciones entre envíos.

## 🚚 Coste de envío

**Media:** 12,06 €  
**Mediana (Q2):** 10,75 €

El coste logístico muestra una notable estabilidad. Además, al representar únicamente el 2,4% del importe medio de venta (12,06 € sobre 503,41 €), puede considerarse un coste operativo muy eficiente en relación con la facturación generada.

## 👥 Edad de los clientes

**Media:** 49,22 años  
**Mediana (Q2):** 49 años

La coincidencia entre media y mediana indica una distribución equilibrada de edades. El perfil predominante corresponde a clientes de mediana edad, situándose alrededor de los 49 años.

## 🤝 Antigüedad de clientes

**Media:** 7,80 años  
**Mediana (Q2):** 8 años

La cartera de clientes presenta un elevado grado de estabilidad, con una antigüedad promedio cercana a los ocho años. Este dato sugiere un nivel significativo de fidelización y una relación consolidada entre los clientes y la empresa.

## ✅ Conclusión general

Los datos analizados muestran un comportamiento notablemente estable y equilibrado en la mayoría de las variables. El negocio presenta importes de venta homogéneos, clientes con una elevada antigüedad, costes logísticos controlados y una tendencia frecuente a las compras multiproducto. Por otro lado, los descuentos tienen una presencia limitada y parecen utilizarse de forma selectiva, sin constituir un elemento central de la estrategia comercial.

---

# 📊 5. Dashboard operativo y visualización de los datos

Para elaborar el Dashboard operativo y visualizar los datos se utiliza la herramienta de **Power BI**.

## 🏠 Página Dashboard

### 📌 Panel superior

- Segmentadores de datos por filtros de año, metodo_envio, canal, producto, país, ciudad, region y estado.
- Tarjetas KPI con total clientes, pedidos, unidades vendidas, importe ventas, coste envio, ingreso y margen descontando el coste de envio del ingreso.

### 📈 Parte central

- Ventas por año y cantidad de productos.
- Ventas por productos.

### ◀️ Lateral izquierdo

- Recuento de pedidos por producto.

### ▶️ Lateral derecho

- Ventas por país.

## 🔍 Página Analisis

### 📌 Panel superior

- Segmentadores de datos por filtros de año, metodo_envio, canal, producto, país, ciudad, region y estado.
- Tarjetas KPI con total clientes, pedidos, unidades vendidas, importe ventas, coste envio, ingreso y margen descontando el coste de envio del ingreso.

### 📈 Parte central

- Distribución de pedidos por año y estado.
- Ingresos por productos.

### ◀️ Lateral izquierdo

- Ranking de cancelaciones.
- Ingresos por ciudad.

### ▶️ Lateral derecho

- Ratio de coste sobre ventas por tienda.
- Pedidos por rango de edad.

## 📋 Página Detalles

### ◀️ Lateral izquierdo

- Botones de filtros: país, ciudad, región, zona de envío, tienda, canal, estado, producto y método de envío.
- Botones de métricas: pedidos, unidades, ventas, costes e ingreso.

### ▶️ Lateral derecho

- Tabla con las columnas y los valores que se despliegan según los botones seleccionados.

---

# 🔎 6. Informe (hallazgos del análisis)

A continuación, se resumen los principales hallazgos del análisis.

## 📈 6.1 Evolución de ventas por año y cantidad

El 2021 es el año con más ventas realizadas, tanto en productos vendidos (36.127 unidades) como en importe total (3.319.767 €). El aumento de ventas en 2021 es más pronunciado que el aumento de productos.

## 📦 6.2 Productos y pedidos por año

El producto más vendido en todos los años con más pedidos es el **Dispositivo J** con 29020 unidades en 5227 pedidos.

Este mismo producto ha generado mayores ingresos (2.568.156 €).

Por otra parte, es el producto con mayor tasa de cancelación de pedidos (26,48 %).

Mientras que el producto que más se ha vendido en cada año ha sido el **Dispositivo C** con 3948 pedidos.

Producto con menor venta ha sido **Dispositivo F** con 27984 pedidos.

## 🏪 6.3 Ventas por tiendas, canal y estado

El canal de venta **En Línea** es el que más ha vendido (12.922 pedidos) en su año récord 2021.

**Tienda 1** es el punto de venta que más ventas ha realizado en el año 2021 (894.925 €).

**Tienda 4** tiene la mejor ratio (1,64%) de costes sobre las ventas realizadas.

Las ventas por estado presentan estados igualados (24% - 25%) de completado, cancelado, enviado y pendiente.

## 🌎 6.4 Ventas por País, Ciudad y Región

EE. UU. concentra el 46,53% de las ventas.

Los Ángeles lidera las ciudades donde más se ha vendido (2.568.888 €).

La región Oeste es la región donde más se ha vendido (6.511.640 €).

## 👥 6.5 Perfil de cliente y edad

El rango de edad con más compras es 46–55 años.

En general, las ventas por género están bastante equilibradas.

---

# 🎯 7. Resultados y conclusiones

### 💰 Ventas

- Ventas: 25.872.236 €.
- Pedidos completados: 12.950.
- Tasa de finalización: 25,22%.

La principal conclusión es que la organización mantiene una actividad estable y diversificada, sin dependencia significativa de una región, canal o producto concreto. Sin embargo, la tasa de finalización de pedidos es del 25,22%, lo que revela una importante oportunidad de mejora operativa, ya que tres de cada cuatro pedidos no llegan al estado final de completado.

### 📈 Evolución temporal

Las ventas presentan una notable estabilidad a lo largo de todo el período analizado.

- Mejor año: 2021 con 3,319 mil €.
- Menor año: 2020 con 3,121 mil €.
- Diferencia entre ambos: 6,3%.

Esto indica ausencia de caídas significativas, pero también una escasa tendencia de crecimiento, reflejando una etapa de madurez del negocio.

### 🌍 Distribución de ventas por región

La distribución regional es muy homogénea:

- Oeste: 6,51 M€
- Este: 6,47 M€
- Norte: 6,45 M€
- Sur: 6,43 M€

La distribución de las ventas por región es muy homogénea. La diferencia entre la región con mayor facturación y la de menor facturación es de apenas un 1,2 %, lo que refleja una cobertura comercial equilibrada y un rendimiento consistente en todo el territorio.

### 🌎 A nivel de países

Estados Unidos lidera claramente las ventas (46,6%), mientras que el resto de los mercados mantienen una participación relativamente equilibrada.

### 👥 Segmentación de clientes

Los grupos de edad media (46-55 años) generan una parte importante de la facturación 5,21 M€.

La mayor contribución proviene de clientes sénior, indicando una buena aceptación del catálogo en segmentos de mayor capacidad adquisitiva.

#### Por género

- Hombres: 51,5%
- Mujeres: 48,5%

No existen diferencias relevantes, mostrando una cartera de clientes equilibrada.

#### Por ingresos

- Ingresos medios: 2,28 M€
- Ingresos altos: 2,07 M€
- Ingresos bajos: 1,96 M€

El negocio presenta una penetración homogénea en todos los segmentos económicos.

### 🛒 Canales de venta

La distribución de ingresos entre canales es prácticamente uniforme:

- M-Commerce: 1,65 M€
- En Línea: 1,62 M€
- Minorista: 1,64 M€
- En Tienda: 1,58 M€

Esto reduce el riesgo de dependencia de un único canal comercial.

### 📦 Productos

Los dispositivos analizados muestran una distribución muy equilibrada.

La principal oportunidad de mejora está en aumentar la conversión de pedidos a completados y reducir cancelaciones.

Desde una perspectiva operativa, los resultados sugieren que la principal limitación del negocio no está en la captación de pedidos, sino en su conversión a ventas finales.

### 🔄 Conversión y estados de pedido

La tasa de finalización del 25,22% indica que existe un elevado volumen de pedidos que permanecen como:

- Pendientes.
- Enviados.
- Cancelados.

Esto apunta a posibles ineficiencias en los procesos de gestión, seguimiento o cierre comercial.

### 🔀 Diversificación comercial

Los canales físicos y digitales presentan un nivel de actividad muy similar, lo que demuestra una estrategia omnicanal correctamente equilibrada.

### 🚚 Cobertura logística

La presencia de múltiples zonas logísticas y opciones de envío (Express, Standard, Local y Pick-up) refleja una infraestructura logística amplia y flexible.

### 📦 Gestión de productos

Ningún producto concentra de forma excesiva las ventas, reduciendo el riesgo comercial asociado a la dependencia de referencias concretas.
