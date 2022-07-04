from cgi import print_arguments
import time
import cliente_plc
from asyncua import ua



if __name__ == "__main__":
    url = "opc.tcp://DESKTOP-K4TC5QG:53530/OPCUA/SimulationServer"
    cliente_plc_opcua = cliente_plc.ClientePLCOpcUa(url=url)

    try:
        print('Conectando...')
        cliente_plc_opcua.conectar()
        print('Conectado')
        print('Leyendo Valores:')
        for x in range(1,10):
            var_random1 = cliente_plc_opcua.leer_valor(5,"Ran1dom1")
            print("\tvar_random1 - {}: {}".format(x,var_random1))
            time.sleep(1)
    except cliente_plc.PLCErrorOpcUa as e:
        print('Error: ',e, ' \nCódigo de error: ', e.codigo)
    except Exception as e:
        print('Error: ',e)

    finally:
        cliente_plc_opcua.desconectar()