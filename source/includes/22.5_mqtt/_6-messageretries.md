## SetMessageRetries

The SetMessageRetries API establishes the maximum number of times that the MQTT client will attempt to send a message before giving up.


###### Available from 4.0.0


### Signature

`SetMessageRetries (number)`


| Parameters | Description                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------- |
| number     | The maximum number of times that the MQTT client will attempt to send a message before giving up. |


### Returns

0 on success.  On error, two values are returned.  The first value is a number indicating the error, the second is a string that describes the error.
