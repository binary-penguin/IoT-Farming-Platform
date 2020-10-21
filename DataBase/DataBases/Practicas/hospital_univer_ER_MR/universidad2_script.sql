-- Create database
CREATE DATABASE universidad2;

-- Create tables

CREATE TABLE Profesor(  clave       VARCHAR(7)  NOT NULL,
                        nombre      VARCHAR(20) NOT NULL,
                        domicilio   VARCHAR(15) NOT NULL,
                        salario     FLOAT       NOT NULL,
                        fecha_nac   DATE        NOT NULL,
                        n_depto     VARCHAR(7)  NOT NULL, -- Departamento(numero)
                        PRIMARY KEY (clave));
                        -- TEMPORARY DISABLED UNTIL ALL DEPTOS ARE DECLARED
--                  ALTER TABLE profesor ADD    FOREIGN KEY (n_depto) REFERENCES Departamento(numero));
    

CREATE TABLE Departamento(  numero      VARCHAR(7)  NOT NULL,
                            nombre      VARCHAR(20) NOT NULL,
                            claveP      VARCHAR(7)  NOT NULL, -- Profesor(clave)
                            fecha_ini   DATE        NOT NULL,
                            localidad   VARCHAR(15) NOT NULL,
                            PRIMARY KEY (numero),   
                            FOREIGN KEY (claveP) REFERENCES Profesor(clave));



CREATE TABLE Curso(         clave       VARCHAR(7)  NOT NULL,
                            nombre      VARCHAR(20) NOT NULL,
                            semestre    VARCHAR(1)  NOT NULL, 
                            n_depto     VARCHAR(7)  NOT NULL, -- Departamento(numero)
                            PRIMARY KEY (clave),   
                            FOREIGN KEY (n_depto) REFERENCES Departamento(numero));


CREATE TABLE Alumno(    matricula   VARCHAR(7)  NOT NULL,
                        nombre      VARCHAR(20) NOT NULL,
                        domicilio   VARCHAR(15) NOT NULL,
                        telefono    VARCHAR(15) NOT NULL,
                        carrera     VARCHAR(4)  NOT NULL,
                        PRIMARY KEY (matricula));

CREATE TABLE Cursa(     matri       VARCHAR(7)  NOT NULL, -- Alumno(matricula)
                        claveC      VARCHAR(7)  NOT NULL, -- Curso(clave)
                        grupo       VARCHAR(2)  NOT NULL,
                        salon       VARCHAR(2)  NOT NULL,
                        horario     VARCHAR(10) NOT NULL,
                        calif       FLOAT       NOT NULL,
                        PRIMARY KEY (matri, claveC),
                        FOREIGN KEY (matri) REFERENCES Alumno(matricula),
                        FOREIGN KEY (claveC) REFERENCES Curso(clave));

CREATE TABLE Imparte(   claveP      VARCHAR(7)  NOT NULL, -- Profesor(clave)
                        claveC      VARCHAR(7) NOT NULL,  -- Curso(clave)
                        grupo       VARCHAR(2)  NOT NULL,
                        salon       VARCHAR(2)  NOT NULL,
                        horario     VARCHAR(10) NOT NULL,
                        PRIMARY KEY (claveC, claveP, grupo),
                        FOREIGN KEY (claveC) REFERENCES Curso(clave), 
                        FOREIGN KEY (claveP) REFERENCES Profesor(clave));


CREATE TABLE Grado(     claveP      VARCHAR(7)  NOT NULL, -- Profesor(clave)
                        tipo        VARCHAR(20) NOT NULL,
                        universidad VARCHAR(15) NOT NULL,
                        fecha       DATE        NOT NULL,
                        PRIMARY KEY (claveP, tipo, universidad),
                        FOREIGN KEY (claveP) REFERENCES Profesor(clave));



                        