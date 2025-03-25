## onUnsubscribeHandler

When the Unsubscribe API call is called, the attempt to unsubscribe from a topic will start up in the background. Once the unsubscribe attempt completes, the onUnsubscribeHandler will be called with the message ID that maps back to the Unsubscribe call. This indicates that the client is no longer subscribed to the topic that was provided in the [Unsubscribe][1] API call.


###### Available from 4.0.0


### Signature

`onUnsubscribeHandler(mqttObject, msgId, mqttProps)`


| Parameters | Description                                                                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mqttObject | The MQTT object that generated this callback.                                                                                                                           |
| msgId      | The message ID that this event maps to.                                                                                                                                 |
| mqttProps  | When using MQTTv5, this will contain a table of any MQTT properties that are sent by the broker as part of the response to the unsubscribe request.  _See table below._ |

### Event Callbacks

Use the `OnUnsubscribe(unsubscribeCallbackHandlerFunction)'` call to establish a callback handler to determine the result of an unsubscribe request.

[1]:	https://snap-one.github.io/docs-driverworks-api-4.0.0-beta/#mqtt-lua-apis-unsubscribe