import libros
import usuarios
import prestamos
import utils
def menu_principal():
    while True:
        print("---Gestión Biblioteca---")
        print("1: Gestión de libros")
        print("2: Gestión de usuarios")
        print("3: Gestión de préstamos")
        print("4: Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            libros.menu_libros()
        elif opcion == "2":
            # TODO:  Mismo metodos que "libros", validar que el dni del usuario no este registrado previamente en la DB
            usuarios.menu_usuarios()
        elif opcion == "3":
            prestamos.menu_prestamos()

        elif opcion == "4":
           print("Gracias por utilizar nuestra app")
           break
        else:
            print("Opción no válida. Inténtalo otra vez")


menu_principal()