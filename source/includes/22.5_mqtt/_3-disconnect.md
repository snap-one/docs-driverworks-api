## Disconnect

The Disconnect API call is used to terminate the connection to the MQTT broker.


###### Available from 4.0.0


### Signature

`Disconnect(mqttProps)`


### Parameters

| Parameters | Description                                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------- |
| mqttProps  | Optional. Table. MQTTv5 properties that should be sent with the disconnect message.   _See table below._ |


### Returns

0 on success.  On error, two values are returned.  The first value is a number indicating the error, the second is a string that describes the error.

### Notes

The Disconnect() call will return immediately, and the disconnection status will be provided by the OnDisconnect() callback.
