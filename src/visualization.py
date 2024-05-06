"""
Este módulo contiene la función plot_budget que genera un gráfico de pastel
con la distribución del presupuesto en tres categorías: Esenciales, Estilo de 
vida y Ahorros e Inversiones.
"""

# Importar librerías
# - streamlit para mostrar el gráfico en la interfaz
# - matplotlib.pyplot para visualizar gráficos
import streamlit as st
import matplotlib.pyplot as plt


def plot_budget(esenciales, estilo, ahorros):
    """
    Función para visualizar la distribución del presupuesto en un gráfico de
    pastel.

    Args:
        esenciales (float): Porcentaje de gastos esenciales.
        estilo (float): Porcentaje de gastos de estilo de vida.
        ahorros (float): Porcentaje de ahorros e inversiones.

    Returns:
        None
    """

    # Crear una figura para el gráfico de pastel con tamaño 10x6 pulgadas
    plt.figure(figsize=(10, 6))

    # Etiquetas y tamaños de las porciones del gráfico
    labels = ['Esenciales', 'Estilo de vida', 'Ahorro e Inversión']

    # Porcentajes de cada categoría
    sizes = [esenciales, estilo, ahorros]

    # Total para calcular porcentajes
    total = sum(sizes)  # Total para calcular porcentajes

    # Colores para cada categoría
    colors = ['#ADD8E6', '#FFC0CB', '#FFFFE0']

    # Resaltar todas las porciones del gráfico
    explode = (0.05, 0.05, 0.05)

    def make_autopct(values):
        """
        Función para formatear las etiquetas con porcentajes y valores con
        separadores de miles.

        Args:
            values (list): Lista de valores para las etiquetas.

        Returns:
            function: Función para formatear las etiquetas.
        """

        def my_autopct(pct):
            """
            Función para formatear las etiquetas con porcentajes y valores con
            separadores de miles.

            Args:
                pct (float): Porcentaje de la porción.

            Returns:
                str: Etiqueta formateada.
            """

            # Calcular el valor de la porción
            val = int(round(pct*total/100.0))

            # Formatear la etiqueta con porcentaje y valor
            return '{p:.1f}%  (${v:,.0f})'.format(p=pct, v=val)

        # Devolver la función para formatear las etiquetas
        return my_autopct

    # Crear el gráfico de pastel con los datos y opciones anteriores
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct=make_autopct(sizes), shadow=True, startangle=90)

    # Añadir un círculo blanco en el centro del gráfico
    plt.axis('equal')

    # Añadir un título al gráfico
    plt.title('Distribución del Presupuesto', fontsize=16)

    # Mostrar el gráfico
    st.pyplot(plt)
