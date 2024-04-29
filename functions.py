import streamlit as st
import pandas as pd

def home(dataframe):
    st.title('Cargatron')
    st.image('img/puntos-recarga-madrid.jpg',caption='Coche cargando')
    with st.expander('¿Quieres saber más?'):
        st.write('Ante el problema climático al que nos enfrentamos, el coche eléctrico se \
                plantea como una solución posible. Queremos facilitarte que encuentres tu puesto de carga más cercano')
    with st.echo():
        st.dataframe(dataframe)

def datos(dataframe):
    st.map(dataframe,latitude='latidtud',longitude='longitud')
    st.bar_chart(dataframe.groupby(['DISTRITO'])[['Nº CARGADORES']].sum())
    st.bar_chart(dataframe.groupby(['OPERADOR'])[['Nº CARGADORES']].sum())

def menu_filtros(dataframe):
    filtro_distrito = st.sidebar.selectbox('Seleccione un distrito',tuple(dataframe['DISTRITO'].unique()))
    distrito_cbox = st.sidebar.checkbox('Filtra por distrito')
    filtro_operador = st.sidebar.selectbox('Seleccione un operador',tuple(dataframe['OPERADOR'].unique()))
    operador_cbox = st.sidebar.checkbox('Filtra por operador')

    lista_dist = []
    lista_op = []
    if distrito_cbox:
        lista_dist.append(filtro_distrito)
    else:
        lista_dist = dataframe['DISTRITO'].unique()
    
    if operador_cbox:
        lista_op.append(filtro_operador)
    else:
        lista_op = dataframe['OPERADOR'].unique()

    filtro_cargadores_start,filtro_cargadores_end = st.sidebar.select_slider('Filtra por número de cargadores',options=range(1,dataframe[['Nº CARGADORES']].max()[0]+1),value=(1,dataframe[['Nº CARGADORES']].max()[0]))
    df_res = dataframe[(dataframe['DISTRITO'].isin(lista_dist))&(dataframe['OPERADOR'].isin(lista_op))&(dataframe['Nº CARGADORES']>=filtro_cargadores_start)&(dataframe['Nº CARGADORES']<=filtro_cargadores_end)]
    if df_res.shape[0] == 0:
        st.warning('No hay datos para los filtros indicados')
        st.stop()
    else:
        st.map(df_res,latitude='latidtud',longitude='longitud')
        if distrito_cbox == False:
            st.bar_chart(df_res.groupby(['DISTRITO'])[['Nº CARGADORES']].sum())
        if operador_cbox == False:
            st.bar_chart(df_res.groupby(['OPERADOR'])[['Nº CARGADORES']].sum())