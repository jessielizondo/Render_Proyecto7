# Cargar librerías
import pandas as pd
import plotly.express as px
import streamlit as st


# Cargar datos
car_data = pd.read_csv(r'C:\Users\Dell\Documents\Data Science Program\Sprint 7\Directorio Principal\Render_Proyecto7\vehicles_us.csv')
car_data["condition"] = car_data["condition"].astype(str)

# Título
st.header("Anuncios de venta de coches", divider = "gray")



# Botón para construir histograma
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear el histograma
    fig = px.histogram(car_data, x="condition", y="price",
                       title='Histograma de la relación entre condición y precio',
                       labels={'price': 'price'},
                       opacity=0.8,
                       log_y=True,  # Usar escala logarítmica para el eje Y
                       color="condition",  # Colorear por condición
                       color_discrete_sequence=['lightpink', 'lightgreen', 'lightblue', 'lightcoral', 'lightsalmon']  # Colores de las barras
                       )    

    st.plotly_chart(fig, use_container_width=True)