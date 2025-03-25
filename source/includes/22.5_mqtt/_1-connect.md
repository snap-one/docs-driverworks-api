## Connect

The Connect API call is used when a driver wants to make the initial connection to an MQTT broker.  It will attempt to connect based on the current state of the object.  As a result, things such as TLS settings and a user name and password should be set prior to making this call.


###### Available from 4.0.0


### Signature

`Connect(host, port, keepalive, mqttProps)`


| Parameters | Description                                                                                                            |
| ---------- | ---------------------------------------------------------------------------------------------------------------------- |
| host       | The IP address or DNS name of the MQTT broker that we want to communicate with.                                        |
| port       | Optional. The port that the MQTT broker we want to communicate with is listening on.                                   |
| keepalive  | Optional. The length of time between keepalive 'ping' messages.  In general, the default of 60 seconds should be used. |
| mqttProps  | Optional. Table. MQTTv5 properties to be sent along with the connection request.  _See table below._                   |


### Returns

0 on success.  On error, two values are returned.  The first value is a number indicating the error, the second is a string that describes the error.

### Notes

The Connect() call will return immediately, while the connection attempt proceeds in the background.  Once the connection has been established, the OnConnect() callback will be called with status for the connection.
