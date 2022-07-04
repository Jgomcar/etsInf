from cliente_plc import *

def main():
    plc_modbus = ClientePLCModbus("192.168.1.205", direccion_dispositivo=0)
    try:
        print('Conectando...')
        plc_modbus.conectar()
        print('Conectado con el autómata')

        print('Escribiendo...')
            # inicializo los datos a 0
        plc_modbus.escribir_valor(5, 0 ,TipoDatos.entero_sin_signo)
        plc_modbus.escribir_valor(10, 4 ,TipoDatos.entero_sin_signo)
        plc_modbus.escribir_valor(15, 8 ,TipoDatos.entero_sin_signo)
        plc_modbus.escribir_valor(20, 12 ,TipoDatos.entero_sin_signo)
        plc_modbus.escribir_valor(25, 0 ,TipoDatos.entero_sin_signo)

        print('valor-1 =',plc_modbus.leer_valor(0, TipoDatos.entero_sin_signo))
        print('valor-2 =',plc_modbus.leer_valor(4, TipoDatos.entero_sin_signo))
        print('valor-3 =',plc_modbus.leer_valor(8, TipoDatos.entero_sin_signo))
        print('valor-4 =',plc_modbus.leer_valor(12, TipoDatos.entero_sin_signo))
    
    except Exception as err:
        print (err)
    
    finally:
        plc_modbus.desconectar()

if __name__ == "__main__":
    sys.exit(main())
    