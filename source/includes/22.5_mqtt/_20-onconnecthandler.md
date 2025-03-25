## onConnectHandler

When the [Connect][1] API call is called, an attempt to connect to the MQTT broker will start up in the background.  Once that connect attempt completes, the "onConnectHandler" will be called with a [reasonCode][2] and flags parameter. The reasonCode parameter will indicate the status of the connection. The flags parameter should generally be ignored.


###### Available from 4.0.0


### Signature

`onConnectHandler(mqttObject, reasonCode, flags, message, mqttProps)`


| Parameters | Description                                                                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| mqttObject | The MQTT object that generated this callback.                                                                                                  |
| reasonCode | The reason code that better explains what happened in the attempt to connect to the MQTT broker.                                               |
| flags      | Connection specific flags for this MQTT broker connection. Should generally be ignored.                                                        |
| message    | A string that explains the meaning of the value returned in the reasonCode.                                                                    |
| mqttProps  | When using MQTTv5, this will contain a table of any MQTT properties that are sent by the broker as part of the connection.  _See table below._ |

### Event Callbacks

Use the `OnConnect(connectCallbackHandlerFunction)` call to establish a callback handler for connecting.

[1]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-connect
[2]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-reason-codes-and-their-meanings