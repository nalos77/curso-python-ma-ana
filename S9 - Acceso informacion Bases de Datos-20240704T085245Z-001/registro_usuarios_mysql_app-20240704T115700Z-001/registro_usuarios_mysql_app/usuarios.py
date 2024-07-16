import utils

class Usuario:
    # constructor
    def __init__(self, dni, nombre, email, password):
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.password = password

class GestionUsuarios:
    def anadir_usuario(self):
        dni = input("Introduce tu dni: ")
        nombre = input("Introduce tu nombre: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")
        # TODO: validar estos datos
        usuario = Usuario(dni, nombre, email, password)
        utils.set_data_mysql(usuario)
        print("Usuario insertado con éxito!")

    def borrar_usuario(self):
        dni = input("Introduce el dni del usuario: ")
        if utils.delete_data_mysql(dni):
            print(f"Usuario con dni {dni} borrado")
        else:
            print(f"Usuario con dni {dni} no registrado")
        
    def mostrar_usuario(self):
        dni = input("Introduce el dni del usuario: ")
        if utils.get_one_data_mysql(dni):
            usuario = utils.get_one_data_mysql(dni)
            print(usuario)
        else:
            print("No se ha encontrado el usuario con dni " + dni)
    
    def mostrar_usuarios(self):
        if not utils.get_data_mysql():
            print("No hay usuarios registrados")
        else:
            print(utils.get_data_mysql())

