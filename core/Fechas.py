
from _datetime import datetime
from PyQt4 import QtCore

def get_hora():
    horas = datetime.now().hour
    minutos = datetime.now().minute
    segundos = datetime.now().second
    resultado = ''

    if horas <10:
        resultado += '0' + str(horas)
    else:
        resultado += str(horas)

    resultado += ':'

    if minutos <10:
        resultado += '0' + str(minutos)
    else:
        resultado += str(minutos)

    resultado += ':'

    if segundos <10:
        resultado += '0' + str(segundos)
    else:
        resultado += str(segundos)

    return resultado

def get_semana() -> str:
    '''
    Devuelve el dia de la semana en el que estamos
    :rtype : basestring
    :return: String
    '''
    dias = ['Lunes',
            'Martes',
            'Miercoles',
            'Jueves',
            'Viernes',
            'Sabado',
            'Domingo']
    return dias[datetime.today().weekday()]

def get_fecha() -> str:
    '''
    Devuelve la fecha en la que estamos
    :rtype : basestring
    :return: String
    '''
    dia = datetime.today().day
    mes = datetime.today().month
    anyo = datetime.today().year
    fecha = dia + '/' + mes + '/' + anyo

    return fecha

def fecha_larga_desde_QDateTime(control=None):
    assert isinstance(control, QtCore.QDateTime)
    fecha = (control.toString('dd/MM/yyyy hh:mm:ss'))
    return fecha
