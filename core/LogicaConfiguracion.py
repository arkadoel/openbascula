from directORM.forConfiguraciones import Configuracion, TbConfiguraciones

class Logica_Configuracion:
    def __init__(self):
        config = TbConfiguraciones()
        configuraciones = config.get_configuraciones()
        for conf in configuraciones:
            assert isinstance(conf, Configuracion)
            print('Parametro: %s  Valor: %s' % (conf.parametro, conf.valor))