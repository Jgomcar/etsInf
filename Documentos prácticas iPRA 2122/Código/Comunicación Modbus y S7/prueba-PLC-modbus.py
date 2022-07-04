from cliente_plc import *
import sys
import random

configuracion = {'ip': '192.168.1.205', 'direccion_dispositivo': 0}

def main():
    plc_modbus = ClientePLCModbus(configuracion['ip'], direccion_dispositivo=configuracion['direccion_dispositivo'])
    
    try:
        print('Conectando...')
        plc_modbus.conectar()
        print('Conectado con el autómata')

        try:

            print('Escribiendo...')
            # plc_modbus.escribir_valor(120, 0 ,TipoDatos.entero_sin_signo)
            # plc_modbus.escribir_valor(8, 8 ,TipoDatos.entero_sin_signo)
            # plc_modbus.escribir_valor(65, 12 ,TipoDatos.entero_sin_signo)
            # plc_modbus.escribir_valor(47, 24 ,TipoDatos.entero_sin_signo)
            # for x in range(0,50,2):
            #     plc_modbus.escribir_valor(random.randint(0,2000), x ,TipoDatos.entero_sin_signo)


            print('Escritura realizada correctamente')
            print('Leyendo...')

            mapa_variables = {
                'int1':'w0',
                'int2':'w8',
                'int3':'w12',
                'int4':'w24'
            }

            plc_modbus.mapear_variables(mapa_variables)

            # print('valor-1 =',plc_modbus.leer_valor(0, TipoDatos.entero_sin_signo))
            # print('valor-2 =',plc_modbus.leer_valor(8, TipoDatos.entero_sin_signo))
            # print('valor-3 =',plc_modbus.leer_valor(12, TipoDatos.entero_sin_signo))
            # print('valor-4 =',plc_modbus.leer_valor(24, TipoDatos.entero_sin_signo))

            for x in range(0,50,2):
                print('valor-{} = {}'.format( x//2 , plc_modbus.leer_valor(x, TipoDatos.entero_sin_signo) ))
            
            nuevo_mapa_variables = plc_modbus.leer_mapa_variables()

            for clave, valor in nuevo_mapa_variables.items():
                print(clave, ' = ', valor)

        except Exception as err:
            print ('ERROR:{}'.format(err))

    except PLCErrorComunicacion as err:
        print('ERROR:{}'.format(err))
    
    finally:
        plc_modbus.desconectar()

if __name__ == '__main__':
    while (True):
        main()
        time.sleep(5)