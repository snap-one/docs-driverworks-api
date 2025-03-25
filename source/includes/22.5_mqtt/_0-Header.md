# MQTT Interface

_Note: The Control4 hosted MQTT Server/Broker is not available to 3rd-party developers and there are no future plans to release it. This client API documentation is provided for the use of driver developers connecting to 3rd-party device(s) or service(s) that provide their own MQTT server/broker._

MQTT is a lightweight publish and subscribe messaging protocol that is intended to connect remote devices using small amounts of code and minimal network bandwidth. Considering there are more and more devices and services making use of MQTT, an MQTT client API for lua\_gen has been delivered.

Prior to using the delivered API, it is recommended that several tools be considered. These include:

**Eclipse Mosquito:**

[https://github.com/eclipse-mosquitto/mosquitto][1]

Mosquito is an open source implementation of a server for version 5.0, 3.1.1, and 3.1 of the MQTT protocol. It also includes a C and C++ client library, and the mosquitto\_pub and mosquitto\_sub utilities for publishing and subscribing.

**MQTT Explorer**

[https://github.com/thomasnordquist/MQTT-Explorer][2]

MQTT Explorer is an MQTT client that delivers a structured overview of MQTT topics and simplifies working with devices/services on your MQTT broker.

**MQTTX (alternative to MQTT Explorer)**

[https://mqttx.app/][3]

MQTTX is an MQTT client that delivers information about MQTT topics and allows publishing to topics.   The main difference between it and MQTT Explorer is the way the information is presented.  Some people prefer the format of
one over the other.

### Create an MQTT Object
In order to make use of the Control4 Lua API, it is necessary to  create an MQTT object.  Once the object has been created, it is possible to  call the API calls that are in the documentation below.

To create an MQTT object:

`myMqttObject = C4:MQTT("myclientname")`

The code above creates a new MQTT client object and assigns it an ID of "myclientname".   The client name must be unique or your driver will have issues with reconnecting constantly. However, you can also omit the client name and a randomly generated ID will be created for you.  It is recommended that if you do define a client name, that you use a value such as the device ID in order to keep the IDs unique in cases where a driver is loaded more than once in a project.

The object creation call can take up to two parameters :

| Parameters   | Description                                                                                                                                                                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| clientId     | Optional. The client ID that should be used with this MQTT session.  If it is not provided, the session will either use a null value or a randomly generated value. Whichever is appropriate for the MQTT broker that is being connected to. The clientId should be unique.    |
| cleanSession | Boolean. Optional. If set to true (the default) any old session data for this clientId will be removed from the broker when the session is connected. If it is false, the old session data will remain on the broker and the session with a matching clientId will be resumed. |

After the object has been created, the API calls defined in this section can be made against the object.



[1]:	https://github.com/eclipse-mosquitto/mosquitto
[2]:	https://github.com/thomasnordquist/MQTT-Explorer
[3]:	https://mqttx.app/