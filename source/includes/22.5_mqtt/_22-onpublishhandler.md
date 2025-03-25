## onPublishHandler

When the Publish API call is called, the attempt to publish data to the MQTT broker will start up in the background.  Once the publish attempt completes, the onPublishHandler will be called with a message ID and a reasonCode. The message ID that is provided will match the message ID returned from the [Publish][1] API call, allowing developers to match publish events against the calls that originated them. The reasonCode parameter will indicate the status of the attempt to publish the data.


###### Available from 4.0.0


### Signature

`onPublishHandler(mqttObject, msgId, reasonCode, message, mqttProps)`


| Parameters | Description                                                                                                                                          |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| mqttObject | The MQTT object that generated this callback.                                                                                                        |
| msgId      | The message ID that this event maps to.                                                                                                              |
| reasonCode | The reason code that describes the result of the attempt to publish.                                                                                 |
| message    | A string that explains the meaning of the value returned in the reasonCode.                                                                          |
| mqttProps  | When using MQTTv5, this will contain a table of any MQTT properties that are sent by the broker as part of the publish response.  _See table below._ |

### Event Callbacks

Use the `OnPublish(publishCallbackHandlerFunction)` call to establish a callback handler for information about published messages.

[1]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-publish