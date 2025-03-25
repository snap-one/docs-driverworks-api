## Reconnect

The Reconnect API will attempt to reconnect to the MQTT broker, using the same configuration as the original Connect request, after a session has been terminated.  Driver developers should delay a few seconds after a connection is broken before issuing a Reconnect in order to avoid flooding the network with reconnect attempts. It is highly recommended to implement an exponential backoff algorithm for reconnecting.


###### Available from 4.0.0


### Signature

`Reconnect()`


### Parameters

None


### Returns

0 on success.  On error, two values are returned.  The first value is a number indicating the error, the second is a string that describes the error.
