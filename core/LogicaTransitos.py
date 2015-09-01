
from directORM.forTransito_actuales import Transito_actual, TbTransito_actuales
from directORM.forProductos import TbProductos
from directORM.forEmpresas import TbEmpresas
from directORM.forConductores import TbConductores
from directORM.forHistoricos import TbHistoricos, Historico
from directORM.forConfiguraciones import TbConfiguraciones, Configuracion

class Logica_Transitos:

    def __init__(self):
        pass

    def guardar_transito(self, transito=None):
        '''
        Guarda un transito en la base de datos
        :param transito:
        '''
        if transito is not None:
            tabla = TbTransito_actuales()
            tabla.save(transito)

    def get_transito(self, id=None):
        '''
        Devuelve el transito buscado por ID desde la db
        :param id:
        :return: transito or None
        '''
        if id is not None:
            tabla = TbTransito_actuales()
            transito = tabla.get_transito_actual(id)
            return transito
        else:
            return None

    def nombres_desde_db(self, transito=None):
        '''
        Devuelve los nombres de producto, poseedor, proveedor, cliente,
        agencia y conductor a traves del transito actual
        :param transito:
        :return:
        '''
        if transito is not None:
            #transito = Transito_actual()
            tproducto = TbProductos()
            producto = tproducto.get_producto(id_producto=transito.id_producto)

            tempresa = TbEmpresas()
            poseedor = tempresa.get_empresa(id_empresa=transito.id_poseedor)
            proveedor = tempresa.get_empresa(id_empresa=transito.id_proveedor)
            cliente = tempresa.get_empresa(id_empresa=transito.id_cliente)
            agencia = tempresa.get_empresa(id_empresa=transito.id_agencia)

            tconductores = TbConductores()
            conductor = tconductores.get_conductor(id_conductor=transito.id_conductor)

            return producto.nombre, \
                   poseedor.nombre, \
                   proveedor.nombre, \
                   cliente.nombre, \
                   agencia.nombre, \
                   conductor.nombre
        else:
            return '', '', '', '', '', ''

    def generar_numero_albaran(self):
        '''
        Coge el numero de albaran guardado en la base de datos, lo retorna y
        antes de hacerlo guarda el numero siguiente
        :return:
        '''
        configuraciones = TbConfiguraciones()
        filas = configuraciones.get_configuraciones(filtro="parametro like 'numAlbaran' ")

        config_albaran = filas[0]
        assert isinstance(config_albaran, Configuracion)
        valor = int(config_albaran.valor)
        valor_a_guardar = valor + 1
        config_albaran.valor = str(valor_a_guardar)

        configuraciones.save(config_albaran)
        return valor

    def guardar_a_historico(self, id=None):
        '''
        Guarda los datos de un transito a la base de datos como historico
        y lo borra de transitos actuales
        :param id:
        :return:
        '''
        if id is not None:
            transitos = TbTransito_actuales()
            transito_tmp = transitos.get_transito_actual(id_transito=id)

            historicos = TbHistoricos()

            historico = Historico()
            historico.fecha_entrada = transito_tmp.fecha_entrada
            historico.mat_cabina = transito_tmp.mat_cabina
            historico.mat_remolque = transito_tmp.mat_remolque
            historico.bruto = transito_tmp.bruto
            historico.tara = transito_tmp.tara
            historico.neto = transito_tmp.neto
            historico.destino = transito_tmp.destino
            historico.origen = transito_tmp.origen
            historico.fecha_salida = transito_tmp.fecha_salida
            historico.num_albaran = self.generar_numero_albaran()

            producto = TbProductos().get_producto(id_producto= transito_tmp.id_producto)
            historico.cod_conta_prod = producto.codigo_contable
            historico.nombre_producto = producto.nombre
            historico.iva_aplicable = producto.iva_aplicado
            historico.importe_producto = producto.precio
            historico.tipo_material = producto.tipo_material
            historico.importe_sin_iva = historico.importe_producto * historico.neto
            historico.importe_final = historico.iva_aplicable * historico.importe_sin_iva

            cliente = TbEmpresas().get_empresa(id_empresa=transito_tmp.id_cliente)
            historico.razon_social_cliente = cliente.razon_social
            historico.cif_cliente = cliente.cif
            historico.direccion_cliente = cliente.direccion
            historico.cod_conta_cliente = cliente.codigo_contable
            historico.tlf_cliente = cliente.telefono
            historico.ubicacion_cliente = ('%s (%s)' % (cliente.localidad, cliente.provincia))

            poseedor = TbEmpresas().get_empresa(id_empresa=transito_tmp.id_poseedor)
            historico.razon_social_poseedor = cliente.razon_social
            historico.cif_poseedor = cliente.cif
            historico.direccion_poseedor = cliente.direccion
            historico.cod_conta_poseedor = cliente.codigo_contable
            historico.tlf_poseedor = cliente.telefono
            historico.ubicacion_poseedor = ('%s (%s)' % (cliente.localidad, cliente.provincia))

            proveedor = TbEmpresas().get_empresa(id_empresa=transito_tmp.id_proveedor)
            historico.razon_social_proveedor = cliente.razon_social
            historico.cif_proveedor = cliente.cif
            historico.direccion_proveedor = cliente.direccion
            historico.cod_conta_proveedor = cliente.codigo_contable
            historico.tlf_proveedor = cliente.telefono
            historico.ubicacion_proveedor = ('%s (%s)' % (cliente.localidad, cliente.provincia))

            agencia = TbEmpresas().get_empresa(id_empresa=transito_tmp.id_agencia)
            historico.razon_social_agencia = cliente.razon_social
            historico.cif_agencia = cliente.cif
            historico.direccion_agencia = cliente.direccion
            historico.cod_conta_agencia = cliente.codigo_contable
            historico.tlf_agencia = cliente.telefono
            historico.ubicacion_agencia = ('%s (%s)' % (cliente.localidad, cliente.provincia))

            conductor = TbConductores().get_conductor(id_conductor=transito_tmp.id_conductor)
            historico.nombre_conductor = ('%s %s') % (conductor.nombre, conductor.apellidos)
            historico.tlf_conductor = conductor.telefono
            historico.nif_conductor = conductor.nif
            historico.direccion_conductor = conductor.direccion
            historico.ubicacion_conductor = ('%s (%s)' % (conductor.localidad, conductor.provincia))

            historicos.save(historico)
            self.eliminar_transito(id=transito_tmp.id_transito)

        else:
            print('No se pudo guardar el transito en el historico')

    def eliminar_transito(self, id=None):
        if id is not None:
            tabla = TbTransito_actuales()
            transito = tabla.get_transito_actual(id_transito=id)
            tabla.remove(transito)
            print('Eliminado transito')
        else:
            print('No se puede eliminar transito, falta ID')