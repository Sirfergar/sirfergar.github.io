from numpy import append
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    
    
    st.sidebar.header("Comparador estadios")
    st.sidebar.write("En esta página introduces la capacidad que desees y te da el listado de estadios que la superan. Por otro lado puedes incluir una asistencia media anual y ver durantes que temporadas y porque equipos se ha visto superada. ")

    st.write('Seleccione con que ligas se quiere comparar:')
    col1, col2= st.columns([5, 5])
    ligafrancesa=col1.checkbox('League One',value=True)
    bundesliga=col1.checkbox('Bundesliga',value=True)
    premierleague=col1.checkbox('Premier League',value=True)
    laliga=col2.checkbox('La Liga',value=True)
    ligaportugal=col2.checkbox('Liga Portugal',value=True)
    seriea=col2.checkbox('Serie A',value=True)

    all_data=pd.read_csv('all_data.zip') 


    lista=[]

    if ligafrancesa:
        lista.append('ligue-1')
    else:
        try:
            lista.remove('ligue-1')
        except:
            nada=lista

    if bundesliga:
        lista.append('bundesliga')
    else:
        try:
            lista.remove('bundesliga')
        except:
            nada=lista

    if premierleague:
        lista.append('premier-league')
    else:
        try:
            lista.remove('premier-league')
        except:
            nada=lista

    if laliga:
        lista.append('laliga')
    else:
        try:
            lista.remove('laliga')
        except:
            nada=lista

    if ligaportugal:
        lista.append('liga-portugal-bwin')
    else:
        try:
            lista.remove('liga-portugal-bwin')
        except:
            nada=lista

    if seriea:
        lista.append('serie-a')
    else:
        try:
            lista.remove('serie-a')
        except:
            nada=lista

    years = st.slider(
        'Seleccione el rango de fechas para el analisis',
        1999, 2021, (1999, 2021))

    all_data_selection=all_data[all_data['year'].isin(range(years[0],years[1]+1))]
    all_data_selection=all_data_selection[all_data_selection['liga'].isin(lista)]

    capacidad=st.number_input('Indique la capacidad de espectadores para conocer que estadios la superan:',min_value=0, max_value=115000)

    df_capacidad=all_data_selection[(all_data_selection['capacidad']>=capacidad)].iloc[:,[2,3,4]].drop_duplicates(subset=["estadio"],keep='first').sort_values(by=['capacidad'],ascending=False)
    total_estadios=len(all_data_selection.drop_duplicates(subset=["estadio"],keep='first'))
    df_capacidad=df_capacidad.set_axis(range(1,len(df_capacidad)+1))

    st.dataframe(df_capacidad)

    st.write(f'Hay un total de {len(df_capacidad)} estadios que tienen mayor capacidad que la que se ha indicado. Lo que quiere decir que el {round(len(df_capacidad)/total_estadios*100,0)}% de todos los estadios de todos los equipos que han pasado las ligas seleccionadas en las fechas seleccionadas tienen una capacidad superior.')

    asistencia=st.number_input('Indique la asistencia de espectadores para conocer que estadios la superan:',min_value=0, max_value=115000)

    df_asistencia=all_data_selection[(all_data_selection['media_espectadores']>=asistencia)].iloc[:,[1,2,3,4,5,7]].sort_values(by=['media_espectadores'],ascending=False)
    df_asistencia=df_asistencia.set_axis(range(1,len(df_asistencia)+1))

    st.dataframe(df_asistencia)

    st.write(f'Hay un total de {len(df_asistencia)} veces que se ha superado la asistencia media, lo que implica que de todos los datos analizados esta asistencia se ha superado un {round(len(df_asistencia)/len(all_data)*100),0}% de las veces.')

    st.write('Autor: fernandofergar2@gmail.com Linkedin: https://www.linkedin.com/in/fernandofergar/')    