## SendIR

Function called from DriverWorks driver to send an IR Code. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:SendIR(idBinding,idIRCode)`


| Parameter | Description |
| --- | --- |
| num  | idBinding: IR Binding ID to send the IR Code. |
| num  | idIRCode: ID of the IR Code to send from .c4i |
| num  | idBinding:Proxy Binding ID. (optional) |


### Returns

`None`


### Usage Note

The IR code to send must be declared as an `<ircode\>` in the `<irsection\>` section of the driver  file.