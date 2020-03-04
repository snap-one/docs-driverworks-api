## GetDeviceVariables

Function used to obtain a Device's variables. This API should not be invoked during OnDriverInit.

###### Available from 2.8.0


### Signature

`C4:GetDeviceVariables()`


| Parameter | Description |
| --- | --- |
| num |  This is the Proxy ID or the Protocol ID assigned to the Device in the project. |


### Returns

| Value | Description |
| --- | --- |
| table | Table of all of the proxy variables or protocol variables for the Device (depending on the parameter passed) as well as all of the information for each of the variables. |

### Example

`C4:GetDeviceVariables(1000)`