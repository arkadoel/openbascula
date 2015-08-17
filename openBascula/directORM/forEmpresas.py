
import sqlite3
import directORM

class Empresa:
    def __init__(self):

        self.idEmpresa = -1
        self.Nombre = ''
        self.RazonSocial = ''
        self.CIF = ''
        self.Direccion = ''
        self.Localidad = ''
        self.Provincia = ''
        self.Telefono = ''
        self.Email = ''
        self.Cuenta_bancaria = ''
        self.Forma_de_pago = ''
        self.Codigo_contabilidad = ''

class TbEmpresas:
    INSERT = '''
        insert into Empresas
        ( Nombre, RazonSocial, CIF, Direccion, Localidad, Provincia, Telefono, Email, Cuenta_bancaria, Forma_de_pago, Codigo_contabilidad)
        values (?,?,?,?,?,?,?,?,?,?,?)
        '''
    DELETE = 'delete from Empresas where idEmpresa = ?'
    SELECT = 'select * from Empresas'
    UPDATE = '''
        update Empresas set  
        Nombre = ?,
        RazonSocial = ?,
        CIF = ?,
        Direccion = ?,
        Localidad = ?,
        Provincia = ?,
        Telefono = ?,
        Email = ?,
        Cuenta_bancaria = ?,
        Forma_de_pago = ?,
        Codigo_contabilidad = ?
        where  idEmpresa = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, empresa ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (empresa.idEmpresa))

    def get_empresa(self, idEmpresa=None):
        sql = self.SELECT + " where idEmpresa=" + str(idEmpresa) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, empresa=None):
        if empresa is not None:
            if self.get_empresa(empresa.idEmpresa) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    empresa.Nombre,
                    empresa.RazonSocial,
                    empresa.CIF,
                    empresa.Direccion,
                    empresa.Localidad,
                    empresa.Provincia,
                    empresa.Telefono,
                    empresa.Email,
                    empresa.Cuenta_bancaria,
                    empresa.Forma_de_pago,
                    empresa.Codigo_contabilidad))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    empresa.Nombre,
                    empresa.RazonSocial,
                    empresa.CIF,
                    empresa.Direccion,
                    empresa.Localidad,
                    empresa.Provincia,
                    empresa.Telefono,
                    empresa.Email,
                    empresa.Cuenta_bancaria,
                    empresa.Forma_de_pago,
                    empresa.Codigo_contabilidad,
                    empresa.idEmpresa))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Empresa()
            o.idEmpresa = fila['idEmpresa']
            o.Nombre = fila['Nombre']
            o.RazonSocial = fila['RazonSocial']
            o.CIF = fila['CIF']
            o.Direccion = fila['Direccion']
            o.Localidad = fila['Localidad']
            o.Provincia = fila['Provincia']
            o.Telefono = fila['Telefono']
            o.Email = fila['Email']
            o.Cuenta_bancaria = fila['Cuenta_bancaria']
            o.Forma_de_pago = fila['Forma_de_pago']
            o.Codigo_contabilidad = fila['Codigo_contabilidad']
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




