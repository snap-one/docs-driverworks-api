## onSubscribeHandler

When the Subscribe API call is called, the attempt to subscribe to a topic will start up in the background. Once the subscribe attempt completes, the onSubscribeHandler will be called with a message ID and an array of integer values that indicate the maximum QoS level that was granted for each of the subscriptions. In general, this array will only contain a single value, unless you have used a wild card in your subscription request.


###### Available from 4.0.0


### Signature

`onSubscribeHandler(mqttObject, msgId, grantedQoS, mqttProps)`


| Parameters | Description                                                                                                                                                              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mqttObject | The MQTT object that generated this callback.                                                                                                                            |
| msgId      | The message ID that this event maps to.                                                                                                                                  |
| grantedQoS | An single column table of QoS levels that indicate the maximum QoS level that was granted for each of the subscriptions.                                                 |
| mqttProps  | When using MQTTv5, this will contain a table of any MQTT properties that are sent by the broker as part of the response to the subscription request.  _See table below._ |

### Event Callbacks

Use the `OnSubscribe(subscribeCallbackHandlerFunction)` call to establish a callback handler for checking the success or failure of a subscription request.
