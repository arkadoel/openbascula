PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
/*
	Archivo generado por directORM
	Fecha: Martes, 2015-08-18 20:07:23
*/

DROP TABLE IF EXISTS "Transito_actuales";
CREATE TABLE "Transito_actuales" (
    "id_transito" INTEGER PRIMARY KEY AUTOINCREMENT,
    "num_albaran" VARCHAR,
    "mat_cabina" VARCHAR,
    "mat_remolque" VARCHAR,
    "fecha_entrada" DATE,
    "fecha_salida" DATE,
    "bruto" INTEGER,
    "tara" INTEGER,
    "neto" INTEGER,
    "iva_aplicable" VARCHAR,
    "importe_final" VARCHAR,
    "importe_producto" VARCHAR,
    "id_producto" INTEGER,
    "id_cliente" INTEGER,
    "id_proveedor" INTEGER,
    "id_agencia" INTEGER,
    "id_poseedor" INTEGER,
    "id_conductor" INTEGER,
    "origen" VARCHAR,
    "destino" VARCHAR
);

DROP TABLE IF EXISTS "Vehiculos";
CREATE TABLE "Vehiculos" (
    "id_vehiculo" INTEGER PRIMARY KEY AUTOINCREMENT,
    "matricula" VARCHAR,
    "id_empresa" INTEGER,
    "id_conductor" INTEGER,
    "fecha_alta" DATE,
    "fecha_baja" DATE
);

DROP TABLE IF EXISTS "Productos";
CREATE TABLE "Productos" (
    "id_producto" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nombre" VARCHAR,
    "descripcion" VARCHAR,
    "precio" REAL,
    "iva_aplicado" INTEGER,
    "tipo_material" VARCHAR,
    "codigo_contable" VARCHAR,
    "es_tarifa_plana" BOOL
);

DROP TABLE IF EXISTS "Usuarios";
CREATE TABLE "Usuarios" (
    "login_name" VARCHAR KEY,
    "password" VARCHAR,
    "real_name" VARCHAR,
    "email" VARCHAR,
    "permiso" VARCHAR
);

DROP TABLE IF EXISTS "Historicos";
CREATE TABLE "Historicos" (
    "id_historico" INTEGER PRIMARY KEY AUTOINCREMENT,
    "num_albaran" VARCHAR,
    "mat_cabina" VARCHAR,
    "mat_remolque" VARCHAR,
    "fecha_entrada" DATE,
    "fecha_salida" DATE,
    "bruto" INTEGER,
    "tara" INTEGER,
    "neto" INTEGER,
    "origen" VARCHAR,
    "destino" VARCHAR,
    "forma_pago" VARCHAR,
    "iva_aplicable" VARCHAR,
    "importe_final" VARCHAR,
    "importe_sin_iva" VARCHAR,
    "importe_producto" VARCHAR,
    "nombre_producto" INTEGER,
    "tipo_material" VARCHAR,
    "cod_conta_prod" INTEGER,
    "razon_social_cliente" VARCHAR,
    "cif_cliente" VARCHAR,
    "direccion_cliente" VARCHAR,
    "tlf_cliente" VARCHAR,
    "ubicacion_cliente" VARCHAR,
    "cod_conta_cliente" VARCHAR,
    "razon_social_proveedor" VARCHAR,
    "cif_proveedor" VARCHAR,
    "direccion_proveedor" VARCHAR,
    "tlf_proveedor" VARCHAR,
    "ubicacion_proveedor" VARCHAR,
    "cod_conta_proveedor" VARCHAR,
    "razon_social_agencia" VARCHAR,
    "cif_agencia" VARCHAR,
    "direccion_agencia" VARCHAR,
    "tlf_agencia" VARCHAR,
    "ubicacion_agencia" VARCHAR,
    "cod_conta_agencia" VARCHAR,
    "razon_social_poseedor" VARCHAR,
    "cif_poseedor" VARCHAR,
    "direccion_poseedor" VARCHAR,
    "tlf_poseedor" VARCHAR,
    "ubicacion_poseedor" VARCHAR,
    "cod_conta_poseedor" VARCHAR,
    "nombre_conductor" VARCHAR,
    "nif_conductor" VARCHAR,
    "direccion_conductor" VARCHAR,
    "tlf_conductor" VARCHAR,
    "ubicacion_conductor" VARCHAR
);

DROP TABLE IF EXISTS "Empresas";
CREATE TABLE "Empresas" (
    "id_empresa" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nombre" VARCHAR,
    "razon_social" VARCHAR,
    "cif" VARCHAR,
    "direccion" VARCHAR,
    "localidad" VARCHAR,
    "provincia" VARCHAR,
    "telefono" VARCHAR,
    "email" VARCHAR,
    "cuenta_bancaria" VARCHAR,
    "forma_de_pago" VARCHAR,
    "codigo_contable" VARCHAR
);

DROP TABLE IF EXISTS "Conductores";
CREATE TABLE "Conductores" (
    "id_conductor" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_empresa" INTEGER,
    "fecha_alta" DATE,
    "fecha_baja" DATE,
    "nombre" VARCHAR,
    "apellidos" VARCHAR,
    "nif" VARCHAR,
    "direccion" VARCHAR,
    "localidad" VARCHAR,
    "provincia" VARCHAR,
    "telefono" VARCHAR,
    "email" VARCHAR
);

DROP TABLE IF EXISTS "Configuraciones";
CREATE TABLE "Configuraciones" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "parametro" VARCHAR,
    "valor" VARCHAR
);


COMMIT;