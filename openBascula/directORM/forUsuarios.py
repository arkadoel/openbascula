
import sqlite3
import directORM

class Usuario:
    def __init__(self):

        self.loginName = ''
        self.password = ''
        self.real_name = ''
        self.email = ''
        self.permiso = ''

class TbUsuarios:
    INSERT = '''
        insert into Usuarios
        ( password, real_name, email, permiso)
        values (?,?,?,?)
        '''
    DELETE = 'delete from Usuarios where loginName = ?'
    SELECT = 'select * from Usuarios'
    UPDATE = '''
        update Usuarios set  
        password = ?,
        real_name = ?,
        email = ?,
        permiso = ?
        where  loginName = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, usuario ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (usuario.loginName))

    def get_usuario(self, loginName=None):
        sql = self.SELECT + " where loginName=" + str(loginName) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, usuario=None):
        if usuario is not None:
            if self.get_usuario(usuario.loginName) is None:
                sql = self.INSERT
                self.gestorDB.ejecutarSQL(sql, (
                    usuario.password,
                    usuario.real_name,
                    usuario.email,
                    usuario.permiso))
            else:
                sql = self.UPDATE
                self.gestorDB.ejecutarSQL(sql, (
                    usuario.password,
                    usuario.real_name,
                    usuario.email,
                    usuario.permiso,
                    usuario.loginName))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Usuario()
            o.loginName = fila['loginName']
            o.password = fila['password']
            o.real_name = fila['real_name']
            o.email = fila['email']
            o.permiso = fila['permiso']
            return o

    def get_usuarios(self, filtro=None):
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




