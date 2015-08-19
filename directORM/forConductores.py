
import sqlite3
import directORM

class Conductor:
    def __init__(self):

        self.id_conductor = -1
        self.id_empresa = 0
        self.fecha_alta = ''
        self.fecha_baja = ''
        self.nombre = ''
        self.apellidos = ''
        self.nif = ''
        self.direccion = ''
        self.localidad = ''
        self.provincia = ''
        self.telefono = ''
        self.email = ''

class TbConductores:
    INSERT = '''
        insert into Conductores
        ( id_empresa, fecha_alta, fecha_baja, nombre, apellidos, nif, direccion, localidad, provincia, telefono, email)
        values (?,?,?,?,?,?,?,?,?,?,?)
        '''
    DELETE = 'delete from Conductores where id_conductor = ?'
    SELECT = 'select * from Conductores'
    UPDATE = '''
        update Conductores set  
        id_empresa = ?,
        fecha_alta = ?,
        fecha_baja = ?,
        nombre = ?,
        apellidos = ?,
        nif = ?,
        direccion = ?,
        localidad = ?,
        provincia = ?,
        telefono = ?,
        email = ?
        where  id_conductor = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, conductor ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (conductor.id_conductor))

    def get_conductor(self, id_conductor=None):
        sql = self.SELECT + " where id_conductor=" + str(id_conductor) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, conductor=None):
        if conductor is not None:
            if self.get_conductor(conductor.id_conductor) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    conductor.id_empresa,
                    conductor.fecha_alta,
                    conductor.fecha_baja,
                    conductor.nombre,
                    conductor.apellidos,
                    conductor.nif,
                    conductor.direccion,
                    conductor.localidad,
                    conductor.provincia,
                    conductor.telefono,
                    conductor.email))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    conductor.id_empresa,
                    conductor.fecha_alta,
                    conductor.fecha_baja,
                    conductor.nombre,
                    conductor.apellidos,
                    conductor.nif,
                    conductor.direccion,
                    conductor.localidad,
                    conductor.provincia,
                    conductor.telefono,
                    conductor.email,
                    conductor.id_conductor))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Conductor()
            o.id_conductor = fila['id_conductor']
            o.id_empresa = fila['id_empresa']
            o.fecha_alta = fila['fecha_alta']
            o.fecha_baja = fila['fecha_baja']
            o.nombre = fila['nombre']
            o.apellidos = fila['apellidos']
            o.nif = fila['nif']
            o.direccion = fila['direccion']
            o.localidad = fila['localidad']
            o.provincia = fila['provincia']
            o.telefono = fila['telefono']
            o.email = fila['email']
            return o

    def get_conductores(self, filtro=None):
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




