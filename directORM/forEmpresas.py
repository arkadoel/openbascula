
import sqlite3
import directORM

class Empresa:
    def __init__(self):

        self.id_empresa = -1
        self.nombre = ''
        self.razon_social = ''
        self.cif = ''
        self.direccion = ''
        self.localidad = ''
        self.provincia = ''
        self.telefono = ''
        self.email = ''
        self.cuenta_bancaria = ''
        self.forma_de_pago = ''
        self.codigo_contable = ''

class TbEmpresas:
    INSERT = '''
        insert into Empresas
        ( nombre, razon_social, cif, direccion, localidad, provincia, telefono, email, cuenta_bancaria, forma_de_pago, codigo_contable)
        values (?,?,?,?,?,?,?,?,?,?,?)
        '''
    DELETE = 'delete from Empresas where id_empresa = ?'
    SELECT = 'select * from Empresas'
    UPDATE = '''
        update Empresas set  
        nombre = ?,
        razon_social = ?,
        cif = ?,
        direccion = ?,
        localidad = ?,
        provincia = ?,
        telefono = ?,
        email = ?,
        cuenta_bancaria = ?,
        forma_de_pago = ?,
        codigo_contable = ?
        where  id_empresa = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, empresa ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (empresa.id_empresa))

    def get_empresa(self, id_empresa=None):
        sql = self.SELECT + " where id_empresa=" + str(id_empresa) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, empresa=None):
        if empresa is not None:
            if self.get_empresa(empresa.id_empresa) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    empresa.nombre,
                    empresa.razon_social,
                    empresa.cif,
                    empresa.direccion,
                    empresa.localidad,
                    empresa.provincia,
                    empresa.telefono,
                    empresa.email,
                    empresa.cuenta_bancaria,
                    empresa.forma_de_pago,
                    empresa.codigo_contable))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    empresa.nombre,
                    empresa.razon_social,
                    empresa.cif,
                    empresa.direccion,
                    empresa.localidad,
                    empresa.provincia,
                    empresa.telefono,
                    empresa.email,
                    empresa.cuenta_bancaria,
                    empresa.forma_de_pago,
                    empresa.codigo_contable,
                    empresa.id_empresa))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Empresa()
            o.id_empresa = fila['id_empresa']
            o.nombre = fila['nombre']
            o.razon_social = fila['razon_social']
            o.cif = fila['cif']
            o.direccion = fila['direccion']
            o.localidad = fila['localidad']
            o.provincia = fila['provincia']
            o.telefono = fila['telefono']
            o.email = fila['email']
            o.cuenta_bancaria = fila['cuenta_bancaria']
            o.forma_de_pago = fila['forma_de_pago']
            o.codigo_contable = fila['codigo_contable']
            return o

    def get_empresas(self, filtro=None):
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




