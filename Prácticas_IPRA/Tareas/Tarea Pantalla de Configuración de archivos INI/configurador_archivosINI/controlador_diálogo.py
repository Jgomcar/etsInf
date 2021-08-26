import configparser, sys
from PySide2. QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtPrintSupport import QPrintDialog, QPrinter
from dialogo_configuracion import Ui_Dialog


class DiálogoConfiguraciónINI(QDialog):
    NOMBRE = 0
    TIPO = 1
    TEXTO_AYUDA = 2
    VALIDACIÓN = 3
    
    def __init__(self):
        super(DiálogoConfiguraciónINI, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Configuración")

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    @Slot()
    def búsqueda_carpeta(self):
        '''Abre un cuadro de búsqueda de un directorio'''
        try:
            ruta_carpeta= QFileDialog.getExistingDirectory(None, "Abre la carpeta deseada", "C://", options=QFileDialog.ShowDirsOnly)
        except Exception as err:
            sys.stderr.write('''
            Ruta no encontrada
            Error:{}
            '''.format(err))
        boton_pulsado = self.sender()
        for control in self.ui.lista_controles:
            if control[4] == boton_pulsado:
                control[0].setText(ruta_carpeta)
                break

    @Slot()
    def búsqueda_impresora(self):
        '''Abre un diálogo de selección de opciones de impresora de donde cogemos el nombre de la impresora y lo 
        escribimos en el control correspondiente'''
        printer = QPrinter(mode=QPrinter.HighResolution)
        printDialog = QPrintDialog(printer, self)
        printer = printDialog.printer()
        if printDialog.exec_() == QDialog.Accepted:
            pass
        boton_pulsado = self.sender()
        for control in self.ui.lista_controles:
            if control[4] == boton_pulsado:
                control[0].setText(str(printer.printerName()))
                control[0].setSelection(0, 0)
                break
        # la variable printer tiene la impresora seleccionada.

    def accept(self):
        if self.comprobar_valores():
            self.guardar_valores()
            super().accept()
        else:
            pass
    def reject(self):
        super().reject()

    def lista_valores(self):
        ''' Devuelve una lista de los valores de la configuración en formato: [nombre_dato, valor_dato]'''
        TIPO = 2

        lista_valores = []
        for lista_de_un_control in self.ui.lista_controles:
            if lista_de_un_control[TIPO] == bool:
                lista_valores.append([lista_de_un_control[self.NOMBRE].objectName(), str(lista_de_un_control[self.NOMBRE].isChecked())])
            else:
                lista_valores.append([lista_de_un_control[self.NOMBRE].objectName(), lista_de_un_control[self.NOMBRE].text()])
        return lista_valores

    def guardar_valores(self):
        ''' Reescribe el archivo INI con los datos nuevos.'''
        
        VALOR = 1

        lista_valores_modificados = self.lista_valores()

        config = configparser.ConfigParser()
        config.read('archivo_prueba.ini')
            # Recorremos el archivo INI por secciones y por valores de cada sección
        for nombre_seccion in config:
            for nombre_valor in config[nombre_seccion]:
                    # Recorremos la lista de valores que queremos configurar/editar
                for dato in lista_valores_modificados:
                    if dato[self.NOMBRE] == nombre_valor:
                            # contruir botón(tipo de dato, nombre del dato, valor actual del dato)
                        config.set(nombre_seccion, nombre_valor, dato[VALOR])
                        break
        # Escrbimos los cambios en el archivo INI
        with open("archivo_prueba.ini", "w") as archivo:
            config.write(archivo)

    def comprobar_valores(self):
        ''' Desaparecen los mensajes de error de los campos inválidos introducidos, además de los errores en las pestañas.
        Después, recorre cada dato y lo comprueba con el método "comprobar_valor" individualmente. '''
        CONTROL = 0
        TEXTO_ERROR = 1
        TIPO = 2
        VALIDACIÓN = 3
        # Borrar los campos errores que se hayan podido escribir anteriormente
        try:
            for lista_de_un_control in self.ui.lista_controles:
                Ui_Dialog.limpiar_texto(self.ui, lista_de_un_control[TEXTO_ERROR])
                #Añadir tabs en negro
            Ui_Dialog.limpiar_errores_pestañas(self.ui)
        except Exception as err:
            sys.stderr.write('''
            Fallo en la limpieza de errores de comprobación
            Error:{}
            '''.format(err))
            exit(1)
        
        try:
            correcto = True
            for lista_de_un_control in self.ui.lista_controles:
                if not self.comprobar_valor(lista_de_un_control[CONTROL],lista_de_un_control[TEXTO_ERROR], lista_de_un_control[TIPO], lista_de_un_control[VALIDACIÓN]):
                    correcto = False
        except Exception as err:
            sys.stderr.write('''
            Fallo en la comprobación de las variables.
            Error: {}
            '''.format(err))
            exit(1)
        return correcto

    def comprobar_valor(self, control, label_error, tipo, validación):
        '''Comprueba, dependiendo del tipo de dato, una validación por defecto y la validación introducida en la lista inicial en el método
        "procesar_datos". '''

        if tipo == bool: return True
        if isinstance (control, QLineEdit) and isinstance(label_error, QLabel) :
            texto = ""
            if tipo == str:
                if control.text() == '':
                    texto = "No deje campos vacíos"
                elif validación != None and not validación(control.text()):
                    texto = "Valor introducido no válido"
                else:
                    return True
            elif tipo == int:
                try:
                    if int(control.text()) <= 0:
                        texto = "Tiene que ser mayor que 0"
                    elif validación != None and not validación(int(control.text())):
                        texto = "Valor introducido no válido"
                    else:
                        return True
                except:
                    texto = "Tiene que ser un número entero"
            elif tipo == float:
                try:
                    if float(control.text()) <= 0:
                        texto = "Tiene que ser mayor que 0"
                    elif validación != None and not validación(float(control.text())):
                        texto = "Valor introducido no válido"
                    else:
                        return True
                except:
                    texto = "Tiene que ser un número real"
            elif tipo == "impresora":
                try:
                    if validación != None and not validación(control.text()):
                        texto = "Valor introducido no válido"
                    else:
                        return True
                except:
                    texto = "Dato incorrecto"
            elif tipo == "carpeta":
                try:
                    if validación != None and not validación(control.text()):
                        texto = "Valor introducido no válido"
                    else:
                        return True
                except:
                    texto = "Dato incorrecto"
            else:
                sys.stderr.write('''
                Fallo de comprobación de las variables.
                Tipo de dato no detectado.
                ''')

            label_error.setText(texto)
            Ui_Dialog.indicar_errores_pestaña(self.ui, label_error.parent())
        return False    
    
    def relacionar_botones(self):
        '''Una vez creados los botones de búsqueda, dependiendo si son de búsqueda de archivos o de búsqueda de impresoras
        les asignará un método u otro.'''

        TIPO = 2
        BOTON_AYUDA = 4

        for control in self.ui.lista_controles:
            if control[BOTON_AYUDA] != None and isinstance(control[BOTON_AYUDA], QPushButton):
                if control[TIPO] == "carpeta":
                    control[BOTON_AYUDA].clicked.connect(self.búsqueda_carpeta)
                elif control[TIPO] == "impresora":
                    control[BOTON_AYUDA].clicked.connect(self.búsqueda_impresora)
                else:
                    pass
    
    def pestaña_del_valor(self, nombre_dato, pestañas):
        '''Devuelve el nombre de la pestaña al que pertenece un determinado dato.'''
        for pestaña in pestañas:
            for valores in pestañas[pestaña]:
                if valores == nombre_dato:
                    return pestaña

    def procesar_datos(self):

        '''Analiza los datos introducidos por código en la lista de "lista_valores" y el diccionario "pestañas" referentes al archivo INI
        seleccionado. Construye controles según el nombre del dato, el tipo, el texto de ayuda y la función de validación introducida.
        Los separará en pestaña según el diccionario.'''

        # Lista de : [ nombre_del_dato, tipo_dato, texto_ayuda, función lambda de validación]
        lista_valores = [["nombre",str,"Por ejemplo: Jose Javier", None],["ingresos", float, "Por ejemplo: 15000",lambda ingresos: ingresos >= 10000 ],
        ["iban", int, "Por ejemplo: 464646", None],["parado",bool, "", None], ["hospital", str, "Por ejemplo: Casa de salut",None],
        ["citas", int, "Por ejemplo: 2",lambda citas: citas >= 0],["centro", str, "Por ejemplo: Los Naranjos",None],
        ["anyo", int,"Por ejemplo: 2021",lambda anyo: anyo >= 2000],["carpeta_notas", "carpeta", "Texto ayuda carpetas", lambda carpeta: carpeta != ""],
        ["impresora", "impresora", "Texto ayuda impresora", lambda impresora: impresora != ""]]
        pestañas = {'Cuenta corriente':['nombre', 'ingresos', 'iban', 'parado'], 'Datos médicos':['hospital', 'citas'], 'Escuela':['centro', 'anyo',
        'carpeta_notas', 'impresora']}
        try:
            config = configparser.ConfigParser()
            config.read('archivo_prueba.ini')
        except FileNotFoundError as err:
            sys.stderr.write('''
            Fallo al abrir el archivo
            Error: {}
            '''.format(err))
            exit(1)
        try:
            # Recorremos el archivo INI por secciones y por valores de cada sección
            for nombre_seccion in config:
                for nombre_valor in config[nombre_seccion]:
                    # Recorremos la lista de valores que queremos configurar/editar
                    for dato in lista_valores:
                        if dato[self.NOMBRE] == nombre_valor:
                            # contruir botón(tipo de dato, nombre del dato, valor actual del dato)
                            if dato[self.TIPO] == bool:
                                Ui_Dialog.construir_boton(self.ui, dato[self.TIPO], dato[self.NOMBRE], config.getboolean(nombre_seccion,nombre_valor), self.pestaña_del_valor(dato[self.NOMBRE], pestañas), dato[self.TEXTO_AYUDA], dato[self.VALIDACIÓN])
                                lista_valores.remove(dato)
                            else:
                                Ui_Dialog.construir_boton(self.ui, dato[self.TIPO], dato[self.NOMBRE], config[nombre_seccion][nombre_valor], self.pestaña_del_valor(dato[self.NOMBRE], pestañas),dato[self.TEXTO_AYUDA], dato[self.VALIDACIÓN])
                                lista_valores.remove(dato)
                            break
        
        except TypeError as err:
            sys.stderr.write('''
            Tipo de variables incorrecto, se espera: int, float, bool, str.
            Error: {}
            '''.format(err))
        except ValueError as err:
            sys.stderr.write('''
            Fallo en el casting de las varibles indicadas.
            Error:{}
            '''.format(err))

if __name__ == '__main__':
    app =QApplication(sys.argv)
    dialog = DiálogoConfiguraciónINI()
    DiálogoConfiguraciónINI.procesar_datos(dialog)
    DiálogoConfiguraciónINI.relacionar_botones(dialog)
    dialog.show()
    sys.exit(app.exec_())