while True:
    try:
        # Mostrar menu
        print("Selecciona la opcion que deseas realizar")
        print("1- Calcular comision")
        print("2- Ver recibos de sueldo de vendedores (Admin)")
        print("3- Salir")

        opc = int(input("Opcion: "))

        # Realizar accion del menu
        match opc:
            case 1:
                print("|------------------|")
                print("Calcular comision")
                print("|------------------|")

            case 2:
                print("|------------------|")
                print("Ver recibos")
                print("|------------------|")

            case 3:
                print("|------------------|")
                print("Saliendo...")
                print("|------------------|")
                break

            case _:
                print("Error: Debes ingresar una opcion valida (1, 2 o 3).")

    except ValueError:
        print("Error: Debes ingresar un numero entero.")
        print("Error: Debes ingresar una opcion valida (1, 2 o 3).")
