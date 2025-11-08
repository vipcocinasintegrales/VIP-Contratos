import os
import streamlit as st

def main():
    # ==============================
    # Configuración de la página
    # ==============================
    st.set_page_config(
        page_title="VIP Contratos",
        page_icon="🪚",
        layout="wide"
    )

    # ==============================
    # Logo
    # ==============================
    carpeta_actual = os.path.dirname(__file__)
    ruta_logo = os.path.join(carpeta_actual, "assets", "logo.png")

    if os.path.exists(ruta_logo):
        st.image(ruta_logo, width=100)
    else:
        st.warning("⚠️ Logo no encontrado en 'app/assets/logo.png'")

    st.markdown("---")

    # ==============================
    # Hola gigante
    # ==============================
    st.markdown(
        "<h1 style='text-align:center; color:#FF5733;'>¡Hola VIP-Contratos!</h1>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ==============================
    # Pie de página
    # ==============================
    st.caption("© 2025 VIP Contratos - Todos los derechos reservados")

if __name__ == "__main__":
    main()
