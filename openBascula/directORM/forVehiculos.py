
import sqlite3
import directORM

class Vehiculo:
    def __init__(self):

        self.idVehiculo = -1
        self.matricula = ''
        self.id_empresa = 0
        self.fecha_alta = ''
        self.fecha_baja = ''

class TbVehiculos:
    INSERT = '''
        insert into Vehiculos
        ( matricula, id_empresa, fecha_alta, fecha_baja)
        values (?,?,?,?)
        '''
    DELETE = 'delete from Vehiculos where idVehiculo = ?'
    SELECT = 'select * from Vehiculos'
    UPDATE = '''
        update Vehiculos set  
        matricula = ?,
        id_empresa = ?,
        fecha_alta = ?,
        fecha_baja = ?
        where  idVehiculo = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, vehiculo ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (vehiculo.idVehiculo))

    def get_vehiculo(self, idVehiculo=None):
        sql = self.SELECT + " where idVehiculo=" + str(idVehiculo) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, vehiculo=None):
        if vehiculo is not None:
            if self.get_vehiculo(vehiculo.idVehiculo) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    vehiculo.matricula,
                    vehiculo.id_empresa,
                    vehiculo.fecha_alta,
                    vehiculo.fecha_baja))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    vehiculo.matricula,
                    vehiculo.id_empresa,
                    vehiculo.fecha_alta,
                    vehiculo.fecha_baja,
                    vehiculo.idVehiculo))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Vehiculo()
            o.idVehiculo = fila['idVehiculo']
            o.matricula = fila['matricula']
            o.id_empresa = fila['id_empresa']
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




