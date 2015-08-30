
class Util:

    @staticmethod
    def formato_matricula(control=None):
        """
        Pone en mayusculas y agrega guiones cuando se cambia entre letras y digitos
        :param control: QLineEdit que se quiere manejar
        """
        if control is not None:

            if len(control.text()) > 1:
                texto = control.text()

                if texto[-2].isdigit() and texto[-1].isalpha()\
                        or texto[-2].isalpha() and texto[-1].isdigit():
                    letra = texto[-1]
                    texto = texto[0:-1] + '-' + letra
                    control.setText(texto)

            #poner los espacios como guiones
            if ' ' in control.text()[-1]:
                control.setText(control.text().replace(' ', '-'))
            #poner el texto en mayusculas
            control.setText(control.text().upper())

    @staticmethod
    def formato_mayuscula(control=None):
        """
        Pone en mayusculas el texto del control pasado
        :param control: QLineEdit que se quiere manejar
        """
        if control is not None:
            #poner el texto en mayusculas
            control.setText(control.text().upper())

    @staticmethod
    def formato_numerico(control=None):
        """
        Hace que solo se admitan numeros
        :param control: QLineEdit que se quiere manejar
        """
        if control is not None:
            texto = control.text()
            if len(texto) is 0:
                if texto.isalpha():
                    control.setText('')
            else:
                if texto[-1].isalpha():
                    control.setText(texto[0:-1])
