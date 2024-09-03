import time

# Base de datos simulada
users_passwords = {}

def bienvenida():
    print("======================================")
    print("    BIENVENIDO AL SISTEMA DE LOGIN    ")
    print("======================================")
    time.sleep(1)

def user_registration():
    while True:
        # Solicitar nombre de usuario
        username = input("\nPor favor ingrese nombre de usuario deseado: ")

        if username in users_passwords:
            print("El nombre de usuario ya existe. Por favor, elija otro.")
        else:
            while True:
                # Solicitar contraseña
                password = input("\nPor favor ingrese su contraseña: ")
                password_bis = input("\nPor favor ingrese su contraseña nuevamente: ")

                if password == password_bis:
                    users_passwords[username] = password
                    print("\nUsuario y contraseña generados correctamente.")
                    break
                else:
                    print("\nLa verificación de contraseña no coincide. Por favor intente nuevamente.")
            break

def user_list():
    if users_passwords:
        print("\nUsuarios registrados actualmente en la base de datos:\n")
        for username in users_passwords:
            print(f"Usuario: {username}\n")
    else:
        print("\nNo existen usuarios registrados.")

def login():
    while True:
        # Solicitar nombre de usuario para iniciar sesión
        username = input("\nPara ingresar, ingrese su nombre de usuario: ")

        if username not in users_passwords:
            print("El nombre de usuario no existe. Por favor, ingrese un nombre de usuario válido.")
            continue

        while True:
            # Solicitar contraseña
            password = input("Ingrese su contraseña: ")
            if users_passwords[username] == password:
                print(f"Inicio de sesión exitoso para el usuario: {username}.")
                break
            else:
                print("Contraseña incorrecta. Por favor, intente nuevamente.")
        break

def main():
    bienvenida()  # Mostrar mensaje de bienvenida
    while True:
        print("\n\nBIENVENIDO AL SISTEMA.\n")
        print("¿Desea registrarse, iniciar sesión, o ver los usuarios registrados?\n")
        print("Elija la opción deseada: \n")
        print("Registrarse: (1)\n")
        print("Iniciar sesión: (2)\n")
        print("Ver los usuarios registrados: (3)\n")

        # Solicitar opción al usuario
        option = input()

        if option == "1":
            user_registration()
        elif option == "2":
            login()
        elif option == "3":
            user_list()
        else:
            print("Opción no válida. Por favor, elija nuevamente.\n")

# Ejecutar el programa
if __name__ == "__main__":
    main()