import streamlit as st
import json

# Rutas de imágenes por juego
logos_juegos = {
    'League of Legends': 'lol.jpg',
    'Valorant': 'valorant.jpg',
    'Counter Strike': 'counter.jpg'
}

# Logo del ILA para agradecimientos
logo_ila = "ila.jpg"  # Cambia por el nombre real del archivo

# Cargar JSON
with open('data.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

# Configuración página
st.set_page_config(page_title="Proyecto TELEVID", layout="wide")

# --- TÍTULO Y DESCRIPCIÓN ---
st.title("🔍 Buscador de términos y usos terminológicos del lenguaje especializado de los videojuegos")
st.markdown(
        """
        **Proyecto realizado por Juan Manuel Neupavert Alzola**  
        Este buscador, que forma parte de la continuación de mi Trabajo de Fin de Máster, permite explorar términos y usos terminológicos pertenecientes al lenguaje especializado de los videojuegos, pudiendo ver los distintos usos que tiene cada término, sus definiciones, los mecanismos de incorporación al español y sus relaciones conceptuales dentro de nuestro corpus."""
    )

# --- BARRA LATERAL: mensajes breves, contacto, estado ---
st.sidebar.title("ℹ️ Información")
st.sidebar.info("🚧 El proyecto TELEVID (Términos Especializados del Lenguaje Especializado de los Videojuegos) está aún en desarrollo. Algunas funcionalidades pueden no estar disponibles. Para más información, contáctanos por correo.")

st.sidebar.markdown("### Proyecto realizado por")
st.sidebar.markdown("**Juan Manuel Neupavert Alzola**")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/juan-manuel-neupavert/) | [Email](mailto:neupavertjm@gmail.com)")
# --- INPUT DE BÚSQUEDA ---

# Lista fija de términos buscables
terminos_disponibles = [
    "Ace", "Agente", "Baitear", "Bait", "Baiter", "Boost", "Boostear", "Boosteo", "Bot", "Botlane",
    "Bufo", "Bufar", "Buff", "Carrear", "Carry", "Campeón", "Clutcher", "Clutchear", "Clutch", "Debuff",
    "Kit", "Disengage", "Draft", "Drop", "Droppear", "Engagear", "Engage", "Feed", "Feedear", "Flash",
    "Flashear", "FPS", "Frag", "Gankeo", "Gankear", "Gankeado", "Kill", "Matar", "Kill feed", "Nerfeo",
    "Nerfear", "A una bala", "Oneshot", "Oneshotear", "OTP", "Pentakill", "Pentakillear", "Ping", "Pinguear",
    "Pingueo", "Pracc", "Praquear", "Scrimmear", "Scrim", "Solokill", "Solokillear", "Stack", "Stackear",
    "Carga", "Toplane", "Toplaner"
]

# Desplegable para seleccionar término
termino_seleccionado = st.selectbox("📂 También puedes seleccionar un término directamente:", [""] + terminos_disponibles)

# Si se selecciona un término y no se ha escrito nada, usarlo como búsqueda
if termino_seleccionado and not busqueda:
    busqueda = termino_seleccionado

# Campo de texto para introducir término manualmente
busqueda = st.text_input("Escribe un término para buscar (recuerda que este término debe estar en el corpus de la investigación):")


# --- Lógica de búsqueda ---
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
                if clave == "Relaciones conceptuales":
                    st.text(f"{etiqueta}:\n{valor}")
                else:
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

# --- FOOTER ---
st.markdown("---")
col_footer1, col_footer2 = st.columns([1, 4])
with col_footer1:
    st.image(logo_ila, width=80)
with col_footer2:
    st.markdown(
        """
        <div style='font-size:14px; color:gray; line-height:1.4'>
        Este programa es una herramienta basada en mi Trabajo de Fin de Máster, desarrollado con el apoyo del Instituto de Lingüística Aplicada (ILA) de la Universidad de Cádiz, que ha proporcionado medios y recursos bibliográficos fundamentales para su realización.  
        Además, he realizado en este centro de investigación las prácticas de empresa del Máster en Ciencias del Lenguaje y sus Aplicaciones.
        </div>
        """,
        unsafe_allow_html=True
    )
