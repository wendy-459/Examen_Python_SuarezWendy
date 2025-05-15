def calcular_propina(total, porcentaje):
    return round(total * (porcentaje / 100), 2)

def calcular_total_con_propina(total, propina):
    return round(total + propina, 2)

def dividir_total(total, personas):
    if personas <= 0:
        return None
    return round(total / personas, 2)
