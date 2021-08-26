# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerzaJOSh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Dialog(object):
    PESTAÑA = 0
    CONTROLES_EN_PESTAÑA = 1
    ERRORES_PESTAÑA = 2
    NOMBRE_PESTAÑA = 3

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(736, 408)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 360, 711, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, 10, 711, 341))
        #
        texto_rojo = QPalette()
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        texto_rojo.setBrush(QPalette.Active, QPalette.WindowText, brush)
        texto_rojo.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        texto_rojo.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.paleta_roja = texto_rojo
        #
        texto_gris = QPalette()
        brush = QBrush(QColor(154, 154, 154, 255))
        brush.setStyle(Qt.SolidPattern)
        texto_gris.setBrush(QPalette.Active, QPalette.WindowText, brush)
        texto_gris.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        texto_gris.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.paleta_gris = texto_gris
        #
        self.tabWidget.setCurrentIndex(1)

        self.lista_controles = []
        self.pestañas = []
        self.tab_error = None

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    
    def contruir_texto_error(self, panel, geometry, nombre_dato):
        '''Construye un texto de error en rojo. Inicialmente no se escribe nada. '''
        label_error = QLabel(panel)
        label_error.setObjectName("{}_error".format(nombre_dato))
        label_error.setGeometry(geometry)
        label_error.setText('')
        label_error.setPalette(self.paleta_roja)
        return label_error

    def construir_nombre_dato(self, nombre_dato, pestaña, geometry):
        '''Construye un texto a la izquierda del control, para indicar el dato al que pertenece.'''
        texto_info = QLabel(pestaña)
        texto_info.setObjectName(u"{}_info".format(nombre_dato))
        texto_info.setText("{}: ".format(nombre_dato.capitalize()))
        texto_info.setGeometry(geometry)
        texto_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        font = QFont()
        font.setPointSize(14)
        texto_info.setFont(font)

    def construir_texto_ayuda(self, nombre_dato, pestaña, geometry, texto):
        '''Contruye un texto gris de ayuda (introducido por la lista) debajo del control (QLineEdit).'''
        texto_ayuda = QLabel(pestaña)
        texto_ayuda.setObjectName(u"{}_help".format(nombre_dato))
        texto_ayuda.setText("{}".format(texto.capitalize()))
        texto_ayuda.setGeometry(geometry)
        font = QFont()
        font.setPointSize(9)
        texto_ayuda.setFont(font)
        texto_ayuda.setPalette(self.paleta_gris)

    def construir(self, tipo_dato, nombre_dato, valor_dato, nombre_pestaña, texto_ayuda,  validación):
        '''Constructor principal de los elementos de la pantalla. '''
        pestaña, numero_controles = self.pestaña_valor(nombre_pestaña)
        if tipo_dato == bool:
            control = QCheckBox(pestaña)
            control.setChecked(valor_dato)
            control.setText(nombre_dato)
        else:
            control = QLineEdit(pestaña)
            control.setText(valor_dato)
            control.setSelection(0,0)
            if tipo_dato == int:
                control.setValidator(QtGui.QIntValidator())
            elif tipo_dato == float:
                control.setValidator(QtGui.QDoubleValidator())
            else: 
                pass
        
        control.setObjectName(nombre_dato)
        y = 20 + numero_controles * 60
        control.setGeometry(QRect(150, y, 113, 20))
        font = QFont()
        font.setPointSize(10)
        control.setFont(font)
        
        self.construir_nombre_dato(nombre_dato, pestaña, QRect(20, y, 130, 40))
        self.construir_texto_ayuda(nombre_dato, pestaña, QRect(150, (y+20), 300, 20), texto_ayuda)
        # Dependiendo del tipo de dato, habrá botón búsqueda o no y la localización del texto de error cambiará.
        if tipo_dato == "impresora" or tipo_dato == "carpeta":
            control.setReadOnly(True)
            botón_busqueda = self.construir_boton_busqueda(nombre_dato, pestaña,  QRect((60 + 210), y, 50, 20))
            texto_error = self.contruir_texto_error(pestaña, QRect((120 + 210), y, 211, 20), nombre_dato)
        else:
            texto_error = self.contruir_texto_error(pestaña, QRect((60 + 210), y, 211, 20), nombre_dato)
            botón_busqueda = None
        
        self.lista_controles.append([control, texto_error, tipo_dato, validación, botón_busqueda]) 

    def construir_boton_busqueda(self, nombre_dato, pestaña, geometry):
        '''Construye un botón de búsqueda para los tipos "impresora" y  "carpeta". '''
        botón_busqueda = QPushButton(pestaña)
        botón_busqueda.setObjectName(u"{}_busqueda".format(nombre_dato))
        botón_busqueda.setGeometry(geometry)
        botón_busqueda.setText("Buscar")
        return botón_busqueda

    def pestaña_valor(self, nombre_pestaña):
        '''obtienen la pestaña y el nº de controles que tiene la pestaña a partir de un nombre común. '''
        for datos_pestaña in self.pestañas:
            if datos_pestaña[self.PESTAÑA].objectName() == nombre_pestaña:
                datos_pestaña[self.CONTROLES_EN_PESTAÑA] += 1
                return datos_pestaña[self.PESTAÑA], datos_pestaña[self.CONTROLES_EN_PESTAÑA]
        return self.construir_pestaña(nombre_pestaña)

    def construir_pestaña(self, nombre_pestaña):
        '''Construye una pestaña nueva a partir de un nombre y la guarda en la lista de pestañas. '''
        CONTROLES_EN_PESTAÑA = 0
        ERRORES_PESTAÑA = 0

        pestaña = QWidget()
        pestaña.setObjectName(u"{}".format(nombre_pestaña))
        
        self.tabWidget.addTab(pestaña, nombre_pestaña)
        self.pestañas.append([pestaña, CONTROLES_EN_PESTAÑA, ERRORES_PESTAÑA, nombre_pestaña])
        return pestaña, CONTROLES_EN_PESTAÑA
    
    def construir_boton(self, tipo_dato, nombre_dato, valor_dato, nombre_pestaña, texto_ayuda, validación):
        '''Evalúa que el tipo de variable sea correcto antes de construir el control. '''
        try:
            if tipo_dato == str or tipo_dato == int or tipo_dato == float or tipo_dato == bool or tipo_dato == "impresora" or tipo_dato == "carpeta":
                self.construir(tipo_dato, nombre_dato, valor_dato, nombre_pestaña, texto_ayuda, validación)
            else:
                raise TypeError
        except ValueError:
            raise ValueError

    def limpiar_texto(self, label):
        '''Hace desaparecer los textos de error que salen por los datos inválidos. '''
        if isinstance(label, QLabel):
            label.setText("")
        else:
            raise Exception

    def indicar_errores_pestaña(self, pestaña_con_error):
        '''Cada error detectado, suma 1 al nº de errores de la pestaña y sobreescribe el nombre. '''
        for lista_pestaña in self.pestañas:
            if lista_pestaña[self.PESTAÑA] == pestaña_con_error:
                lista_pestaña[self.ERRORES_PESTAÑA] += 1
                self.escribir_errores_pestaña(lista_pestaña)
                break

    def escribir_errores_pestaña(self, lista_pestaña):
        '''Comprueba si hay errores en una pestaña y si no hay escribe el nombre de la pestaña en negro y sin números, pero si 
        hay lo escribe en rojo y con el nº de errores entre paréntesis. '''
        índice_pestaña = self.tabWidget.indexOf(lista_pestaña[self.PESTAÑA])
        if lista_pestaña[self.ERRORES_PESTAÑA] == 0:
            self.tabWidget.setTabText(índice_pestaña, u"{}".format(lista_pestaña[self.NOMBRE_PESTAÑA]))
            self.tabWidget.tabBar().setTabTextColor(índice_pestaña,Qt.black)
        else:
            self.tabWidget.setTabText(índice_pestaña, u"{} ({})".format(lista_pestaña[self.NOMBRE_PESTAÑA], lista_pestaña[self.ERRORES_PESTAÑA]))
            self.tabWidget.tabBar().setTabTextColor(índice_pestaña,Qt.red)
            if self.tab_error == None:
                self.tabWidget.setCurrentIndex(índice_pestaña)
                self.tab_error = 1
            

    def limpiar_errores_pestañas(self):
        '''Pone a 0 el número de errores detectados en una pestaña y sobreescribe el nombre de la pestaña.'''
        self.tab_error = None
        for lista_pestaña in self.pestañas:
            lista_pestaña[self.ERRORES_PESTAÑA] = 0
            self.escribir_errores_pestaña(lista_pestaña)