## SetWill

The SetWill API call sets what is known as the "last will and testament" of an MQTT device.   If the connection to a device is terminated, the MQTT broker will publish this message to allow other subscribers to know that the device has disconnected.   In general, you should only use this if your driver is actively publishing information for others to consume, and the other devices need to be aware of when this driver loses connection unexpectedly with the MQTT broker.  The "last will and testament" is not set on a clean disconnect from the MQTT broker.

###### Available from 4.0.0


### Signature

`SetWill(topic, payload, qos, retain)`


| Parameters | Description                                                                                                                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| topic      | The MQTT topic that should be used to publish the will message.                                                                                                                                                                      |
| payload    | Optional. The payload that should be published to the will topic.                                                                                                                                                                    |
| qos        | Optional. The Quality of Service value that should be used to publish this message. _See table below._                                                                                                                               |
| retain     | Optional. Boolean. If set to 'true' then the MQTT broker will retain the message for any future clients to see. If set to 'false' then the MQTT broker will publish the message to any subscribers that are listening at that point. |


### Returns

0 on success.  On error, two values are returned.  The first value is a number indicating the error, the second is a string that describes the error.
