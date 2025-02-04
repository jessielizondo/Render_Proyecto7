# Cargar librerías
import pandas as pd
import plotly.express as px
import streamlit as st


# Cargar datos
car_data = pd.read_csv(r'C:\Users\Dell\Documents\Data Science Program\Sprint 7\Directorio Principal\Render_Proyecto7\vehicles_us.csv')
car_data["condition"] = car_data["condition"].astype(str)

# Título
st.header("Anuncios de venta de coches", divider = "red")

# Crear un filtro para seleccionar condiciones
conditions = car_data["condition"].unique()
selected_condition = st.multiselect("Selecciona las condiciones de los coches", conditions, default=conditions)

# Filtrar los datos basados en la selección del usuario
filtered_data = car_data[car_data["condition"].isin(selected_condition)]


# Checkbox para crear histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: 
    st.write('Creación de un histograma interactivo para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma
    fig = px.histogram(filtered_data, x="model_year", color="condition", 
                       title='Relación entre Condición y Año de Modelo',
                       labels={'model_year': 'Año del modelo','condition': 'Condición'},
                       opacity=0.8,
                       log_y=True,  # Usar escala logarítmica para el eje Y
                       color_discrete_sequence=['lightpink', 'lightgreen', 'lightblue', 'lightcoral', 'lightsalmon', 'lightseagreen'], 
                       category_orders={"condition": sorted(selected_condition)})  # Ordenar las condiciones por selección
    
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)


# Checkbox para construir gráfico de dispersión
build_disp = st.checkbox('Construir gráfico de dispersión')

if build_disp:
    st.write('Creación de un gráfico de dispersión interactivo para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el gráfico
    fig = px.scatter(car_data, x="odometer", y="price", color="condition",
                 title="Relación entre Precio y Kilometraje",
                 labels={"odometer": "Kilometraje", "price": "Precio"},
                 opacity=0.7)

# Mostrar el gráfico interactivo
st.plotly_chart(fig, use_container_width=True)