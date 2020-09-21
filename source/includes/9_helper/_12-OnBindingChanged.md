## OnBindingChanged

Function called by Director when a binding changes state (bound or unbound).

###### Available from 2.9.0


### Signature

`OnBindingChanged (idBinding, strClass, bIsBound, otherDeviceID, otherBindingID)`


| Parameter | Description |
| --- | --- |
| idBinding | ID of the binding whose state has changed. |
| str | Class of binding that has changed. A single binding can have multiple classes: COMPONENT, STEREO, etc. This indicates which has been bound or unbound. |
| bIsBound | Whether the binding has been bound or unbound. |
| otherDeviceID | This Device ID value represents the Device ID for the device that makes up the other half of this binding. |
| otherBindingID | This Binding ID value represents the Binding ID for the device represented by the otherDeviceID value in the parameter above. |


### Returns

`None`


### Usage Note

Protocol drivers do not get OnBindingChanged notifications for AV and Room bindings being bound, only  control type bindings (Serial, IR, etc.). It is intended to be used specifically for when serial bindings are made, so the driver knows it can send initialization, etc. to the now-connected device.