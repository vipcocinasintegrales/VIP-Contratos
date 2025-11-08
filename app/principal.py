import streamlit as st

def main():
    st.set_page_config(page_title="VIP Contratos", page_icon="🪚", layout="wide")

    # Cabecera
    st.image("app/assets/logo.png", width=100)
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

    # Pie de página
    st.markdown("---")
    st.caption("© 2025 VIP Contratos - Todos los derechos reservados")

if __name__ == "__main__":
    main()
