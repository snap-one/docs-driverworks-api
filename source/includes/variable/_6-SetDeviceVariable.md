## SetDeviceVariable

Function called from a DriverWorks driver to set the value of another driver or device's variable. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:SetDeviceVariable(DeviceID, variableID, strValue)`	


| Parameter | Description |
| --- | --- |
| num |  ID value of the device |
| num |  ID of variable to set |
| str | Value to set variable |


### Returns

`None`


### Usage Note

User Variables belong to the Variable Agent, with a DeviceID of 100001.


### Examples

Sets the device variable value of the device with ID of 10 and variable ID of 1005 to 90:

`C4:SetDeviceVariable(10, 1005, 90)`
