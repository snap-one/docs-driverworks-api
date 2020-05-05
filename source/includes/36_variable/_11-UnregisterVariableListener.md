## UnregisterVariableListener

Function called from DriverWorks driver to remove a listener on a particular device's variable. Variable changes for the particular Device's Variable will no longer be reported. This API will not work if a variable has not been registered, added or does not exist.

###### Available from 1.6.0.


### Signature

`C4:UnregisterVariableListener(idDevice, idVariable)`


| Parameter | Description |
| --- | --- |
| num | Device ID of the device that owns the requested variable |
| num | Variable ID of the  requested variable |


### Returns

`None`


### Usage Notes

User Variables belong to the Variable Agent, with a DeviceID of 100001.T


### Example

This stops the system from reporting variable value changes for the specified device and variables:

```
C4:UnregisterVariableListener(84, 1000)
C4:UnregisterVariableListener(84, 1003)
C4:RegisterVariableListener(100001, 209
```