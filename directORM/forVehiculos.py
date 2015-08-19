
import sqlite3
import directORM

class Vehiculo:
    def __init__(self):

        self.id_vehiculo = -1
        self.matricula = ''
        self.id_empresa = 0
        self.id_conductor = 0
        self.fecha_alta = ''
        self.fecha_baja = ''

class TbVehiculos:
    INSERT = '''
        insert into Vehiculos
        ( matricula, id_empresa, id_conductor, fecha_alta, fecha_baja)
        values (?,?,?,?,?)
        '''
    DELETE = 'delete from Vehiculos where id_vehiculo = ?'
    SELECT = 'select * from Vehiculos'
    UPDATE = '''
        update Vehiculos set  
        matricula = ?,
        id_empresa = ?,
        id_conductor = ?,
        fecha_alta = ?,
        fecha_baja = ?
        where  id_vehiculo = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, vehiculo ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (vehiculo.id_vehiculo))

    def get_vehiculo(self, id_vehiculo=None):
        sql = self.SELECT + " where id_vehiculo=" + str(id_vehiculo) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, vehiculo=None):
        if vehiculo is not None:
            if self.get_vehiculo(vehiculo.id_vehiculo) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    vehiculo.matricula,
                    vehiculo.id_empresa,
                    vehiculo.id_conductor,
                    vehiculo.fecha_alta,
                    vehiculo.fecha_baja))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    vehiculo.matricula,
                    vehiculo.id_empresa,
                    vehiculo.id_conductor,
                    vehiculo.fecha_alta,
                    vehiculo.fecha_baja,
                    vehiculo.id_vehiculo))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Vehiculo()
            o.id_vehiculo = fila['id_vehiculo']
            o.matricula = fila['matricula']
            o.id_empresa = fila['id_empresa']
            o.id_conductor = fila['id_conductor']
            o.fecha_alta = fila['fecha_alta']
            o.fecha_baja = fila['fecha_baja']
            return o

    def get_vehiculos(self, filtro=None):
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




