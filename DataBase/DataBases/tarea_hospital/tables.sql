
-- Comments in MySQL!!
-- Create database
-- CREATE DATABASE hospital

-- Create tables
CREATE TABLE Doctor(clave		VARCHAR(7)	NOT NULL,
					nombre		VARCHAR(20)	NOT NULL,
					direccion	VARCHAR(15)	NOT NULL,
					telefono	VARCHAR(15)	NOT NULL,
					consultorio	VARCHAR(5)	NOT NULL,
					especialidad	VARCHAR(15)	NOT NULL,
					PRIMARY KEY(clave));

CREATE TABLE Paciente(	clave		VARCHAR(7)	NOT NULL,
						nombre		VARCHAR(20)	NOT NULL,
						direccion	VARCHAR(15)	NOT NULL,
						telefono	VARCHAR(15)	NOT NULL,
						PRIMARY KEY(clave));

CREATE TABLE Atiende(	claveD		VARCHAR(7)	NOT NULL,
						claveP		VARCHAR(7)	NOT NULL,
						fecha		DATE		NOT NULL,
						diagnostico	VARCHAR(20)	NOT NULL,
						tratamiento	VARCHAR(12)	NOT NULL,
						FOREIGN KEY(claveD) REFERENCES Doctor(clave),
						FOREIGN KEY(claveP) REFERENCES Paciente(clave),
						PRIMARY KEY(claveD, claveP, fecha));

CREATE TABLE Analisis(	claveP		VARCHAR(7)	NOT NULL,
						tipo		VARCHAR(15)	NOT NULL,
						fecha_aplic	DATE		NOT NULL,
						fecha_entrega	DATE		NOT NULL,
						descripcion	VARCHAR(15)	NOT NULL,
						FOREIGN KEY(claveP) REFERENCES Paciente(clave),
						PRIMARY KEY(claveP, tipo, fecha_aplic));



