## Unsubscribe

The Unsubscribe API call allows a driver to unsubscribe from a topic (or topics if using a wild card).   Unsubscribing from a topic will cease calling [OnMessage][1] when new information is published to the topic.   Like other calls, this call will return before the unsubscribe has completed and will return a message ID.   When the unsubscribe has completed, the [OnUnsubscribe][2] callback will be called and it will be provided with the message ID for the unsubscribe request, along with status indicating the result of the unsubscribe attempt.


###### Available from 4.0.0


### Signature

`Unsubscribe(sub, mqttProps)`


| Parameters | Description                                                                                           |
| ---------- | ----------------------------------------------------------------------------------------------------- |
| sub        | The topic that this MQTT client would like to unsubscribe from.                                       |
| mqttProps  | Optional. Table. MQTTv5 properties that should be sent with this publish request.  _See table below._ |

### Returns

On success an error code of 0 is returned with the 2nd return value being the message ID for the subscription request that is sent.  The third return value is not returned in this case.  On error, a code other than 0 is returned with the 2nd return value being null, and the 3rd return value being a string that indicates information about why the call failed.

### Notes

If multiple unsubscribe requests are "in flight" at the same time, the message ID that is returned can be used with the [OnUnsubscribe][3] to determine which unsubscribe request the success or failure maps to.


[1]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-onmessagehandler
[2]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-onsubscribehandler
[3]:	https://snap-one.github.io/docs-driverworks-api-4.0.0-beta/#mqtt-lua-apis-onunsubscribehandler