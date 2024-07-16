def conexion_a_mysql():
    import mysql.connector
    connex = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="app"
    )
    # mensaje de error en la conex MySQL
    if connex.is_connected():
        return connex
    else:
        print("Ha habido un error en la conex. a MySQL")
    
def set_data_mysql(usuarioObj):
    connex = conexion_a_mysql()
    cursor = connex.cursor()
    # Evitar inyeccion SQL (seguridad)
    query = "insert into usuarios values (null, %s, %s, %s, %s)"
    cursor.execute(query, (usuarioObj.dni, usuarioObj.nombre, usuarioObj.email, usuarioObj.password))
    connex.commit()
    cursor.close()

def get_data_mysql():
    connex = conexion_a_mysql()
    cursor = connex.cursor()
    query = "select * from usuarios"
    cursor.execute(query)
    usuarios = cursor.fetchall()
    connex.close()
    return usuarios


# CONSULTAS FALTAN
# Borrar un usuario mediante DNI
def delete_data_mysql(dni):
    if get_one_data_mysql(dni):
        connex = conexion_a_mysql()
        cursor = connex.cursor()
        query = "delete from usuarios where dni = %s"
        cursor.execute(query, (dni,))
        usuarios = cursor.fetchall()
        connex.close()
    return True
# delete from tu_tabla where dni = dni_que_pone_el_usuario
# query = delete from tu_tabla where dni = %s
# cursor.execute(query, (dni,))

# Buscar un usuario por DNI
def get_one_data_mysql(dni):
    connex = conexion_a_mysql()
    cursor = connex.cursor()
    query = "select * where dni = %s from usuarios"
    cursor.execute(query, (dni,))
    usuario = cursor.fetchall()
    connex.close()
    return usuario
# select * from tu_tabla where dni = dni_que_pone_el_usuario
