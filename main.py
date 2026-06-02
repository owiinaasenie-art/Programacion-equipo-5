while True:
    try:
        # Mostrar menu
        print("|---------------------------------------|")
        print("Selecciona la opcion que deseas realizar")
        print("|---------------------------------------|")
        print("1- Calcular comision")
        print("2- Ver recibos de sueldo de vendedores (Admin)")
        print("3- Salir")
        opc = int(input("Opcion: "))

        # Realizar accion del menu
        match opc:
            case 1:
                print("|------------------|")
                print("calcular comision")
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
                print("|------------------|")
                print("Error: Debes ingresar una opcion valida (1, 2 o 3)")
                print("|------------------|")

    except ValueError:
        print("Error: No se permiten letras ni numeros decimales.")
        print("Por favor, ingresa un numero entero valido.")
