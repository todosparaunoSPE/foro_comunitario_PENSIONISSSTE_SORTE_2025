# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:22:18 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd

# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Título de la aplicación
page = st.sidebar.radio("Navegar por", ["Formulario", "Comentarios"])

# Cambiar el título dependiendo de la página seleccionada
if page == "Formulario":
    st.title("Foro Comunitario de AFORE PENSIONISSSTE - ¡ Sorteo 2025 !")
elif page == "Comentarios":
    st.title("Comentarios Recientes del Foro Comunitario")

# Sidebar: Foro Comunitario de AFORE PENSIONISSSTE
st.sidebar.title("Foro Comunitario de AFORE PENSIONISSSTE - Sorteo 2025")
st.sidebar.markdown("""
¡Bienvenidos al foro de PENSIONISSSTE! Este es un espacio creado para que puedas compartir tus experiencias, resolver dudas y aprender más sobre el sorteo anual de AFORE PENSIONISSSTE.

Preguntas sobre el Sorteo AFORE PENSIONISSSTE 2025:

1. **¿Qué opinas sobre el sorteo anual de AFORE PENSIONISSSTE?**
   Comparte tu experiencia o expectativas sobre este sorteo.

2. **¿Crees que el sorteo de AFORE PENSIONISSSTE beneficia a los trabajadores que participan?**
   ¿Cómo crees que se podría mejorar este sorteo?

3. **¿Cómo afectaría el resultado del sorteo en tus planes para el retiro?**
   ¿Estás confiado en que el sorteo beneficiará tu futuro pensionario?

4. **¿Qué piensas sobre las medidas de transparencia que implementa PENSIONISSSTE en el sorteo?**
   ¿Consideras que el proceso es justo y claro para los participantes?

5. **¿Te gustaría que se hicieran más sorteos a lo largo del año?**
   ¿Qué otros tipos de incentivos o beneficios te gustaría ver en este tipo de sorteos?

6. **¿Qué sugerencias tienes para mejorar la participación en el sorteo AFORE PENSIONISSSTE?**
   ¿Qué cambios podrían hacer que más personas se interesen en participar?

7. **¿Te has beneficiado de algún sorteo de AFORE en el pasado?**
   Cuéntanos tu experiencia si has sido afortunado en otros sorteos.
""")

# Enlace del Google Forms modificado para incrustar
google_forms_url = "https://docs.google.com/forms/d/e/1FAIpQLSd1WTeiABRY8Pwsy7bQAhMSiicwrQy3zGAuNS4s4veur8p1OQ/viewform?embedded=true"

# URL pública de Google Sheets para leer los datos como CSV
sheet_id = "1IJcQrfbQ5SsIlO3pmbAV9j3Br4vlsIYxXKob0cFTmcE"
sheet_name = "Hoja1"  # Cambia esto por el nombre de la hoja que almacena las respuestas
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Leer los datos desde Google Sheets
df = pd.read_csv(csv_url)

# Si la página seleccionada es "Formulario"
if page == "Formulario":
    # Mostrar el formulario en un iframe
    st.components.v1.html(
        f"""
        <iframe src="{google_forms_url}" width="640" height="800" frameborder="0" marginheight="0" marginwidth="0">
        Cargando…
        </iframe>
        """,
        height=800,
    )

    # Agregar espacio entre los botones
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

# Si la página seleccionada es "Comentarios"
if page == "Comentarios":
    # Mostrar solo la lista de comentarios
    st.subheader("Comentarios Recientes")

    if 'Comentarios' in df.columns:
        for i, comentario in enumerate(df['Comentarios'], 1):
            st.markdown(f"**{i}.** {comentario}")
    else:
        st.write("No se encontraron comentarios en las respuestas.")
