import filtrar_por_seleccion
import analisis_mestalla
import analisis_seleccion
import articulo

import streamlit as st
st.set_page_config(page_title="Análisis capacidad Mestalla", page_icon="📈")
PAGES = {
    "Artículo estudiando los datos": articulo,
    "Análisis de Mestalla": analisis_mestalla,
    "Análisis grandes Ligas": analisis_seleccion,
    "Comparador estadios": filtrar_por_seleccion

}
st.sidebar.title('Analizador de asistencias')
selection = st.sidebar.radio("Ir a:", list(PAGES.keys()))
page = PAGES[selection]
page.app()
