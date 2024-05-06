"""
Este módulo contiene la función `calcular_presupuesto` que calcula cuánto
dinero se debe destinar a cada categoría de un presupuesto mensual.
"""


def calcular_presupuesto(ingreso, porcentaje_gastos_esenciales):
    """
    Calcula cuánto dinero se debe destinar a cada categoría de un presupuesto
    mensual.

    Args:
        ingreso (float): Ingresos mensuales netos.
        porcentaje_gastos_esenciales (int): Porcentaje de ingresos que se
            destinarán a gastos esenciales.

    Returns:
        tuple: Una tupla con tres elementos que representan el dinero que se
            debe destinar a gastos esenciales, deseos y ahorros,
            respectivamente.
    """

    # Calcular necesidades
    necesidades = ingreso * (porcentaje_gastos_esenciales / 100)

    # Calcular deseos y ahorros
    if porcentaje_gastos_esenciales == 50:
        deseos = ingreso * 0.3  # 30% para estilo de vida
        ahorros = ingreso * 0.2  # 20% para ahorros/inversiones
    elif porcentaje_gastos_esenciales == 70:
        deseos = ingreso * 0.2  # 20% para estilo de vida
        ahorros = ingreso * 0.1  # 10% para ahorros/inversiones
    else:
        deseos = (ingreso - necesidades) * 3/5
        ahorros = ingreso - necesidades - deseos

    return necesidades, deseos, ahorros
