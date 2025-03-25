## onDisconnectHandler

When the session with the MQTT broker is disconnected, either by a call to the [Disconnect][1] API, or by an external event, the "onDisconnectHandler" will be called indicating the reason that the connection was disconnected. If your driver did not request the disconnection, it may want to start a timer to attempt to call the [Reconnect][2] API until a connection is established again.


###### Available from 4.0.0


### Signature

`onDisconnectHandler(mqttObject, reasonCode, message, mqttProps)`


| Parameters | Description                                                                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| mqttObject | The MQTT object that generated this callback.                                                                                                  |
| reasonCode | The reason code that explains why the MQTT session was disconnected.                                                                           |
| message    | A string that explains the meaning of the value returned in the reasonCode.                                                                    |
| mqttProps  | When using MQTTv5, this will contain a table of any MQTT properties that are sent by the broker as part of the disconnect.  _See table below._ |


### Event Callbacks

Use the `OnDisconnect(disconnectCallbackHandlerFunction)` call to establish a callback handler for disconnecting.

[1]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-disconnect
[2]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-reconnect