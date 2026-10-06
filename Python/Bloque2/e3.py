agenda = {"ana": 1234, "pepe": 2233, "juan": 3245, "gabriel": 5454, "alba": 5987}
select = 1
while select != 0:
    print("\nMenú:" \
    "\n1 - Mostrar agenda ordenada" \
    "\n2 - Buscar por nombre" \
    "\n3 - Añadir contacto" \
    "\n4 - Eliminar contacto" \
    "\n0 - Salir")
    
    select = int(input("Elige una opción: "))
    
    if select == 0 :
        print("Hasta luego")

    elif select == 1:
        print("\nAgenda:")
        ordenada = dict(sorted(agenda.items()))
        for nom, num in ordenada.items():
            print(f"{nom}: {num}")

    elif select == 2:
        busca = input("Buscar por: ")
        print(f"{agenda.get(busca.lower(), "Contacto no encontrado")}")

    elif select == 3:
        nombre = str(input("Nombre del contacto: ")).lower()
        numero = int(input("Número del contacto: "))
        if agenda.get(nombre) == None:
            agenda[nombre] = numero
            print(f"Contacto de {nombre} añadido con éxito")
        else:
            print("Nombre ya utilizado, inténtalo de nuevo")

    elif select == 4:
        n = str(input("Nombre del contacto: ")).lower()
        if agenda.get(n) == None:
            print("Error: contacto no existente")
        else:
            del agenda[n]
            print("Contacto eliminado con éxito")
            
    else:
        print("Opción inválida")