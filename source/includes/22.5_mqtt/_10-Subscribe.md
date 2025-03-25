## Subscribe

The Subscribe API call allows a driver to subscribe to a topic (or topics if using a wild card).  Subscribing to a topic will cause the [OnMessage][1] callback to be called any time that a message is published to the specified topic.   The parameters of the OnMessage callback will contain the information about what was published.   When called, this call will return before the subscription has been created.   Once the subscription is created, the [OnSubscribe][2] callback will be called.   The OnSubscribe call back will have the message ID returned from this call to indicate which subscription call is being referenced.


###### Available from 4.0.0


### Signature

`Subscribe(sub, qos)`


| Parameters | Description                                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------- |
| sub        | The topic that this MQTT client would like to subscribe to.                                              |
| qos        | Optional. The Quality of Service value that should be used to subscribe to the topic. _See table below._ |
| mqttProps  | Optional. Table. MQTTv5 properties that should be sent with this publish request.  _See table below._    |


### Returns

On success an error code of 0 is returned with the 2nd return value being the message ID for the subscription request that is sent.  The 3rd return value is not returned in this case.  On error, a code other than 0 is returned with the 2nd return value being null, and the 3rd return value being a string that indicates information about why the call failed.

### Notes

If multiple subscription requests are "in flight" at the same time, the message ID that is returned can be used with the [OnSubscribe][3] to determine which subscription request the success or failure maps to.


[1]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-onmessagehandler
[2]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-onsubscribehandler
[3]:	https://snap-one.github.io/docs-driverworks-api-4.0.0-beta/#mqtt-lua-apis-onsubscribehandler