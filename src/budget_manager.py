def calcular_presupuesto(ingreso, porcentaje_gastos_esenciales):
    necesidades = ingreso * (porcentaje_gastos_esenciales / 100)
    if porcentaje_gastos_esenciales == 50:
        deseos = ingreso * 0.3  # 30% para estilo de vida
        ahorros = ingreso * 0.2  # 20% para ahorros/inversiones
    elif porcentaje_gastos_esenciales == 70:
        deseos = ingreso * 0.2  # 20% para estilo de vida
        ahorros = ingreso * 0.1  # 10% para ahorros/inversiones
    else:
        deseos = (ingreso - necesidades) * 3/5
        ahorros = ingreso - necesidades - deseos

    # Ajustar los porcentajes de deseos y ahorros si exceden el 100% junto con los gastos esenciales
    total = necesidades + deseos + ahorros

    return necesidades, deseos, ahorros
