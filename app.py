import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Análisis Exploratorio de Vehículos")

# Descripción de la aplicación
st.write("Esta es una aplicación web interactiva para visualizar datos de vehículos.")

# Cargar el conjunto de datos
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")  # Asegúrate de que el archivo está en la raíz del proyecto
    return df

# Cargar los datos en un DataFrame
df = load_data()

# Mostrar los primeros registros
st.write("Vista previa del conjunto de datos:")
st.dataframe(df.head())

# Crear un botón para mostrar un histograma
if st.button("📊 Mostrar Histograma de Precios", key="hist_button"):
    fig = px.histogram(df, x="price", title="Distribución de Precios de los Vehículos", nbins=50)
    st.plotly_chart(fig)

# Crear un botón para mostrar un gráfico de dispersión
if st.button("📈 Mostrar Gráfico de Dispersión (Año vs Precio)", key="scatter_button"):
    fig_scatter = px.scatter(df, 
                             x="model_year", 
                             y="price", 
                             title="Relación entre Año del Vehículo y Precio", 
                             color="condition",
                             labels={"model_year": "Año del Vehículo", "price": "Precio"},
                             opacity=0.6)
    st.plotly_chart(fig_scatter)


