prestamos = []
import utils
def menu_prestamos():
    while True:
        print("---Gestión de prestamos---")
        print("1: Registrar un prestamo")
        print("2: Devolver libro o eliminar un prestamo (por id)")
        print("3: Buscar prestamo de usuario")
        print("4: Mostrar todos los prestamos")
        print("5: Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            fecha = input("Introduce la fecha del prestamo: ")
            dni = input("Introduce el dni del prestamo: ")
            while utils.validar_dni_format(dni) == False:
                dni = input("Introduce el dni del prestamo: ")
            
            isbn = input("Introduce el isbn del prestamo: ")
            id = input("Introduce el id del prestamo: ")
            anadir_prestamo(fecha, dni, isbn, id)

        if opcion == "2":
            id = input("Introduce el id del prestamo que quieres eliminar: ")
            eliminar_prestamo(id)

        if opcion == "3":
            busqueda = input("Introduce la fecha, dni, isbn o id del prestamo que quieres buscar")
            resultados = buscar_prestamo(busqueda, busqueda, busqueda, busqueda)
            if resultados:
                print("Resultados de la búsqueda: ")
                for resultado in resultados:
                    print(f"Fecha: {resultado["fecha"]}, Dni: {resultado["dni"]}, Isbn: {resultado["isbn"]}, ID: {resultado["id"]}")
            else:
                print ("No se encontraron resultados")

        if opcion == "4":
            mostrar_prestamos()
        
        elif opcion == "5":
            break

def anadir_prestamo(f, d, isb, i):
    prestamo = {
        "fecha": f,
        "dni": d,
        "isbn": isb,
        "id": i
    }
    if buscar_prestamo(d, d, isb, i):
       print(f"prestamo ya existente: {prestamo}") 
    else:    
        prestamos.append(prestamo)
        print(f"prestamo añadido: {prestamo}")

def eliminar_prestamo(id): # un usuario puede tener mas de un prestamo, en este caso podria tener un isbn unico, pero tambien podria ser que guardaramos historial de los prestamos hechos ya finalizados por lo tanto habria varias entradas con igual isbn, mejor usar un id vinculante
    for prestamo in prestamos:
        if prestamo["id"] == id:
            prestamos.remove(prestamo)
            print(f"prestamo con id {id} borrado")
            return
    print("prestamo no encontrado")

def buscar_prestamo(fecha=None, dni=None, isbn=None, id=None): # Si no llega valor al param,tomara valor None
    resultados = []
    for prestamo in prestamos:
        if dni and dni.lower() == prestamo["dni"].lower():
            resultados.append(prestamo)
    return resultados

def mostrar_prestamos():
    if prestamos:
        print("prestamos registrados: ")
        for prestamo in prestamos:
            print(f"fecha: {prestamo["fecha"]}, dni: {prestamo["dni"]}, isbn: {prestamo["isbn"]}, id: {prestamo["id"]}")
    else:
        print("No hay prestamos ")