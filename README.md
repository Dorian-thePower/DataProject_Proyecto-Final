# 📊 DataProject – Proyecto Final

## Análisis exploratorio de ventas (EDA)

Este documento presenta el análisis exploratorio de datos de ventas en el periodo entre el 2015 y 2022 creados por libre elección, con el objetivo de analizar el progreso de las ventas.

---

# 📖 1. Descripción del proyecto

El proyecto analiza el progreso y el rendimiento de las ventas, usando los datos de los años entre el 2015 y 2022.

Se revisa la evolución de ventas, basándose en los datos demográficos, socioeconómicos, canales de ventas, métodos de envío y también por años para evaluar el rendimiento de ventas desde diferentes perspectivas.

Además, se comparan resultados por tipo de tienda y por país para tener una visión global.

---

# 📂 2. Estructura del proyecto

## 🗄️ 2.1 Datos de origen

Los datos utilizados proceden de los archivos sales.csv y customers.xlsx.

---

## 🔄 2.2 Transformación y limpieza de datos

- Se crea el notebook ETL_Datos.ipynb para realizar la transformación y limpieza de datos.
- En la carpeta Datos_Raw se cargan los archivos CSV y XLSX desde la ruta local y se convierten en DataFrames con Pandas.
- Los DataFrames se renombran como df_sales y df_customer.
- Se realiza transformación, conversión de datos a español y limpieza de valores duplicados, vacíos y nulos en el dataframe df_sales.
- Se unen ambos DataFrames mediante merge(), utilizando la columna Id_cliente, y se crea el DataFrame df_unido.
- Se establece la columna Id_cliente como índice.
- Se realiza transformación, conversión de datos a español y limpieza de valores duplicados, vacíos y nulos en el dataframe df_unido.
- Se eliminan las columnas no necesarias para el análisis: Provincia, Direccón, Teléfono, Correo, Cantidad_num.
- Se revisan los tipos de datos disponibles y se comprueba que no existan duplicados.
- Se realiza tratamiento y normalización de valores de la columna Importe en formato numérico.
- Se cambia el formato de las fechas a dd/mm/aaaa en las columnas Fecha_venta y Fecha_registro.
- Los valores nulos en las columnas Fecha_venta se cambian por los valores de Fecha_registro y viceversa; los valores nulos numéricos se sustituyen por la mediana.
- Se realiza tratamiento y normalización de valores de la columna Descuento en formato numérico decimal.
- Se realiza tratamiento y normalización de valores de la columna Cantidad en formato numérico entero.
- La columna Edad se convierte de decimal a entero.
- Se realiza tratamiento, limpieza y conversión de datos a español de las columnas Genero y Nivel_ingresos.
- Se normalizan los datos de la columna Genero, cambiando valores Desconocido por un género según el listado de nombres de clientes.
- Se normalizan los datos en la columna Nivel_ingresos, cambiando valores Desconocido por bajo, medio o alto según determinados rangos de edad.
- Se normalizan los datos en la columna Region, sustituyendo valores Desconocido según la región de la ciudad de la última venta del mismo cliente.
- Se normalizan los datos en la columna Zona_envio, sustituyendo valores Desconocido según la zona de envío de la ciudad de la última venta del mismo cliente.
- Se normalizan los valores de la columna Nombre, eliminando espacios y convirtiendo los datos a mayúsculas.
- Se crea una nueva columna Antigüedad a partir de los datos de la columna Fecha_registro.
- El resultado final se convierte en CSV y se guarda en la carpeta Data > Processed.

---

# 📊 3. Análisis descriptivo de los datos

Los datos limpios y transformados se guardan en el notebook Analisis_Datos.ipynb, ubicado en la carpeta Notebooks, y en el archivo Analisis_Datos.py, ubicado en la carpeta Datos_Processed.

El dataset contiene:

- 56.608 registros
- 24 columnas
- Periodo de ventas: 2015-2022

Los principales campos utilizados en el análisis son los siguientes:

- Id_cliente: Identificador del cliente
- Id_venta: Identificador de la venta
- Fecha_venta: Fecha de venta del producto
- Importe: Importe de la venta del producto
- Producto: Nombre del producto
- Cantidad: Unidades vendidas
- Descuento: Descuento aplicado
- Canal: Canal de venta
- Region: Región donde se vende
- Estado: Estado del pedido
- Zona_envio: Zona logística de envío
- Metodo_envio: Método logístico de envío
- Peso_paquete: Peso del paquete enviado
- Rango_valor_pedido: Valor del pedido
- Coste_envio: Coste de envío del pedido
- Id_canal: Nombre de canal
- Id_producto: Identificador del producto
- Nombre: Nombre completo del cliente
- Fecha_registro: Fecha de alta del cliente
- Pais: País donde se vende
- Genero: Género del cliente
- Edad: Edad del cliente
- Nivel_ingresos: Nivel económico del cliente
- Ciudad: Ciudad donde se vende
- Antigüedad: Antigüedad del cliente

---

# 📈 4. Análisis estadístico de los datos

A partir del análisis de la tabla df_analisis realizado en Python, se identifican las siguientes conclusiones y tendencias relevantes.

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
