## OnBindingChanged

Converts the numeric value passed in to network byte order. This API can be invoked during OnDriverInit.

###### Available from 1.6.0

### Signature

`C4:OnBindingChanged(idBinding, strClass, bIsBound, otherDeviceID, otherBindngID) `


| Parameter | Description |
| --- | --- |
| num | ID of the binding whose state has changed |
| str | Class of binding that has changed. A single binding can have multiple classes: COMPONENT, STEREO, etc |
| bool | Whether the binding has been bound or unbound. |
| num | ID value representing the device that IS NOT the Device who's Binding ID is the first parameter for this API. |
| otherBindingID | Binding ID  for the device represented by the otherDeviceID value in the parameter above. |


### Returns

`None`


### Usage Note

Protocol drivers do not get OnBindingChanged notifications for AV and Room bindings being bound, only  control type bindings (Serial, IR, etc.). It is intended to be used specifically for when serial bindings are made, so the driver knows it can send initialization, etc. to the now-connected device.
