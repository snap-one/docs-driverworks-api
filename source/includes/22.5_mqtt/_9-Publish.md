## Publish

The Publish API call allows a driver to send information to any other devices or programs that may be listening to the specified MQTT topic. When this call is called, an error code and message ID will be returned and the publish will happen in the background. Once the publish has completed (successfully or otherwise), the [OnPublish ][1]callback will be called with the message ID as a parameter and other status information.


###### Available from 4.0.0


### Signature

`Publish(topic, payload, qos, retain, mqttProps)`


| Parameters | Description                                                                                                                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| topic      | The MQTT topic that should be used to publish a message to.                                                                                                                                                                          |
| payload    | Optional. The payload that should be published to the named MQTT topic.                                                                                                                                                              |
| qos        | Optional. The Quality of Service value that should be used to publish this message. _See table below._                                                                                                                               |
| retain     | Optional. Boolean. If set to 'true' then the MQTT broker will retain the message for any future clients to see. If set to 'false' then the MQTT broker will publish the message to any subscribers that are listening at that point. |
| mqttProps  | Optional. Table. MQTTv5 properties that should be sent with this publish request.  _See table below._                                                                                                                                |


### Returns

On success an error code of 0 is returned with the 2nd return value being the message ID for the message that was published.  The 3rd return value is not returned in this case.  On error, a code other than 0 is returned with the 2nd return value being null, and the 3rd return value being a string that indicates information about why the call failed.

### Notes

If multiple publish requests are "in flight" at the same time, the message ID that is returned can be used with the [OnPublish ][2] callback to determine which message the success or failure maps to.

[1]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-onpublishhandler
[2]:	https://snap-one.github.io/docs-driverworks-api-4.0.0-beta/#mqtt-lua-apis-onpublishhandler