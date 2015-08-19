
import sqlite3
import directORM

class Transito_actual:
    def __init__(self):

        self.id_transito = -1
        self.num_albaran = ''
        self.mat_cabina = ''
        self.mat_remolque = ''
        self.fecha_entrada = ''
        self.fecha_salida = ''
        self.bruto = 0
        self.tara = 0
        self.neto = 0
        self.iva_aplicable = ''
        self.importe_final = ''
        self.importe_producto = ''
        self.id_producto = 0
        self.id_cliente = 0
        self.id_proveedor = 0
        self.id_agencia = 0
        self.id_poseedor = 0
        self.id_conductor = 0
        self.origen = ''
        self.destino = ''

class TbTransito_actuales:
    INSERT = '''
        insert into Transito_actuales
        ( num_albaran, mat_cabina, mat_remolque, fecha_entrada, fecha_salida, bruto, tara, neto, iva_aplicable, importe_final, importe_producto, id_producto, id_cliente, id_proveedor, id_agencia, id_poseedor, id_conductor, origen, destino)
        values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        '''
    DELETE = 'delete from Transito_actuales where id_transito = ?'
    SELECT = 'select * from Transito_actuales'
    UPDATE = '''
        update Transito_actuales set  
        num_albaran = ?,
        mat_cabina = ?,
        mat_remolque = ?,
        fecha_entrada = ?,
        fecha_salida = ?,
        bruto = ?,
        tara = ?,
        neto = ?,
        iva_aplicable = ?,
        importe_final = ?,
        importe_producto = ?,
        id_producto = ?,
        id_cliente = ?,
        id_proveedor = ?,
        id_agencia = ?,
        id_poseedor = ?,
        id_conductor = ?,
        origen = ?,
        destino = ?
        where  id_transito = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, transito_actual ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (transito_actual.id_transito))

    def get_transito_actual(self, id_transito=None):
        sql = self.SELECT + " where id_transito=" + str(id_transito) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, transito_actual=None):
        if transito_actual is not None:
            if self.get_transito_actual(transito_actual.id_transito) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    transito_actual.num_albaran,
                    transito_actual.mat_cabina,
                    transito_actual.mat_remolque,
                    transito_actual.fecha_entrada,
                    transito_actual.fecha_salida,
                    transito_actual.bruto,
                    transito_actual.tara,
                    transito_actual.neto,
                    transito_actual.iva_aplicable,
                    transito_actual.importe_final,
                    transito_actual.importe_producto,
                    transito_actual.id_producto,
                    transito_actual.id_cliente,
                    transito_actual.id_proveedor,
                    transito_actual.id_agencia,
                    transito_actual.id_poseedor,
                    transito_actual.id_conductor,
                    transito_actual.origen,
                    transito_actual.destino))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    transito_actual.num_albaran,
                    transito_actual.mat_cabina,
                    transito_actual.mat_remolque,
                    transito_actual.fecha_entrada,
                    transito_actual.fecha_salida,
                    transito_actual.bruto,
                    transito_actual.tara,
                    transito_actual.neto,
                    transito_actual.iva_aplicable,
                    transito_actual.importe_final,
                    transito_actual.importe_producto,
                    transito_actual.id_producto,
                    transito_actual.id_cliente,
                    transito_actual.id_proveedor,
                    transito_actual.id_agencia,
                    transito_actual.id_poseedor,
                    transito_actual.id_conductor,
                    transito_actual.origen,
                    transito_actual.destino,
                    transito_actual.id_transito))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Transito_actual()
            o.id_transito = fila['id_transito']
            o.num_albaran = fila['num_albaran']
            o.mat_cabina = fila['mat_cabina']
            o.mat_remolque = fila['mat_remolque']
            o.fecha_entrada = fila['fecha_entrada']
            o.fecha_salida = fila['fecha_salida']
            o.bruto = fila['bruto']
            o.tara = fila['tara']
            o.neto = fila['neto']
            o.iva_aplicable = fila['iva_aplicable']
            o.importe_final = fila['importe_final']
            o.importe_producto = fila['importe_producto']
            o.id_producto = fila['id_producto']
            o.id_cliente = fila['id_cliente']
            o.id_proveedor = fila['id_proveedor']
            o.id_agencia = fila['id_agencia']
            o.id_poseedor = fila['id_poseedor']
            o.id_conductor = fila['id_conductor']
            o.origen = fila['origen']
            o.destino = fila['destino']
            return o

    def get_transito_actuales(self, filtro=None):
        if filtro is None:
            sql = self.SELECT
        else: 
            sql = self.SELECT + " where " + filtro
        filas = self.gestorDB.consultaSQL(sql)
        objetos = list()
        for fila in filas:
            o = self.mapear_objeto(fila)
            objetos.append(o)

        return objetos




