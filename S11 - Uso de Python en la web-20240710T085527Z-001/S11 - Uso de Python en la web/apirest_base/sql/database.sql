DROP DATABASE IF EXISTS apirest_base; -- borra DB si existe
CREATE DATABASE apirest_base; -- crea DB 
USE apirest_base; -- selecciona DB

-- crea la tabla "tarjeta_pago"
CREATE TABLE tarjeta_pago (
    num_tarjeta INT PRIMARY KEY,
    fecha_cad DATE,
    cvc INT
);

-- crea la tabla "usuario"
CREATE TABLE usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    dni CHAR(9),
    password VARCHAR(255),
    num_tarjeta INT UNIQUE,
    FOREIGN KEY (num_tarjeta) REFERENCES tarjeta_pago(num_tarjeta)
);

-- crea la tabla "billete"
CREATE TABLE billete (
    id_billete INT PRIMARY KEY AUTO_INCREMENT,
    zona INT,
    usos INT,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);
