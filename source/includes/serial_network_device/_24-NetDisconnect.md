## NetDisconnect

Function called from DriverWorks driver to disconnect from a specific idBinding and nPort. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:NetDisconnect(idBinding, nPort)`


| Parameter | Description |
| --- | --- |
| num | Binding ID of the network interface to disconnect from |
| num | Network port. |


### Returns

`None`