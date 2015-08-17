PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
/*
	Archivo generado por directORM
	Fecha: Lunes, 2015-08-17 16:14:11
*/

DROP TABLE IF EXISTS "Vehiculos";
CREATE TABLE "Vehiculos" (
    "idVehiculo" INTEGER PRIMARY KEY AUTOINCREMENT,
    "matricula" VARCHAR,
    "id_empresa" INTEGER,
    "fecha_alta" DATE,
    "fecha_baja" DATE
);

DROP TABLE IF EXISTS "Usuarios";
CREATE TABLE "Usuarios" (
    "loginName" VARCHAR KEY,
    "password" VARCHAR,
    "real_name" VARCHAR,
    "email" VARCHAR,
    "permiso" VARCHAR
);

DROP TABLE IF EXISTS "ConfiguracionAppes";
CREATE TABLE "ConfiguracionAppes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "parametro" VARCHAR,
    "valor" VARCHAR
);

DROP TABLE IF EXISTS "Empresas";
CREATE TABLE "Empresas" (
    "idEmpresa" INTEGER PRIMARY KEY AUTOINCREMENT,
    "Nombre" VARCHAR,
    "RazonSocial" VARCHAR,
    "CIF" VARCHAR,
    "Direccion" VARCHAR,
    "Localidad" VARCHAR,
    "Provincia" VARCHAR,
    "Telefono" VARCHAR,
    "Email" VARCHAR,
    "Cuenta_bancaria" VARCHAR,
    "Forma_de_pago" VARCHAR,
    "Codigo_contabilidad" VARCHAR
);


COMMIT;