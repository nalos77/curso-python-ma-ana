# API REST (Servidor Web)  el proyecto final de curso de Python.

# Estructura Proyecto
/apirest_base/
    |------- /sql             ->  Scripts SQL para la estructura de la DB
    |------- app.py           ->  Punto de entrada de la apirest (lógica servidor web)
    |------- database.py      ->  Clase con lógica de interacción a MySQL
    |------- requirements.txt ->  Archivo que contiene todos los módulos necesarios para la app

## requirements.txt: El comando que ejecutamos para que lea todos los módulos (dependencias) de este archivo y los instale en nuestro proyecto:
```
pip install -r requirements.txt
```


# Crear entorno virtual y activarlo
```
python -m venv venv
```
```
venv\Scripts\activate
```

# PASOS DESARROLLO
1- Crear el archivo "sql/database.sql" que contiene la estructura de la base de datos en MySQL (DB relacional). Esta base de datos contiene tres tablas, tarjeta_pago, usuario y billete con campos diferentes y algunos compartidos con los que interactua la api rest.

2- Desarrollar la Clase "Database" en "/database.py":
    - Constructor: Crea la conexion a MySQL
    - 3 métodos: Que realizan las acciones de "CONSULTA", "EJECUCIÓN" y "CERRAR CONEXIÓN"

3- Desarrollar la API REST en "/app.py" 
    1- Añadir los imports que necesita este modulo
    2- Desarrollamos la Clase "ApiRestBase"
        1- Método que gestiona las cabeceras (informacion que viaja junto al paquete (request, response))
        2- Método que gestiona la peticion GET
        3- Método que gestiona la peticion POST
        4- Método que gestiona la peticion PUT
        5- Método que gestiona la peticion DELETE


# Peticiones CRUD (create/read/update/delete)
# GET: http://localhost:3000/tarjeta_pago -> Devuelve todos los datos de la tabla "tarjeta_pago" (cRud)
# GET: http://localhost:3000/usuario -> Devuelve todos los datos de la tabla "usuario" (cRud)
# GET: http://localhost:3000/billete -> Devuelve todos los datos de la tabla "billete" (cRud)
    - body: None

# POST: http://localhost:3000/tarjeta_pago -> Crea/inserta un dato (str) en la tabla "tarjeta_pago" (Crud)
    - body (json): { "num_tarjeta": "dato_tipo_texto",
    "fecha_cad": "dato_tipo_texto",
    "cvc": "dato_tipo_texto" } 
# POST: http://localhost:3000/usuario -> Crea/inserta un dato (str) en la tabla "usuario" (Crud)
    - body (json): { "id": "",
    "dni": "dato_tipo_texto",
    "password": "dato_tipo_texto"
    "num_tarjeta": "dato_tipo_texto"
     } 
# POST: http://localhost:3000/billete -> Crea/inserta un dato (str) en la tabla "billete" (Crud)
    - body (json): { "id_billete": "dato_tipo_texto",
    "zona": "dato_tipo_texto",
    "usos": "dato_tipo_texto",
    "id_usuario": "dato_tipo_texto"
     } 

# PUT: http://localhost:3000/usuario -> Actualiza un dato (str) en la tabla "usuario" (crUd)
    - body (json): { id:"id_del_dato_a_act", "mensaje": "dato_tipo_texto_act", }

# DELETE: http://localhost:3000/tarjeta_pago -> Borra un dato (str) en la tabla "tarjeta_pago" (crUd)
# DELETE: http://localhost:3000/usuario -> Borra un dato (str) en la tabla "usuario" (crUd)
# DELETE: http://localhost:3000/billete -> Borra un dato (str) en la tabla "billete" (crUd)
    - body (json): { id:"id_del_dato_a_borrar" } 

git config --global user.name "nalos77"
git config --global user.email "nalos77@gmail.com"