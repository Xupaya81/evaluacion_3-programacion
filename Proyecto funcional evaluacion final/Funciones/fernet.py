# Funciones/encryption.py
from cryptography.fernet import Fernet

def encriptar_texto():
    # Mover la generación de la clave dentro de la opción de cifrado
    clave = Fernet.generate_key()
    f = Fernet(clave)
    mensaje_cifrado = None

    print("\n--- Menú de Encriptación ---")
    while True:
        print("1. Ingresar un nuevo mensaje")
        print("2. Desencriptar el mensaje")
        print("3. Salir a menu API")
        opcion = input("Selecciona una opción (1, 2 o 3): ")

        if opcion == "1":
            mensaje = input('''Ingresa una palabra para cifrar: 
                            ''').encode()
            mensaje_cifrado = f.encrypt(mensaje)

        elif opcion == "2":
            if mensaje_cifrado is None:
                print("No hay ningún mensaje cifrado. Por favor, selecciona la opción 1 para cifrar un mensaje primero.")
            else:
                mensaje_descifrado = f.decrypt(mensaje_cifrado)
                print(f"Mensaje desencriptado: {mensaje_descifrado.decode()}")
        elif opcion == "3":
            print("Saliendo del menú de encriptación.")
            break
        else:
            print('''Opción inválida, por favor selecciona 1, 2 o 3.
                  ''')
