## onLogHandler

Any time during the lifetime of the MQTT object, it may generate log information. When log information is generated, the onLogHandler callback is called.


###### Available from 4.0.0


### Signature

`onLogHandler(mqttObject, level, logLine)`


| Parameters | Description                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------- |
| mqttObject | The MQTT object that generated this callback.                                                       |
| level      | An integer that indicates the log level that this message should be logged with. _See table below._ |
| logLine    | A string that contains the log message that was generated.                                          |


### Event Callbacks

Use the `OnLog(logCallbackHandlerFunction)` call to establish a callback handler to get lower level log message about the status of the MQTT connection for your driver.


### Log Levels

| Log Level ID | Log Level Name |
| ------------ | -------------- |
| 0            | FATAL          |
| 1            | ERROR          |
| 2            | WARNING        |
| 3            | INFO           |
| 4            | DEBUG          |
| 5            | TRACE          |
