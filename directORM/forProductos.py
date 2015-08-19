
import sqlite3
import directORM

class Producto:
    def __init__(self):

        self.id_producto = -1
        self.nombre = ''
        self.descripcion = ''
        self.precio = 0.0
        self.iva_aplicado = 0
        self.tipo_material = ''
        self.codigo_contable = ''
        self.es_tarifa_plana = False

class TbProductos:
    INSERT = '''
        insert into Productos
        ( nombre, descripcion, precio, iva_aplicado, tipo_material, codigo_contable, es_tarifa_plana)
        values (?,?,?,?,?,?,?)
        '''
    DELETE = 'delete from Productos where id_producto = ?'
    SELECT = 'select * from Productos'
    UPDATE = '''
        update Productos set  
        nombre = ?,
        descripcion = ?,
        precio = ?,
        iva_aplicado = ?,
        tipo_material = ?,
        codigo_contable = ?,
        es_tarifa_plana = ?
        where  id_producto = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, producto ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (producto.id_producto))

    def get_producto(self, id_producto=None):
        sql = self.SELECT + " where id_producto=" + str(id_producto) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, producto=None):
        if producto is not None:
            if self.get_producto(producto.id_producto) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    producto.nombre,
                    producto.descripcion,
                    producto.precio,
                    producto.iva_aplicado,
                    producto.tipo_material,
                    producto.codigo_contable,
                    producto.es_tarifa_plana))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    producto.nombre,
                    producto.descripcion,
                    producto.precio,
                    producto.iva_aplicado,
                    producto.tipo_material,
                    producto.codigo_contable,
                    producto.es_tarifa_plana,
                    producto.id_producto))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Producto()
            o.id_producto = fila['id_producto']
            o.nombre = fila['nombre']
            o.descripcion = fila['descripcion']
            o.precio = fila['precio']
            o.iva_aplicado = fila['iva_aplicado']
            o.tipo_material = fila['tipo_material']
            o.codigo_contable = fila['codigo_contable']
            o.es_tarifa_plana = fila['es_tarifa_plana']
            return o

    def get_productos(self, filtro=None):
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




