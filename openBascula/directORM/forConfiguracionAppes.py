
import sqlite3
import directORM

class ConfiguracionApp:
    def __init__(self):

        self.id = -1
        self.parametro = ''
        self.valor = ''

class TbConfiguracionAppes:
    INSERT = '''
        insert into ConfiguracionAppes
        ( parametro, valor)
        values (?,?)
        '''
    DELETE = 'delete from ConfiguracionAppes where id = ?'
    SELECT = 'select * from ConfiguracionAppes'
    UPDATE = '''
        update ConfiguracionAppes set  
        parametro = ?,
        valor = ?
        where  id = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, configuracionapp ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (configuracionapp.id))

    def get_configuracionapp(self, id=None):
        sql = self.SELECT + " where id=" + str(id) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, configuracionapp=None):
        if configuracionapp is not None:
            if self.get_configuracionapp(configuracionapp.id) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    configuracionapp.parametro,
                    configuracionapp.valor))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    configuracionapp.parametro,
                    configuracionapp.valor,
                    configuracionapp.id))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = ConfiguracionApp()
            o.id = fila['id']
            o.parametro = fila['parametro']
            o.valor = fila['valor']
            return o

    def get_configuracionappes(self, filtro=None):
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




