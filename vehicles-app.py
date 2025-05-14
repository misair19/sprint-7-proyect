# Importación de librerías
import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

# Carga del dataset
vehicles_df = pd.read_csv('vehicles_us.csv')

# Establecer el título
st.title('Anuncios de ventas de vehículos')

# Establecer un encabezado
st.header('Distribución general del recorrido del vehículo')
st.write('A continuación se presentan estadísticas de trayecto acumulado de los vehículos listados')

# Crear un botón
hist_button = st.button('Construir histograma') 

# al hacer clic en el botón, escribir un mensaje     
if hist_button: 
    # crear un histograma
    fig = px.histogram(vehicles_df, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig)

# Establecer un encabezado
st.header('Distribución general de precios y distancia recorrida')
st.write('Se presentan estadísticas de precios de los vehículos, la distancia recorrida y su condición')
# Crear un botón
hist_button = st.button('Construir gráfico de dispersión') 

# al hacer clic en el botón, escribir un mensaje     
if hist_button: 
    # crear un gráfico de dispersión
    fig = px.scatter(vehicles_df, x="odometer", y="price", color='condition')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig)

# Establecer un encabezado
st.header('Distribución de precios y estado de los vehículos por modelo')

# Crear un menú desplegable
modelo_seleccionado = st.selectbox("Selecciona un modelo:", vehicles_df['model'].unique())

# Filtrar por modelo
df_filtrado = vehicles_df[vehicles_df['model'] == modelo_seleccionado]

# Mostrar gráfico
if not df_filtrado.empty:
    fig, ax = plt.subplots(figsize=(7, 3)) # crear la figura y el eje
    sns.histplot(data=df_filtrado, x="price", hue="condition", multiple="stack", palette="deep", edgecolor=".3", linewidth=.5) # crear el histograma
    st.pyplot(fig) # mostrar el gráfico
    st.write('Datos para', modelo_seleccionado)
    st.write(df_filtrado)
else:
    st.warning("No hay datos para ese modelo.") # advertencia si no hay datos disponibles

st.write('Para', modelo_seleccionado, 'elija la información que desea analizar:')
# crear una casilla de verificación

option1 = st.button('Gráfico de dispersión del precio en función del recorrido') 
option2 = st.button('Gráfico de dispersión del precio en función del año')

# al hacer clic en el botón     
if option1 and not option2: 
    # crear un gráfico de dispersión
    fig = px.scatter(df_filtrado, x="odometer", y="price", color='condition')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig)
elif option2 and not option1:
    # crear un gráfico de dispersión
    fig = px.scatter(df_filtrado, x="model_year", y="price", color='condition')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig)
