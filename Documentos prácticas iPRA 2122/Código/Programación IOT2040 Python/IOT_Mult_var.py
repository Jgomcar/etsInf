from ast import If
from unittest.util import _PLACEHOLDER_LEN
from cliente_plc import *
import sys

import numpy as np

configuracion = {'ip': '192.168.1.205', 'direccion_dis': 0}
incrementar = True
contador = 5

#prueba
val = np.linspace(-np.pi, np.pi, 100)
valoresSin = list(map(lambda n : abs(int(n*100)), val))
crescendo = True
contador2 = 0

def main():
    plc_modbus = ClientePLCModbus(configuracion['ip'], direccion_dispositivo=configuracion['direccion_dis'])
    try:
        print('Conectando...')
        plc_modbus.conectar()
        print('Conectado con el autómata')

        try:

            print('Escribiendo...')
            # inicializo los datos a 0
            for x in range(0,12,4):
                plc_modbus.escribir_valor(0, x ,TipoDatos.entero_sin_signo)

            while (True):
                time.sleep(5)
                sierra(plc_modbus)
                incremento(plc_modbus)
                cuadrado(plc_modbus)
                sinusoidal(plc_modbus)
                print('Escritura realizada correctamente')

            

        except Exception as err:
            print ('ERROR:{}'.format(err))

    except PLCErrorComunicacion as err:
        print('ERROR:{}'.format(err))
    
    finally:
        plc_modbus.desconectar()

# Escribe del 0 al 100 en bucle cíclico
def sierra(plc_modbus):
    dato_0 = plc_modbus.leer_valor(0, TipoDatos.entero_sin_signo)
    if (dato_0 == 100): dato_0 = 0
    else: dato_0 = dato_0 + 1
    plc_modbus.escribir_valor(dato_0, 0, TipoDatos.entero_sin_signo)

# Escribe de 0 a 100 y vuelta, de 100 a 0
def incremento(plc_modbus):
    dato_4 = plc_modbus.leer_valor(4, TipoDatos.entero_sin_signo)
    global incrementar
    if (incrementar):
        dato_4 = dato_4 + 1
        if (dato_4 == 100): incrementar = not(incrementar)
    else:
        dato_4 = dato_4 - 1
        if(dato_4 == 0): incrementar = not(incrementar)
    plc_modbus.escribir_valor(dato_4, 4, TipoDatos.entero_sin_signo)

# Escribe el valor 0 o el valor 100 y los mantiene durante unos segundos
def cuadrado(plc_modbus):
    global contador
    if(contador == 0):
        dato_8 = plc_modbus.leer_valor(8, TipoDatos.entero_sin_signo)
        if (dato_8 == 0): dato_8 = 100
        else: dato_8 = 0
        plc_modbus.escribir_valor(dato_8, 8, TipoDatos.entero_sin_signo)
        contador = 20
    else: contador = contador - 1

# Escribe valores sinusoidales enteros
def sinusoidal(plc_modbus):
    global crescendo
    global valoresSin
    global contador2
    dato = valoresSin[contador2]
    print(dato)
    plc_modbus.escribir_valor(dato, 12, TipoDatos.entero_sin_signo)
    if(contador2 == 99):
        crescendo = False
    elif(contador2 == 0):
        crescendo = True
    if (crescendo):
        contador2 +=1
    else:
        contador2 -=1

if __name__ == '__main__':
    sys.exit(main())

