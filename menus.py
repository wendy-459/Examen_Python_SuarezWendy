from definiciones import calcular_propina, calcular_total_propina, dividir_total

def menu_calculo_propina():
    while True:
        print("=================================================")
        print("  Cálculo de Propina")
        print("=================================================")
        try:
            total = float(input("Ingrese el monto total de la cuenta: $"))
            porcentaje = float(input("Ingrese el porcentaje de propina (por ejemplo: 15): "))
            propina = calcular_propina(total, porcentaje)
            total_a_pagar = calcular_total_con_propina(total, propina)
            print("=================================================")
            print(f"La propina calculada es: ${propina}.")
            print(f"El total a pagar es: ${total_pagar}.")
            print("==================================================")
            copiar = (input("¿Deseas calcular nuevamente? (si/no): ")).lower().strip()
            if copiar != "si":
                break
        except ValueError:
            print("Solo numeros.")

def menu_dividir_cuenta():
    while True:
        print("=================================================")
        print("  Dividir Cuenta entre Varias Persona")
        print("=================================================")
        try:
            total = float(input("Ingrese el monto total de la cuenta: $"))
            porcentaje = float(input("Ingrese el porcentaje de propina (por ejemplo: 15): "))
            personas = int(input("Ingrese el número de personas: "))
            
            propina = calcular_propina(total, porcentaje)
            total_a_pagar = calcular_total_con_propina(total, propina)
            monto_persona = dividir_total(total_pagar, personas)

            print("==================================================")
            print(f"La propina calculada es: ${propina}.")
            print(f"El total a pagar es: ${total_pagar}.")
            print(f"Monto por persona: ${monto_persona}.")
            print("==================================================")

            copiar = int(input("¿Deseas calcular nuevamente? (si/no): ")).strip().lower()
            if copiar != "si":
                break
        except ValueError:
            print("Solo numeros.")
