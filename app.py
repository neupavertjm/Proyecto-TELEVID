import streamlit as st
import json

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(page_title="Proyecto TELEVID", layout="wide", page_icon="🎮")

# --- RUTAS DE IMÁGENES ---
logos_juegos = {
    'League of Legends': 'lol.jpg',
    'Valorant': 'valorant.jpg',
    'Counter Strike': 'counter.jpg'
}

logo_ila = "ila.jpg"
logo_neupaterm = "neupaterm_logo.png"

# --- CARGAR DATOS ---
with open('data.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

# --- TÍTULO Y DESCRIPCIÓN ---
st.title("🔍 Buscador de términos y usos terminológicos del lenguaje especializado de los videojuegos")
st.markdown(
    """
    **Proyecto realizado por Juan Manuel Neupavert Alzola**  
    Este buscador, que forma parte de la continuación de mi Trabajo de Fin de Máster, permite explorar términos y usos terminológicos pertenecientes al lenguaje especializado de los videojuegos, pudiendo ver los distintos usos que tiene cada término, sus definiciones, los mecanismos de incorporación al español y sus relaciones conceptuales dentro de nuestro corpus.
    """
)

# --- SIDEBAR ---
st.sidebar.title("ℹ️ Información general")
st.sidebar.info(
    "🧩 **TELEVID** fue el primer prototipo funcional de un buscador terminológico aplicado al lenguaje de los videojuegos. "
    "Su diseño se basa en el modelo **DOCUTERM**, desarrollado en el Instituto de Lingüística Aplicada (ILA, Universidad de Cádiz) "
    "por el profesor **Miguel Casas Gómez**, centrado en la documentación de los usos terminológicos. "
    "Puedes consultar la publicación original en: "
    "[Casas Gómez (2022)](https://doi.org/10.4995/rlyla.2022.16249). "
    "A partir de esta base teórica y metodológica surge **NeupaTerm**, un gestor terminológico integral que amplía las posibilidades "
    "de análisis, gestión y documentación de los usos en distintos lenguajes especializados."
)



st.sidebar.markdown("### 👤 Proyecto realizado por")
st.sidebar.markdown("**Juan Manuel Neupavert Alzola**")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/juan-manuel-neupavert/) | [Email](mailto:neupavertjm@gmail.com)")

# --- LOGO NEUPATERM (sidebar con fondo blanco y marco elegante) ---
st.sidebar.markdown("---")
st.sidebar.markdown(
    f"""
    <p style='text-align:center; font-size:13px; color:gray; margin-top:-5px;'>
        Proyecto vinculado:<br>
        <a href='https://neupaterm.com' target='_blank' style='text-decoration:none; color:#2A63B8;'>
            <b>NeupaTerm</b>
        </a><br>
        Gestor terminológico basado en el modelo <b>DOCUTERM</b>.
    </p>
    """,
    unsafe_allow_html=True
)

# --- SECCIÓN DE EVOLUCIÓN EN SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🚀 Evolución del proyecto")
st.sidebar.markdown(
    """
    **TELEVID** fue el primer prototipo funcional de un buscador terminológico aplicado al lenguaje de los videojuegos.  
    A partir de su desarrollo, surge **[NeupaTerm](https://neupaterm.com)**, un gestor terminológico completo basado en el modelo **DOCUTERM**, orientado a documentar **usos terminológicos** y relaciones conceptuales de forma dinámica y multilingüe.
    """
)
st.sidebar.markdown("🧩 TELEVID sirvió como base metodológica y técnica de NeupaTerm.")

# --- INTERFAZ PRINCIPAL ---
st.markdown("### 🕹️ Explora los términos del corpus especializado")
st.markdown("Selecciona un término o escríbelo manualmente para consultar sus usos en el corpus:")

terminos_disponibles = [
    "Ace", "Agente", "Baitear", "Bait", "Baiter", "Boost", "Boostear", "Boosteo", "Bot", "Botlane",
    "Bufo", "Bufar", "Buff", "Carga", "Carrear", "Carry", "Campeón", "Clutcher", "Clutchear", "Clutch", "Debuff",
    "Kit", "Disengage", "Draft", "Drop", "Droppear", "Engagear", "Engage", "Feed", "Feedear", "Flash",
    "Flashear", "FPS", "Frag", "Gankeo", "Gankear", "Gankeado", "Kill", "Matar", "Kill feed", "Nerfeo",
    "Nerfear", "A una bala", "Oneshot", "Oneshotear", "OTP", "Pentakill", "Pentakillear", "Ping", "Pinguear",
    "Pingueo", "Pracc", "Praquear", "Scrimmear", "Scrim", "Solokill", "Solokillear", "Stack", "Stackear",
    "Toplane", "Toplaner"
]

busqueda = ""

# --- SELECTBOX + INPUT MANUAL ---
termino_seleccionado = st.selectbox("📂 Selecciona un término:", [""] + terminos_disponibles)
if termino_seleccionado:
    busqueda = termino_seleccionado

entrada_manual = st.text_input("🖊️ O escribe un término:")
if entrada_manual:
    busqueda = entrada_manual

# --- LÓGICA DE BÚSQUEDA ---
if busqueda:
    busqueda_lower = busqueda.lower()
    exactos = [
        item for item in datos
        if busqueda_lower == item.get("Término en español", "").lower()
        or busqueda_lower == item.get("Término en inglés", "").lower()
    ]

    def mostrar_resultado(r):
        st.markdown(f"### 🎮 **{r.get('Término en español', '')} / {r.get('Término en inglés', '')}**")
        campos = [
            ("Subíndice", "Subíndice"),
            ("Definición", "📘 Definición"),
            ("Mecanismo de incorporación al español", "⚙️ Mecanismo de incorporación"),
            ("Categoría lingüística", "🔤 Categoría lingüística"),
            ("Contextos en español", "💬 Contextos en español"),
            ("Contexto en inglés", "💬 Contexto en inglés"),
            ("Fuente contexto español", "🔗 Fuente contexto en español"),
            ("Fuente contexto inglés", "🔗 Fuente contexto en inglés"),
            ("Relaciones conceptuales", "🧠 Relaciones conceptuales"),
            ("Cuestiones traductológicas", "🈳 Cuestiones traductológicas"),
            ("Fuente", "📚 Fuente"),
            ("Notas", "📝 Notas"),
        ]

        for clave, etiqueta in campos:
            valor = r.get(clave, "")
            if valor:
                st.markdown(f"**{etiqueta}:** {valor}")

        juego_relacionado = r.get('Juego Relacionado', '')
        if juego_relacionado:
            juegos = [j.strip() for j in juego_relacionado.split(',')]
            st.markdown(f"**🎮 Juegos relacionados:**")
            cols = st.columns(len(juegos))
            for i, juego in enumerate(juegos):
                if juego in logos_juegos:
                    with cols[i]:
                        st.image(logos_juegos[juego], width=70)
                        st.markdown(juego)

        st.markdown("---")

    if exactos:
        st.subheader("🔹 Coincidencias exactas:")
        for r in exactos:
            mostrar_resultado(r)
    else:
        st.warning("⚠️ No se encontraron coincidencias exactas.")
else:
    st.info("💡 Introduce un término para comenzar la búsqueda.")

# --- SECCIÓN ADICIONAL: DE TELEVID A NEUPATERM ---
with st.expander("🧩 De TELEVID a NeupaTerm"):
    st.markdown("""
    TELEVID representa el primer paso hacia un entorno más amplio de gestión terminológica.
    
    A partir de su estructura de búsqueda de corpus, surge **[NeupaTerm](https://www.neupaterm.com)**, un sistema que amplía las capacidades de TELEVID para:
    - Gestionar glosarios terminológicos completos.  
    - Documentar los usos terminológicos según el modelo **DOCUTERM**.  
    - Trabajar con equivalencias multilingües y formatos profesionales (JSON, CSV, TMX).  
    
    Ambos proyectos comparten un objetivo común: **mejorar la comprensión y gestión del lenguaje especializado**, tomando los videojuegos como dominio inicial de análisis.
    """)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align:center; background-color:white;
                    border:1px solid #ddd; border-radius:12px;
                    box-shadow:0px 2px 6px rgba(0,0,0,0.1);
                    padding:12px; width:100%;'>
            <img src='neupaterm_logo.png' width='220'>
            <p style='font-size:13px; color:gray; margin-top:8px;'>
                <i>Logo del gestor terminológico <b>NeupaTerm</b>, evolución directa del prototipo TELEVID.</i>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# --- FOOTER ---
st.markdown("<hr>", unsafe_allow_html=True)
col_footer1, col_footer2, col_footer3 = st.columns([1, 4, 1])
with col_footer1:
    st.image(logo_ila, width=80)
with col_footer2:
    st.markdown(
        """
        <div style='font-size:14px; color:gray; line-height:1.4'>
        Este programa es una herramienta basada en mi Trabajo de Fin de Máster, desarrollada con el apoyo del Instituto de Lingüística Aplicada (ILA) de la Universidad de Cádiz.  
        Además, he realizado en este centro las prácticas de empresa del Máster en Ciencias del Lenguaje y sus Aplicaciones.
        </div>
        """,
        unsafe_allow_html=True
    )
with col_footer3:
    st.image(logo_neupaterm, width=80)
