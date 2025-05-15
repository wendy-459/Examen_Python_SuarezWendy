from menus import menu_calculo_propina, menu_dividir_cuenta

def main():
    while True:
        print("=================================================")
        print("   SIMULADOR DE PROPINA                          ")
        print("=================================================")
        print("1. Calcular propina y total a pagar.")
        print("2. Calcular total a pagar dividido entre varias personas.")
        print("3. Salir.")
        print("=================================================")
        opcion = input("Por favor, elige una opción (1-3): ").strip()
        
        if not opcion.isdigit():
            
            print('Solo se permiten números, intente de nuevo.\n')
            continue

        if opcion == "1":   
            menu_calculo_propina()
        elif opcion == "2":
            menu_dividir_cuenta()
        elif opcion == "3":
            print("=================================================")
            print("¡Gracias por usar el Simulador de Propina!"       )
            print("=================================================")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")
            continue
        
if __name__ == "__main__":
    main()