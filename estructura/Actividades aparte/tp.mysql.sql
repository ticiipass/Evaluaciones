CREATE DATABASE glosarioProgramacion;

CREATE TABLE operaciones(
id INT AUTO_INCREMENT PRIMARY KEY,
operacion VARCHAR (255) NOT NULL,
explicacion (255) NOT NULL,
ejemplo VARCHAR (255) NOT NULL
);

CREATE TABLE materias (
id INT AUTO_INCREMENT PRIMARY KEY,
matematica VARCHAR (255) NOT NULL,
lengua VARCHAR (255) NOT NULL,
programacion VARCHAR (255) NOT NULL,
foreign key (matematica) references operaciones (id) (
);