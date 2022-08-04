from numpy import append
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():

    st.sidebar.header("Análisis capacidad Mestalla")
    st.sidebar.write("En esta página se puede observar la entrada media anual de Mestalla así como el porcentaje medio de asitencia.")

    all_data=pd.read_csv('all_data.zip')  


    col1, col2= st.columns([0.75, 5])


    col2.title('Análisis capacidad nuevo Mestalla')
    col1.image('https://tmssl.akamaized.net/images/wappen/head/1049.png?lm=1406966320')

    st.title('Asistencia media a Mestalla')
    df_by_year=pd.DataFrame(all_data[(all_data['equipo']=='Valencia CF')].iloc[:,5])
    index=list(all_data[(all_data['equipo']=='Valencia CF')].iloc[:,1])
    index=[str(i) for i in index]
    df_by_year=df_by_year.set_axis(index)
    st.bar_chart(df_by_year)

    all_data_free_covid=all_data[(all_data['year']<2020)]

    media_20_years=round(all_data_free_covid[(all_data_free_covid['year']>1998)*(all_data_free_covid['equipo']=='Valencia CF')].media_espectadores.mean())
    media_10_years=round(all_data_free_covid[(all_data_free_covid['year']>2009)*(all_data_free_covid['equipo']=='Valencia CF')].media_espectadores.mean())
    media_5_years=round(all_data_free_covid[(all_data_free_covid['year']>2014)*(all_data_free_covid['equipo']=='Valencia CF')].media_espectadores.mean())

    st.write('Para los siguientes cálculos no se tienen en cuenta 2020 ni 2021 a consecuencia de la pandemia.')
    st.write(f'Mestalla ha tenido una asistencia media de 2020-1999 de: {media_20_years}')
    st.write(f'Mestalla ha tenido una asistencia media de 2020-2010 de: {media_10_years}')
    st.write(f'Mestalla ha tenido una asistencia media de 2020-2015 de: {media_5_years}')

    st.title('Porcentaje de asitencia media a Mestalla')
    df_by_year=pd.DataFrame(all_data[(all_data['equipo']=='Valencia CF')].porcentaje_medio_asistencia)
    index=list(all_data[(all_data['equipo']=='Valencia CF')].iloc[:,1])
    index=[str(i) for i in index]
    df_by_year=df_by_year.set_axis(index)
    st.bar_chart(df_by_year)

    media_pctg_20_years=round(all_data_free_covid[(all_data_free_covid['year']>1998)*(all_data_free_covid['equipo']=='Valencia CF')].porcentaje_medio_asistencia.mean(),2)
    media_pctg_10_years=round(all_data_free_covid[(all_data_free_covid['year']>2009)*(all_data_free_covid['equipo']=='Valencia CF')].porcentaje_medio_asistencia.mean(),2)
    media_pctg_5_years=round(all_data_free_covid[(all_data_free_covid['year']>2014)*(all_data_free_covid['equipo']=='Valencia CF')].porcentaje_medio_asistencia.mean(),2)

    st.write('Para los siguientes cálculos no se tienen en cuenta 2020 ni 2021 a consecuencia de la pandemia.')
    st.write(f'Mestalla ha tenido una asistencia media de 2020-1999 del: {media_pctg_20_years}%')
    st.write(f'Mestalla ha tenido una asistencia media de 2020-2010 del: {media_pctg_10_years}%')
    st.write(f'Mestalla ha tenido una asistencia media de 2020-2015 del: {media_pctg_5_years}%')



    st.write('Autor: fernandofergar2@gmail.com Linkedin: https://www.linkedin.com/in/fernandofergar/')    