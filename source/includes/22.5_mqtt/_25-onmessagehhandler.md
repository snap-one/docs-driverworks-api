## onMessagehandler

When a subscribed topic gets a new message, the OnMessage API is called to indicate that a new message has been sent.


###### Available from 4.0.0


### Signature

`onMessageHandler(mqttObject, msgId, topic, payload, qos, retain)`


| Parameters | Description                                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------------------------- |
| mqttObject | The MQTT object that generated this callback.                                                                         |
| msgId      | The message ID that this event maps to.                                                                               |
| topic      | The topic that generated this message.                                                                                |
| payload    | The payload of the message that came in.                                                                              |
| qos        | The QoS level that this message was sent with.                                                                        |
| retain     | Indicates if this is a retained message, or not.                                                                      |
| mqttProps  | When using MQTTv5, this will contain a table of any MQTT properties that are part of the message.  _See table below._ |


### EventCallbacks

Use the `OnMessage(messageCallbackHandlerFunction)` call to establish a callback handler to get messages for subscriptions that this client has made.


### Notes

If your driver expects to do anything but publish messages, you must set a callback handler for OnMessage().  Failure to do so will result in not getting any of the messages that you have subscribed for.

