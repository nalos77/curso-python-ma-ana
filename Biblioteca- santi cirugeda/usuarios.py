usuarios = []

def menu_usuarios():
    while True:
        print("---Gestión de Usuarios---")
        print("1: Añadir un usuario")
        print("2: Eliminar un usuario (por Dni o mail)")
        print("3: Buscar usuario")
        print("4: Mostrar todos los usuarios")
        print("5: Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del usuario: ")
            dni = input("Introduce el dni del usuario: ")
            mail = input("Introduce el mail del usuario: ")
            genero = input("Introduce el genero del usuario: ")
            anadir_usuario(nombre, dni, mail, genero)

        if opcion == "2":
            dni_mail = input("Introduce el mail o dni del usuario que quieres eliminar: ")
            eliminar_usuario(dni_mail)

        if opcion == "3":
            busqueda = input("Introduce el nombre, dni, mail o genero del usuario que quieres buscar")
            resultados = buscar_usuario(busqueda, busqueda, busqueda, busqueda)
            if resultados:
                print("Resultados de la búsqueda: ")
                for resultado in resultados:
                    print(f"Nombre: {resultado["nombre"]}, Dni: {resultado["dni"]}, Mail: {resultado["mail"]}, Género: {resultado["genero"]}")
            else:
                print ("No se encontraron resultados")

        if opcion == "4":
            mostrar_usuarios()
        
        elif opcion == "5":
            break

def anadir_usuario(n, d, m, g):
    usuario = {
        "nombre": n,
        "dni": d,
        "mail": m,
        "genero": g
    }
    if buscar_usuario(d, d, m, m):
       print(f"Usuario ya existente: {usuario}") 
    else:    
        usuarios.append(usuario)
        print(f"Usuario añadido: {usuario}")

def eliminar_usuario(dni_mail):
    for usuario in usuarios:
        if usuario["dni"] == dni_mail or usuario["mail"] == dni_mail :
            usuarios.remove(usuario)
            print(f"usuario con mail o dni {dni_mail} borrado")
            return
    print("usuario no encontrado")

def buscar_usuario(nombre=None, dni=None, mail=None, genero=None): # Si no llega valor al param, toma el valor None
    resultados = []
    for usuario in usuarios:
        if nombre and nombre.lower() == usuario["nombre"].lower():
            resultados.append(usuario)
        elif dni and dni.lower() == usuario["dni"].lower():
            resultados.append(usuario)
        elif mail and mail.lower() == usuario["mail"].lower():
            resultados.append(usuario)
    return resultados

def mostrar_usuarios():
    if usuarios:
        print("Usuarios registrados: ")
        for usuario in usuarios:
            print(f"Nombre: {usuario["nombre"]}, dni: {usuario["dni"]}, mail: {usuario["mail"]}, Género: {usuario["genero"]}")
    else:
        print("No hay usuarios ")