# Cargar librerías
import pandas as pd
import plotly.express as px
import streamlit as st


# Cargar datos
car_data = pd.read_csv(r'C:\Users\Dell\Documents\Data Science Program\Sprint 7\Directorio Principal\Render_Proyecto7\vehicles_us.csv')
car_data["condition"] = car_data["condition"].astype(str)

# Título
st.header("Análisis de venta de coches", divider = "red")

# Filtros generales
st.sidebar.header("Filtros")
conditions = car_data["condition"].unique()
selected_condition = st.sidebar.multiselect("Selecciona las condiciones de los coches", conditions, default=conditions)

# Filtrar datos según la selección del usuario
filtered_data = car_data[car_data["condition"].isin(selected_condition)]

# HISTOGRAMA
st.sidebar.header("Histograma")
build_histogram = st.sidebar.checkbox('Construir histograma')

if build_histogram: 
    st.subheader('Histograma Interactivo: Relación entre Condición y Año del Modelo')
    fig = px.histogram(filtered_data, x="model_year", color="condition", 
                       title='Relación entre Condición y Año de Modelo',
                       labels={'model_year': 'Año del Modelo', 'condition': 'Condición'},
                       opacity=0.8,
                       log_y=True,  # Usar escala logarítmica para el eje Y
                       color_discrete_sequence=['lightpink', 'lightgreen', 'lightblue', 'lightcoral', 'lightsalmon', 'lightseagreen'], 
                       category_orders={"condition": sorted(selected_condition)})  # Ordenar las condiciones por selección
    
    st.plotly_chart(fig, use_container_width=True)

# GRÁFICO DE DISPERSIÓN
st.sidebar.header("Gráfico de Dispersión")
build_disp = st.sidebar.checkbox('Construir gráfico de dispersión')

if build_disp:
    st.subheader('Gráfico de Dispersión: Relación entre Precio y Kilometraje')
    fig = px.scatter(filtered_data, x="odometer", y="price", color="condition",
                     title="Relación entre Precio y Kilometraje",
                     labels={"odometer": "Kilometraje", "price": "Precio"},
                     opacity=0.7)
    
    st.plotly_chart(fig, use_container_width=True)