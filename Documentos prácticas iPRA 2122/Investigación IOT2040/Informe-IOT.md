# Informe IOT

## SIMATIC IOT 2040
Es una pasarela **inteligente** que estandariza la comunicación entre varias fuentes de datos, luego analiza y reenvía las comunicaciones a los correspondientes receptores, y es fácil de implementar.
Es ideal como **puerta de enlace entre la nube o el nivel de TI de la empresa y la producción**. La apertura del sistema permite soluciones personalizadas y numerosas posibilidades de programación en lenguajes de alto nivel.

  - Soporte Yocto Linux.
  - Fácilmente ampliable con Arduino.
  - Diseño industrial y montaje en rieles DIN.
  - Procesador Quark de Intel de alto rendimiento.
  - Amplia gama de opciones para programar.
  - Soluciones flexibles con diferentes protocolos, desde RTU hasta MTTQ/AMQP.
  - Uso de bibliotecas y ejemplos de código abierto.

El dispositivo *SIMATIC IOT 2040* ya tiene instalados **Node** y **Python** en la imagen ejemplo, por lo que se puede instalar muchas bibliotecas y paquetes sobre esas herramientas.

En caso de necesitar otro software de código abierto, por lo genereal se puede realizar una compilación cruzada con el complemento Eclipse. O se puede compilar directamente en el *IOT2040*. Otra opción sería construir tu propia imagen e incluir más software sobre recetas de Yocto.

## Conexión de SIMATIC IOT 2040 a través de Python

Para programar en Python no es necesario eclipse. Existen muchas bibliotecas de Python para usar comunicación basada en Ethernet:

- Para comunicación S7: <https://pypi.python.org/pypi/python-snap7/>
- Modbus TCP: <https://pypi.python.org/pypi/pymodbus3/1.0.0>
- TCP: <https://wiki.python.org/moin/TcpCommunication>
- UDP: <https://wiki.python.org/moin/UdpCommunication>

Se deben instalar las bibliotecas requeridas en su *IOT 2040* usando:
```script=
pip3 install <paquete>
```

 ### Código ejemplo para conectar un dispositivo (simulado) a un objeto de **AWS**:
 ```python = 
#!/usr/bin/python

# ejercicio 1 - Simulador de Dispositivo con Python.
# Asegurate que tu region tu hosts esten correctos. 

import sys
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
from datetime import datetime
import random


#Conigura tu MQTT cliente y tus certificados. Setup our MQTT client and security certificates
#Asegurate que el nombre de tus certificados coincida. 

mqttc = AWSIoTMQTTClient("1234")

#Debes pegar en Endpoint de tu dispositivo. 
#El endpoint se encuentra en el menu de la izquierda coniguracion -> punto de enlace y copias y pegas aca el link que aparece. 

mqttc.configureEndpoint("data.iot.us-west-2.amazonaws.com",8883)
mqttc.configureCredentials("./rootCA.pem","./privateKey.pem","./certificate.pem")

#Función para crear una carga útil en JSON


def json_encode(string):
        return json.dumps(string)

mqttc.json_encode=json_encode

#Aca enviamos nuestro mensaje a iot topic

def send():
    mqttc.publish("data", message, 0)
    print ("Mensaje Publicado")
    #conectando al gateway
mqttc.connect()
print ("Conectado")


#Loop until terminated
while True:
    now = datetime.now()
    #Declarando las variables
    message ={
    'ID': str(random.randint(0,10)),
    'Temperatura': random.randint(30,50),
    'Fecha': str(now.strftime("%Y-%m-%d %H:%M:%S")),
    'Evento': str(random.randint(100,500))
    }
    #decodificando el JSON
    message = mqttc.json_encode(message)
    print(message)
    send()
    time.sleep(5)

mqttc.disconnect()

#To check and see if your message was published to the message broker go to the MQTT Client and subscribe to the iot topic and you should see your JSON Payload
 ```

# Plataformas de gestión e interpretación de datos en la nube

## Ubidots:
Pulse [aquí](https://ubidots.com/) para acceder a la página web oficial.

Servicios que ofrece la plataforma:

- **SDK y API aptos para dispositivos**: Conectar hardware fácilmente a la nube de Ubidots con más de 200 librerías y tutoriales para guiar la integración a través de HTTP, MQTT, TCP, UDP o por "parseo de custom/industrial protocols".
- **Complementos de datos Entrada/Salida de datos de terceros**: Capacidad para crear una API propia y analizar los datos de una función HTTP GET o POST de la nube de Node.js.
- **Variables Sintéticas**: Transforman datos sin procesar en información mediante fórmulas matemáticas complejas y expresiones estadísticas.
- **Backend y almacenamiento de series temporales de dos años**
- **Live Dashboard**: Paneles a tiempo real utilizando tablas, gráficos, cuadros, widgets de control de Ubidots, pero con la posibilidad de utilizar código própio con plantillas HTML própias.
- **Informes programados**: Entrega de informes programados en PDF o en Excel.
- **Motor de Eventos**: Posibilidad de agregar lógica condicional y compleja con [webhooks](https://es.wikipedia.org/wiki/Webhook) para comunicación M2M y alertas SMS, correo electrónico, Telegram y Slack para mantener a los operadores informados.
- **Gestión de usuarios**: Posibilidad de asignar permisos y restricciones a cualquier usuario final u operador que interactúe con tableros, dispositivos y/o eventos.
- **Usabilidad**: Interfaces intuitivas y herramientas de desarrollo en la nube.
- **Posee una API para desarrolladores**: Esta [API](https://docs.ubidots.com/reference/welcome) se encuentra disponible desde la página web oficial y establece conexiones mediante _curl_ y objetos _json_. Un ejemplo:

``` script=
//Example Request to create a device with Token in the Header

curl -X POST 'https://industrial.api.ubidots.com/api/v2.0/devices/' \
 -H 'Content-Type: application/json' \
 -H 'X-Auth-Token: oaXBo6ODhIjPsusNRPUGIK4d72bc73' \
 -d '{}'
 
 
//Example Request to GET all devices with Token sent as Query Parameter
 
curl -X GET 'https://industrial.api.ubidots.com/api/v2.0/devices/?token=asdf657asdf675asdf876asdf' \
```

### Precios: [enlace](https://ubidots.com/pricing#)
| Tipo de Cuota | Mensualidad | Número de dispositivos | Rentención de datos |
|:---------------:|:-------------:|:------------------------:|:---------------------:| 
| Emprendedor IOT | 49$ | 25 | 2 años |
| Profesional | 199$ | 200 | 2 años |
| Industrial | 499$ | 1000 | 2 años |
| Empresa || Contactar |

## MindSphere - Siemens: 
Pulse [aquí](https://new.siemens.com/es/es/productos/software/mindsphere.html) para acceder a la página web oficial.

Beneficios que ofrece la plataforma:

- Desarrollo de soluciones industriales para el IoT más robustas y rápidas.
- PaaS abierto con accesibilidad a la nube nativa.
- Conectividad completa en todo tipo de entornos.
- Potente herramineta para el análisis inteligente de los datos.
- Ecosistema interactivo y disponible a nivel mundial.

Características:

- Ciberseguridad garantizada.
- Fácil desarrollo, implementación y prueba con soluciones preconfiguradas.
- Amplio espectro de API de MindSphere.
- Visualización y exploración de datos.
- Automatización de estadísticas con los datos de rendimiento gracias a [Product Intelligence](https://en.wikipedia.org/wiki/Product_intelligence).

No he encontrado información acerca de cuotas en la página web.