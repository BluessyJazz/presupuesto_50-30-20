"""
Este script contiene la interfaz gráfica de usuario para el cálculo del
presupuesto 50-30-20. 

El usuario debe ingresar sus ingresos mensuales y seleccionar el método de
presupuesto a utilizar. El programa calculará cuánto dinero debe destinar a
cada categoría de su presupuesto mensual y mostrará el resultado en la
interfaz gráfica.
"""

# Importar librerías
# - streamlit para la interfaz gráfica
# - calcular_presupuesto para calcular el presupuesto
# - plot_budget para visualizar el presupuesto
import streamlit as st
from budget_manager import calcular_presupuesto
from visualization import plot_budget

# Configurar la página
st.set_page_config(page_title='Presupuesto 50-30-20',
                   page_icon='💰',
                   layout='centered',
                   initial_sidebar_state='auto'
                   )


def main():
    """
    Función principal para la interfaz gráfica de usuario

    Args:
        None

    Returns:
        None
    """
    st.title('Presupuesto 50-30-20')
    st.write('Este programa te ayudará a calcular cuánto dinero debes \
             destinar a cada categoría de tu presupuesto mensual')

    with st.form(key='my_form'):
        ingresos = st.number_input('Ingresos mensuales',
                                   min_value=0.0,
                                   help='Ingresos mensuales netos',
                                   format='%f',
                                   step=1000.0
                                   )
        metodo_presupuesto = st.selectbox('Método de presupuesto',
                                          ['50-30-20',
                                           '70-20-10',
                                           'Personalizado'])
        if metodo_presupuesto == 'Personalizado':
            porcentaje_necesidades = st.slider('Porcentaje de gastos \
                                                esenciales',
                                               min_value=50,
                                               max_value=100,
                                               value=50)

        submit_button = st.form_submit_button(label='Calcular presupuesto')

        # Calcular presupuesto
        if metodo_presupuesto == '50-30-20':
            gastos_esenciales = 50
        elif metodo_presupuesto == '70-20-10':
            gastos_esenciales = 70
        elif metodo_presupuesto == 'Personalizado':
            gastos_esenciales = porcentaje_necesidades

        # Validar ingresos
        if submit_button and ingresos == 0:
            st.warning('Ingresa un valor válido para los ingresos')

    if submit_button and ingresos > 0:

        necesidades, deseos, ahorro = \
            calcular_presupuesto(ingresos, gastos_esenciales)

        # Mostrar presupuesto en 3 columnas con su explicación
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('Gastos esenciales')
            st.write(f'💰 ${necesidades:,.0f}')
        with col2:
            st.write('Gastos prescindibles')
            st.write(f'💸 ${deseos:,.0f}')
        with col3:
            st.write('Ahorro e inversión')
            st.write(f'🏦 ${ahorro:,.0f}')

        # Visualizar presupuesto
        plot_budget(necesidades, deseos, ahorro)
        st.markdown('---')

    # Mostrar información sobre el presupuesto 50-30-20
    st.markdown('## Cómo funciona el presupuesto 50-30-20')
    st.write('El presupuesto 50-30-20 es un método simple para distribuir tu \
             dinero en tres categorías principales: gastos esenciales, gastos \
             prescindibles y ahorro e inversión. Aquí tienes una descripción \
             de cada categoría:')
    st.markdown('### Gastos esenciales 💰')
    st.write('Los gastos esenciales son aquellos que son necesarios para \
             mantener tu vida y tu trabajo. Esto incluye alimentos, vivienda, \
             transporte, servicios públicos, seguros y otros gastos básicos.')
    st.markdown('### Gastos prescindibles 💸')
    st.write('Los gastos prescindibles son aquellos que no son esenciales, \
             pero que mejoran tu calidad de vida. Esto incluye \
             entretenimiento, comidas fuera de casa, ropa, viajes y otros \
             gastos discrecionales.')
    st.markdown('### Ahorro e inversión 🏦')
    st.write('El ahorro e inversión es el dinero que guardas para el futuro. \
             Esto incluye ahorros de emergencia, ahorros a largo plazo, \
             contribuciones a la jubilación y otras inversiones.')
    st.markdown('## Otras formas de presupuestar')
    st.write('Además del presupuesto 50-30-20, hay otras formas de \
             presupuestar tu dinero. Algunas personas prefieren el método \
             70-20-10, que destina el 70% a gastos esenciales, el 20% a \
             gastos prescindibles y el 10% a ahorro e inversión. También \
             puedes personalizar tu presupuesto según tus necesidades y \
             objetivos financieros.')


if __name__ == "__main__":
    main()
