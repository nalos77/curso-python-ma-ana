# importar modulos necesarios
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, bcrypt
# modulo database
from database import Database

class ApiRestBase(BaseHTTPRequestHandler):
    # metodo que gestiona las cabeceras  
    def set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    
    def do_GET(self):
        db = Database() # instancia
        if self.path == "/usuario":
            resultado = db.query("select * from usuario")
            resultadoFormat = [
                {
                    "id": mensaje[0],
                    "dni": mensaje[1],
                    "password": mensaje[2],
                    "num_tarjeta": mensaje[3],
                }
                for mensaje in resultado 
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultadoFormat).encode("utf-8"))
        elif self.path == "/tarjeta_pago":
            resultado = db.query("select * from tarjeta_pago")
            resultadoFormat = [
                {
                    "num_tarjeta": mensaje[0],
                    "fecha_cad": mensaje[1],
                    "cvc": mensaje[2],
                }
                for mensaje in resultado 
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultadoFormat).encode("utf-8"))
        elif self.path == "/billete":
            resultado = db.query("select * from billete")
            resultadoFormat = [
                {
                    "id_billete": mensaje[0],
                    "zona": mensaje[1],
                    "usos": mensaje[2],
                    "id_usuario": mensaje[3],
                }
                for mensaje in resultado 
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultadoFormat).encode("utf-8"))
        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/usuario":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

            Passhashed = bcrypt.hashpw(mensaje["password"].encode("utf-8"), bcrypt.gensalt())

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            db.execute("insert into usuario values (default, %s, %s, %s)", (mensaje["dni"], Passhashed, mensaje["num_tarjeta"]))
            db.close()
            self.set_headers(201) # envio un 201 (recurso creado) al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            response = json.dumps({"mensaje": "Dato almacenado en MySQL ok!"}).encode("utf-8")
            self.wfile.write(response)

        elif self.path == "/tarjeta_pago":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            db.execute("insert into tarjeta_pago values (%s, %s, %s)", (mensaje["num_tarjeta"], mensaje["fecha_cad"],mensaje["cvc"]))
            db.close()
            self.set_headers(201) # envio un 201 (recurso creado) al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            response = json.dumps({"mensaje": "Dato almacenado en MySQL ok!"}).encode("utf-8")
            self.wfile.write(response)

        elif self.path == "/billete":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            print(post_data)
            mensaje = json.loads(post_data) 

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            db.execute("insert into billete values (%s, %s, %s, %s)", (mensaje["id_billete"], mensaje["zona"],mensaje["usos"],mensaje["id_usuario"]))
            db.close()
            self.set_headers(201) # envio un 201 (recurso creado) al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            response = json.dumps({"mensaje": "Dato almacenado en MySQL ok!"}).encode("utf-8")
            self.wfile.write(response) 

        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))
    
    def do_PUT(self):
        if self.path == "/usuario":
        # Recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

            # Hash de la contraseña
            Passhashed = bcrypt.hashpw(mensaje["password"].encode("utf-8"), bcrypt.gensalt())

            # Instancia a Database
            db = Database()

            # Llamamos al método "execute" con el formato de consulta que evita inyección de SQL
            rows = db.execute("UPDATE usuario SET dni = %s, password = %s, num_tarjeta = %s WHERE id = %s", (mensaje["dni"], Passhashed, mensaje["num_tarjeta"], mensaje["id"]))
            db.close()

        if rows > 0:
            self.set_headers(200)  # Envío un 200 (OK) al método de cabeceras
            # Devolvemos un mensaje en formato JSON al cliente
            response = json.dumps({"mensaje": "Dato actualizado ok!"}).encode("utf-8")
            self.wfile.write(response)
        else:
            self.set_headers(404)  # Envío un 404 (no encontró ID)
            self.wfile.write(json.dumps({"error": "Usuario no encontrado"}).encode("utf-8"))
            
    def do_DELETE(self):
        if self.path == "/usuario":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("delete from usuario where id = %s", (mensaje["id"],))
            db.close()
            if rows > 0:
                self.set_headers(200) # envio un 201 (recurso creado) al metodo de cabeceras
                # devolvemos un mensaje en formato JSON al cliente
                response = json.dumps({"mensaje": "Dato borrado ok!"}).encode("utf-8")
                self.wfile.write(response)
            else: 
                self.set_headers(404) # envio un 404 (no encontro ID)
                self.wfile.write(json.dumps({"error": "Mensaje no encontrado"}).encode("utf-8"))
        
        elif self.path == "/tarjeta_pago":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("delete from tarjeta_pago where num_tarjeta = %s", (mensaje["num_tarjeta"],))
            db.close()
            if rows > 0:
                self.set_headers(200) # envio un 201 (recurso creado) al metodo de cabeceras
                # devolvemos un mensaje en formato JSON al cliente
                response = json.dumps({"mensaje": "Dato borrado ok!"}).encode("utf-8")
                self.wfile.write(response)
            else: 
                self.set_headers(404) # envio un 404 (no encontro ID)
                self.wfile.write(json.dumps({"error": "Mensaje no encontrado"}).encode("utf-8"))
        
        elif self.path == "/billete":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("delete from billete where id_billete = %s", (mensaje["id_billete"],))
            db.close()
            if rows > 0:
                self.set_headers(200) # envio un 201 (recurso creado) al metodo de cabeceras
                # devolvemos un mensaje en formato JSON al cliente
                response = json.dumps({"mensaje": "Dato borrado ok!"}).encode("utf-8")
                self.wfile.write(response)
            else: 
                self.set_headers(404) # envio un 404 (no encontro ID)
                self.wfile.write(json.dumps({"error": "Mensaje no encontrado"}).encode("utf-8"))
        
        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))


def run(server_class=HTTPServer, handle_class=ApiRestBase, port=3000):
    server_address = ("localhost", port)
    httpd = server_class(server_address, handle_class)
    print(f"ApiRest escuchando por el puerto {port}")
    httpd.serve_forever()

run()




