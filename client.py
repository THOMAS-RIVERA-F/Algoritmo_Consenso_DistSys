import proxy  # Asegúrate de tener el archivo proxy.py implementado correctamente

def menu():
    print("\n--- Menú de Operaciones ---")
    print("1. Escribir en la base de datos (Write)")
    print("2. Leer de la base de datos (Read)")
    print("3. Salir")
    opcion = input("Elige una opción (1/2/3): ")
    return opcion

if __name__ == "__main__":
    p = proxy.Proxy()  # Instanciar la conexión con el proxy
    
    while True:
        # Mostrar el menú y solicitar opción del usuario
        opcion = menu()
        
        if opcion == '1':
            # Opción de escritura
            clave = input("Introduce la clave para escribir: ")
            valor = input("Introduce el valor para escribir: ")
            success = p.write(clave, valor)  # Llamada a la operación write en el proxy
            if success:
                print(f"Escritura exitosa: {clave} -> {valor}")
            else:
                print("Error en la operación de escritura.")
        
        elif opcion == '2':
            # Opción de lectura
            clave = input("Introduce la clave para leer: ")
            value = p.read(clave)  # Llamada a la operación read en el proxy
            if value is not None:
                print(f"Lectura exitosa: {clave} -> {value}")
            else:
                print(f"No se encontró el valor asociado a la clave: {clave}")
        
        elif opcion == '3':
            # Opción para salir del bucle
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción correcta.")

