## RegisterDeviceEvent

This API allows for a driver to register for another driver's event. The device ID passed is the ID of the device that is firing the event of interest. This is followed by the event ID.

###### Available in  2.9.0


### Signature

`C4:RegisterDeviceEvent(deviceID,eventID)`


| Parameter | Description |
| --- | --- |
| num | Device ID value of the device firing the event |
| num | ID value of the Event |


### Returns

`None`


### Usage Note

Knowledge of device event ID values are required to use this API in a driver. For this reason, the use of this API is intended for event registration between two drivers which have been created in support of one another. For example, this API would be useful in a network driver that wishes to know events fired by one of its module drivers.
