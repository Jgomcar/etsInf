from asyncua.sync import Client
from asyncua import ua as ua

if __name__ == "__main__":

    url_servidor = "opc.tcp://DESKTOP-K4TC5QG:53530/OPCUA/SimulationServer"
    cliente = None
    try:
        cliente = Client(url_servidor)
        cliente.connect()

        var_random1 = cliente.get_node("ns=5;s=Random1")
        # var_random1 = cliente.get_node("i=8888")
        print("random1 como DataValue: ", var_random1.read_data_value())
        print("random1 como valor Python: ", var_random1.read_value())

    except Exception as e:
        print("Error {}: {}".format(e.__class__.__name__, e))
    finally:
        if cliente:
            cliente.disconnect()