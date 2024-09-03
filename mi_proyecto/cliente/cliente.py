import time

# Base de dados simulada com correos eletrônicos
users_data = {}

def bienvenida():
    print("======================================")
    print("    BIENVENIDO AL SISTEMA DE LOGIN    ")
    print("======================================")
    time.sleep(1)

def user_registration():
    while True:
        # Solicitar nome de usuário
        username = input("\nPor favor, ingrese el nombre de usuario deseado: ")

        if username in users_data:
            print("El nombre de usuario ya existe. Por favor, elija otro.")
        else:
            while True:
                # Solicitar senha
                password = input("\nPor favor, ingrese su contraseña: ")
                password_bis = input("\nPor favor, ingrese su contraseña nuevamente: ")

                if password == password_bis:
                    # Solicitar correo electrónico
                    email = input("\nPor favor, ingrese su correo electrónico: ")
                    users_data[username] = {'password': password, 'email': email}
                    print("\nUsuario y contraseña generados correctamente.")
                    break
                else:
                    print("\nLa verificación de contraseña no coincide. Por favor intente nuevamente.")
            break

def user_list():
    if users_data:
        print("\nUsuarios registrados actualmente en la base de datos:\n")
        for username, data in users_data.items():
            print(f"Usuario: {username} - Email: {data['email']}")
    else:
        print("\nNo existen usuarios registrados.")

def login():
    while True:
        # Solicitar nome de usuário para iniciar sesión
        username = input("\nPara ingresar, ingrese su nombre de usuario: ")

        if username not in users_data:
            print("El nombre de usuario no existe. Por favor, ingrese un nombre de usuario válido.")
            continue

        while True:
            # Solicitar senha
            password = input("Ingrese su contraseña: ")
            if users_data[username]['password'] == password:
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
