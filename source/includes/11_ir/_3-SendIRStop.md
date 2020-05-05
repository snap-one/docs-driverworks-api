## SendIRStop

Causes Director to stop sending the specified IR Code out the specified binding. This is typically used on button release events. This API can be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:SendIRStop(idBinding,idBinding, idIRCode)`


| Parameter | Description |
| --- | --- | 
| num | idBinding: Proxy Binding ID. |
| num | idBinding: Binding ID to send the IR Code. |
| num | idIRCode: Id of the IR Code to start sending from the driver file. |


### Returns

`None`


### Usage Note

Usage Note: The IR code to send must be declared as an `<ircode\>` in the `<irsection\>` section of the driver file.


### Example

This example stops sending the specified IR Code out the specified IR Binding:

`C4:SendIRStop(1, 22)`