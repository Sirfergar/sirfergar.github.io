from numpy import append
import streamlit as st
import pandas as pd

def app():
    
    st.sidebar.header("Análisis grandes Ligas")
    st.sidebar.write("En esta página elije el equipo que quieras de las grandes ligas para poder ver la evolución de la asistencia media anual a lo largo de sus años en primera división.")

    all_data=pd.read_csv('all_data.zip')  
    equipo_elegido=st.selectbox("Elija un equipo de futbol para analizar:",list(all_data["equipo"].drop_duplicates(keep='first')))

    col1, col2= st.columns([0.75, 5])
    col2.title(f'Análisis capacidad {equipo_elegido}')
    col1.image(list(all_data[all_data["equipo"]==equipo_elegido].logo_liga)[0])

    st.title(f'Asistencia media {equipo_elegido}')
    df_by_year=pd.DataFrame(all_data[(all_data['equipo']==equipo_elegido)].iloc[:,5])
    index=list(all_data[(all_data['equipo']==equipo_elegido)].iloc[:,1])
    index=[str(i) for i in index]
    df_by_year=df_by_year.set_axis(index)
    st.bar_chart(df_by_year)


    all_data_free_covid=all_data[(all_data['year']<2020)]

    try:
        media_20_years=round(all_data_free_covid[(all_data_free_covid['year']>1998)*(all_data_free_covid['equipo']==equipo_elegido)].media_espectadores.mean())
    except:
        media_20_years='No hay datos suficientes'
    try:    
        media_10_years=round(all_data_free_covid[(all_data_free_covid['year']>2009)*(all_data_free_covid['equipo']==equipo_elegido)].media_espectadores.mean())
    except:
        media_10_years='No hay datos suficientes'
    try:
        media_5_years=round(all_data_free_covid[(all_data_free_covid['year']>2014)*(all_data_free_covid['equipo']==equipo_elegido)].media_espectadores.mean())
    except:
        media_5_years='No hay datos suficientes'

    st.write('Para los siguientes cálculos no se tienen en cuenta 2020 ni 2021 a consecuencia de la pandemia.')
    st.write(f'Ha tenido una asistencia media de 2020-1999 de: {media_20_years}')
    st.write(f'Ha tenido una asistencia media de 2020-2010 de: {media_10_years}')
    st.write(f'Ha tenido una asistencia media de 2020-2015 de: {media_5_years}')

    st.title(f'Porcentaje de asitencia media {equipo_elegido}')
    df_by_year=pd.DataFrame(all_data[(all_data['equipo']==equipo_elegido)].porcentaje_medio_asistencia)
    index=list(all_data[(all_data['equipo']==equipo_elegido)].iloc[:,1])
    index=[str(i) for i in index]
    df_by_year=df_by_year.set_axis(index)
    st.bar_chart(df_by_year)

    media_pctg_20_years=round(all_data_free_covid[(all_data_free_covid['year']>1998)*(all_data_free_covid['equipo']==equipo_elegido)].porcentaje_medio_asistencia.mean(),2)
    media_pctg_10_years=round(all_data_free_covid[(all_data_free_covid['year']>2009)*(all_data_free_covid['equipo']==equipo_elegido)].porcentaje_medio_asistencia.mean(),2)
    media_pctg_5_years=round(all_data_free_covid[(all_data_free_covid['year']>2014)*(all_data_free_covid['equipo']==equipo_elegido)].porcentaje_medio_asistencia.mean(),2)

    st.write('Para los siguientes cálculos no se tienen en cuenta 2020 ni 2021 a consecuencia de la pandemia.')
    st.write(f'Ha tenido una asistencia media de 2020-1999 del: {media_pctg_20_years}%')
    st.write(f'Ha tenido una asistencia media de 2020-2010 del: {media_pctg_10_years}%')
    st.write(f'Ha tenido una asistencia media de 2020-2015 del: {media_pctg_5_years}%')

    
    st.write('Autor: fernandofergar2@gmail.com Linkedin: https://www.linkedin.com/in/fernandofergar/')    
