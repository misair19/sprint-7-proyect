# Importación de librerías
import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

# Carga del dataset
vehicles_df = pd.read_csv(r'C:\PERSONAL\Data Analyst\Sprint 7\sprint-7-proyect\vehicles_us.csv')

# Establecer el título
st.title('Anuncios de ventas de vehículos en Estados Unidos')

# Establecer un encabezado
st.header('Distribución general de precios')
st.write('A continuación se presentan estadísticas de precios de los vehículos listados')

# Crear un botón
hist_button = st.button('Construir histograma') 

# al hacer clic en el botón, escribir un mensaje     
if hist_button: 
    # crear un histograma
    fig = px.histogram(vehicles_df, x="price")
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
    sns.histplot(data=df_filtrado, x="price", hue="condition", multiple="stack", palette="light:m_r",
    edgecolor=".3", linewidth=.5) # crear el histograma
    st.pyplot(fig) # mostrar el gráfico
    st.write('Datos para', modelo_seleccionado)
    st.write(df_filtrado)
else:
    st.warning("No hay datos para ese modelo.") # advertencia si no hay datos disponibles


# crear una casilla de verificación
#build_histogram = st.checkbox('Construir un histograma')

# si la casilla de verificación está seleccionada
#if build_histogram: 
 #   st.write('Construir un histograma para la columna odómetro')
  #      ...




