create database glosario1; 
CREATE TABLE usuarios ( 
id INT auto_increment PRIMARY KEY,
username VARCHAR (255) NOT NULL, 
PASSWORD VARCHAR (255) NOT NULL,
rango VARCHAR (255) NOT NULL; 

CREATE TABLE palabras_reservadas (
id INT auto_increment PRIMARY KEY, 
palabra VARCHAR (255) NOT NULL, 
lenguaje VARCHAR (255) NOT NULL, 
significado varchar (255) NOT NULL, 
ejemplo VARCHAR (255) NOT NULL; 

CREATE TABLE palabras_reservadas ( 
id INT auto_increment PRIMARY KEY, 
nombre VARCHAr (255) NOT NULL;


