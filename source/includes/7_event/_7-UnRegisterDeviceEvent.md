## UnregisterDeviceEvent

This API unregisters prior event registration created by the [RegisterDeviceEvent][1] API. The device ID passed is the ID of the device that is firing the registered event. This is followed by the event ID.

###### Available in  2.9.0


### Signature

`C4:UnregisterDeviceEvent(deviceId, eventId)`


| Parameter | Description |
| --- | --- |
| num | Device ID value of the device firing the registered event. |
| num| ID value of the Event |


### Returns

`None`

[1]:	https://snap-one.github.io/docs-driverworks-api/#event-interface-registerdeviceevent