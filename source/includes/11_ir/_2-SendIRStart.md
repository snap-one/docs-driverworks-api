## SendIRStart

Causes Director to start sending the specified IR Code out the specified binding. This is typically used on button press events. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:SendIRStart(idBinding, idBinding, idIRCode)`


| Parameter | Description |
| --- | --- |	
| num | idBinding: Proxy Binding ID. |
| num | idBinding: Binding ID to send the IR Code. |
| num | idIRCode: Id of the IR Code to start sending from the driver. |


### Returns

`None`


### Usage Note

Failure to call the SendIRStop function will cause the IR code to be sent continually, which (in the case of
volume ramps) could be catastrophic to equipment. The IR code to send must be declared as an `<ircode\>` in the
`<irsection\>` of the driver file.


### Example

This example starts sending the specified IR Code out the specified IR Binding:

`C4:SendIRStart(1, 22)`	