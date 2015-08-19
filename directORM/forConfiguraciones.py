
import sqlite3
import directORM

class Configuracion:
    def __init__(self):

        self.id = -1
        self.parametro = ''
        self.valor = ''

class TbConfiguraciones:
    INSERT = '''
        insert into Configuraciones
        ( parametro, valor)
        values (?,?)
        '''
    DELETE = 'delete from Configuraciones where id = ?'
    SELECT = 'select * from Configuraciones'
    UPDATE = '''
        update Configuraciones set  
        parametro = ?,
        valor = ?
        where  id = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, configuracion ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (configuracion.id))

    def get_configuracion(self, id=None):
        sql = self.SELECT + " where id=" + str(id) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, configuracion=None):
        if configuracion is not None:
            if self.get_configuracion(configuracion.id) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    configuracion.parametro,
                    configuracion.valor))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    configuracion.parametro,
                    configuracion.valor,
                    configuracion.id))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Configuracion()
            o.id = fila['id']
            o.parametro = fila['parametro']
            o.valor = fila['valor']
            return o

    def get_configuraciones(self, filtro=None):
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




