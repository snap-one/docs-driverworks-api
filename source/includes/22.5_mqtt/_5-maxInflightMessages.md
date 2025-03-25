## SetMaxInflightMessages

The SetMaxInflightMessages API establishes the maximum number of messages that can be "in flight" for the MQTT connection.


###### Available from 4.0.0


### Signature

`SetMaxInflightMessages (number)`


| Parameters | Description                                             |
| ---------- | ------------------------------------------------------- |
| number     | The maximum number of messages that can be "in flight”. |


### Returns

0 on success.  On error, two values are returned.  The first value is a number indicating the error, the second is a string that describes the error.
