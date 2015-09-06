
import sqlite3
import directORM

class Historico:
    def __init__(self):

        self.id_historico = -1
        self.num_albaran = ''
        self.mat_cabina = ''
        self.mat_remolque = ''
        self.fecha_entrada = ''
        self.fecha_salida = ''
        self.bruto = 0
        self.tara = 0
        self.neto = 0
        self.origen = ''
        self.destino = ''
        self.forma_pago = ''
        self.iva_aplicable = ''
        self.importe_final = ''
        self.importe_sin_iva = ''
        self.importe_producto = ''
        self.nombre_producto = ''
        self.tipo_material = ''
        self.cod_conta_prod = 0
        self.razon_social_cliente = ''
        self.cif_cliente = ''
        self.direccion_cliente = ''
        self.tlf_cliente = ''
        self.ubicacion_cliente = ''
        self.cod_conta_cliente = ''
        self.razon_social_proveedor = ''
        self.cif_proveedor = ''
        self.direccion_proveedor = ''
        self.tlf_proveedor = ''
        self.ubicacion_proveedor = ''
        self.cod_conta_proveedor = ''
        self.razon_social_agencia = ''
        self.cif_agencia = ''
        self.direccion_agencia = ''
        self.tlf_agencia = ''
        self.ubicacion_agencia = ''
        self.cod_conta_agencia = ''
        self.razon_social_poseedor = ''
        self.cif_poseedor = ''
        self.direccion_poseedor = ''
        self.tlf_poseedor = ''
        self.ubicacion_poseedor = ''
        self.cod_conta_poseedor = ''
        self.nombre_conductor = ''
        self.nif_conductor = ''
        self.direccion_conductor = ''
        self.tlf_conductor = ''
        self.ubicacion_conductor = ''

class TbHistoricos:
    INSERT = '''
        insert into Historicos
        ( num_albaran, mat_cabina, mat_remolque, fecha_entrada, fecha_salida, bruto, tara, neto, origen, destino, forma_pago, iva_aplicable, importe_final, importe_sin_iva, importe_producto, nombre_producto, tipo_material, cod_conta_prod, razon_social_cliente, cif_cliente, direccion_cliente, tlf_cliente, ubicacion_cliente, cod_conta_cliente, razon_social_proveedor, cif_proveedor, direccion_proveedor, tlf_proveedor, ubicacion_proveedor, cod_conta_proveedor, razon_social_agencia, cif_agencia, direccion_agencia, tlf_agencia, ubicacion_agencia, cod_conta_agencia, razon_social_poseedor, cif_poseedor, direccion_poseedor, tlf_poseedor, ubicacion_poseedor, cod_conta_poseedor, nombre_conductor, nif_conductor, direccion_conductor, tlf_conductor, ubicacion_conductor)
        values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        '''
    DELETE = 'delete from Historicos where id_historico = ?'
    SELECT = 'select * from Historicos'
    UPDATE = '''
        update Historicos set  
        num_albaran = ?,
        mat_cabina = ?,
        mat_remolque = ?,
        fecha_entrada = ?,
        fecha_salida = ?,
        bruto = ?,
        tara = ?,
        neto = ?,
        origen = ?,
        destino = ?,
        forma_pago = ?,
        iva_aplicable = ?,
        importe_final = ?,
        importe_sin_iva = ?,
        importe_producto = ?,
        nombre_producto = ?,
        tipo_material = ?,
        cod_conta_prod = ?,
        razon_social_cliente = ?,
        cif_cliente = ?,
        direccion_cliente = ?,
        tlf_cliente = ?,
        ubicacion_cliente = ?,
        cod_conta_cliente = ?,
        razon_social_proveedor = ?,
        cif_proveedor = ?,
        direccion_proveedor = ?,
        tlf_proveedor = ?,
        ubicacion_proveedor = ?,
        cod_conta_proveedor = ?,
        razon_social_agencia = ?,
        cif_agencia = ?,
        direccion_agencia = ?,
        tlf_agencia = ?,
        ubicacion_agencia = ?,
        cod_conta_agencia = ?,
        razon_social_poseedor = ?,
        cif_poseedor = ?,
        direccion_poseedor = ?,
        tlf_poseedor = ?,
        ubicacion_poseedor = ?,
        cod_conta_poseedor = ?,
        nombre_conductor = ?,
        nif_conductor = ?,
        direccion_conductor = ?,
        tlf_conductor = ?,
        ubicacion_conductor = ?
        where  id_historico = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, historico ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (historico.id_historico))

    def get_historico(self, id_historico=None):
        sql = self.SELECT + " where id_historico=" + str(id_historico) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, historico=None):
        if historico is not None:
            if self.get_historico(historico.id_historico) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    historico.num_albaran,
                    historico.mat_cabina,
                    historico.mat_remolque,
                    historico.fecha_entrada,
                    historico.fecha_salida,
                    historico.bruto,
                    historico.tara,
                    historico.neto,
                    historico.origen,
                    historico.destino,
                    historico.forma_pago,
                    historico.iva_aplicable,
                    historico.importe_final,
                    historico.importe_sin_iva,
                    historico.importe_producto,
                    historico.nombre_producto,
                    historico.tipo_material,
                    historico.cod_conta_prod,
                    historico.razon_social_cliente,
                    historico.cif_cliente,
                    historico.direccion_cliente,
                    historico.tlf_cliente,
                    historico.ubicacion_cliente,
                    historico.cod_conta_cliente,
                    historico.razon_social_proveedor,
                    historico.cif_proveedor,
                    historico.direccion_proveedor,
                    historico.tlf_proveedor,
                    historico.ubicacion_proveedor,
                    historico.cod_conta_proveedor,
                    historico.razon_social_agencia,
                    historico.cif_agencia,
                    historico.direccion_agencia,
                    historico.tlf_agencia,
                    historico.ubicacion_agencia,
                    historico.cod_conta_agencia,
                    historico.razon_social_poseedor,
                    historico.cif_poseedor,
                    historico.direccion_poseedor,
                    historico.tlf_poseedor,
                    historico.ubicacion_poseedor,
                    historico.cod_conta_poseedor,
                    historico.nombre_conductor,
                    historico.nif_conductor,
                    historico.direccion_conductor,
                    historico.tlf_conductor,
                    historico.ubicacion_conductor))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    historico.num_albaran,
                    historico.mat_cabina,
                    historico.mat_remolque,
                    historico.fecha_entrada,
                    historico.fecha_salida,
                    historico.bruto,
                    historico.tara,
                    historico.neto,
                    historico.origen,
                    historico.destino,
                    historico.forma_pago,
                    historico.iva_aplicable,
                    historico.importe_final,
                    historico.importe_sin_iva,
                    historico.importe_producto,
                    historico.nombre_producto,
                    historico.tipo_material,
                    historico.cod_conta_prod,
                    historico.razon_social_cliente,
                    historico.cif_cliente,
                    historico.direccion_cliente,
                    historico.tlf_cliente,
                    historico.ubicacion_cliente,
                    historico.cod_conta_cliente,
                    historico.razon_social_proveedor,
                    historico.cif_proveedor,
                    historico.direccion_proveedor,
                    historico.tlf_proveedor,
                    historico.ubicacion_proveedor,
                    historico.cod_conta_proveedor,
                    historico.razon_social_agencia,
                    historico.cif_agencia,
                    historico.direccion_agencia,
                    historico.tlf_agencia,
                    historico.ubicacion_agencia,
                    historico.cod_conta_agencia,
                    historico.razon_social_poseedor,
                    historico.cif_poseedor,
                    historico.direccion_poseedor,
                    historico.tlf_poseedor,
                    historico.ubicacion_poseedor,
                    historico.cod_conta_poseedor,
                    historico.nombre_conductor,
                    historico.nif_conductor,
                    historico.direccion_conductor,
                    historico.tlf_conductor,
                    historico.ubicacion_conductor,
                    historico.id_historico))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Historico()
            o.id_historico = fila['id_historico']
            o.num_albaran = fila['num_albaran']
            o.mat_cabina = fila['mat_cabina']
            o.mat_remolque = fila['mat_remolque']
            o.fecha_entrada = fila['fecha_entrada']
            o.fecha_salida = fila['fecha_salida']
            o.bruto = fila['bruto']
            o.tara = fila['tara']
            o.neto = fila['neto']
            o.origen = fila['origen']
            o.destino = fila['destino']
            o.forma_pago = fila['forma_pago']
            o.iva_aplicable = fila['iva_aplicable']
            o.importe_final = fila['importe_final']
            o.importe_sin_iva = fila['importe_sin_iva']
            o.importe_producto = fila['importe_producto']
            o.nombre_producto = fila['nombre_producto']
            o.tipo_material = fila['tipo_material']
            o.cod_conta_prod = fila['cod_conta_prod']
            o.razon_social_cliente = fila['razon_social_cliente']
            o.cif_cliente = fila['cif_cliente']
            o.direccion_cliente = fila['direccion_cliente']
            o.tlf_cliente = fila['tlf_cliente']
            o.ubicacion_cliente = fila['ubicacion_cliente']
            o.cod_conta_cliente = fila['cod_conta_cliente']
            o.razon_social_proveedor = fila['razon_social_proveedor']
            o.cif_proveedor = fila['cif_proveedor']
            o.direccion_proveedor = fila['direccion_proveedor']
            o.tlf_proveedor = fila['tlf_proveedor']
            o.ubicacion_proveedor = fila['ubicacion_proveedor']
            o.cod_conta_proveedor = fila['cod_conta_proveedor']
            o.razon_social_agencia = fila['razon_social_agencia']
            o.cif_agencia = fila['cif_agencia']
            o.direccion_agencia = fila['direccion_agencia']
            o.tlf_agencia = fila['tlf_agencia']
            o.ubicacion_agencia = fila['ubicacion_agencia']
            o.cod_conta_agencia = fila['cod_conta_agencia']
            o.razon_social_poseedor = fila['razon_social_poseedor']
            o.cif_poseedor = fila['cif_poseedor']
            o.direccion_poseedor = fila['direccion_poseedor']
            o.tlf_poseedor = fila['tlf_poseedor']
            o.ubicacion_poseedor = fila['ubicacion_poseedor']
            o.cod_conta_poseedor = fila['cod_conta_poseedor']
            o.nombre_conductor = fila['nombre_conductor']
            o.nif_conductor = fila['nif_conductor']
            o.direccion_conductor = fila['direccion_conductor']
            o.tlf_conductor = fila['tlf_conductor']
            o.ubicacion_conductor = fila['ubicacion_conductor']
            return o

    def get_historicos(self, filtro=None):
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




