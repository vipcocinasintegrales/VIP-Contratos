import os
import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="VIP Contratos",
        page_icon="🪚",
        layout="wide"
    )

    # Cabecera con logo
    carpeta_actual = os.path.dirname(__file__)
    ruta_logo = os.path.join(carpeta_actual, "assets", "logo.png")

    if os.path.exists(ruta_logo):
        st.image(ruta_logo, width=100)
    else:
        st.warning("⚠️ Logo no encontrado en 'app/assets/logo.png'")

    st.title("🪚 VIP Contratos")
    st.subheader("Sistema inteligente de cotizaciones y contratos")

    st.markdown("---")

    # Sección de bienvenida
    st.write(
        "Bienvenido al sistema VIP-Contratos. "
        "Aquí podrás generar cotizaciones, contratos y exportar documentos automáticamente."
    )

    # Botón de prueba para futuras cotizaciones
    if st.button("Generar cotización de prueba"):
        st.success("✅ Funcionalidad de cotización en construcción.")

    st.markdown("---")
    st.caption("© 2025 VIP Contratos - Todos los derechos reservados")

if __name__ == "__main__":
    main()
