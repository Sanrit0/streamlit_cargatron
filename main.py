import streamlit as st
import pandas as pd
from PIL import Image
from functions import home, datos, menu_filtros
#datos, cargar_datos, menu_filtros
#st.beta_expander ahora es expander
# Este es mi script

st.set_page_config(page_title='Cargatron', layout='wide', page_icon=':battery:')
df = pd.read_csv('data/red_recarga_acceso_publico_2021.csv', sep = ';')

opcion = st.sidebar.selectbox('Seleccione una opción del menu',('Home','Datos','Filtros'))
st.sidebar.file_uploader("Carga tus propios datos", type= ['.csv'])

match opcion:
    case 'Home':
        home(df)
    case 'Datos':
        datos(df)
    case 'Filtros':
        menu_filtros(df)

st.balloons()