## GetDevicesByName

Function used to obtain the Device ID and the Room ID assigned to a device in the project. This API should not be invoked during OnDriverInit.

###### Available from 2.8.0


### Signature

`C4:GetDeviceByName(str,str)`


| Parameter | Description |
| --- | --- |
| str |  Name of the Device in the project. |
| str |  Optional. Name of the Room where the Device resides. |


### Returns

| Value | Description |
| --- | --- |
| table |  Device ID and Room ID values. |
 

### Usage Note
The ID value returned for the Device is actually the Proxy ID.


### Example

`C4:GetDevicesByName("AV Switch","Theater")`
