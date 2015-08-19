
import sqlite3
import directORM

class Usuario:
    def __init__(self):

        self.login_name = ''
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
    DELETE = 'delete from Usuarios where login_name = ?'
    SELECT = 'select * from Usuarios'
    UPDATE = '''
        update Usuarios set  
        password = ?,
        real_name = ?,
        email = ?,
        permiso = ?
        where  login_name = ?
        '''
    def __init__(self):
        self.gestorDB = directORM.Db()

    def remove(self, usuario ):
        sql = self.DELETE
        self.gestorDB.ejecutarSQL(sql, (usuario.login_name))

    def get_usuario(self, login_name=None):
        sql = self.SELECT + " where login_name=" + str(login_name) +";"
        fila = self.gestorDB.consultaUnicaSQL(sql)
        if fila is None:
            return None
        else: 
            o = self.mapear_objeto(fila)
            return o


    def save(self, usuario=None):
        if usuario is not None:
            if self.get_usuario(usuario.login_name) is None:
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
                    usuario.login_name))

    def mapear_objeto(self, fila=None):
        if fila is None:
            return None
        else:
            o = Usuario()
            o.login_name = fila['login_name']
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




