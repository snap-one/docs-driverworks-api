## SendToDevice

Function called from DriverWorks driver to send a Control4 CommandMessage to the specified Control4 device driver. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:SendToDevice(idDevice, strCommand, tParams, AllowEmptyValues logCommand))`


| Parameter | Description |
| --- | --- |
| num | Device ID of the driver you wish to send the command to. |
| str | Command to be sent |
| table | Lua table of parameters for the command. |
| bool | allowEmptyValues (T/F) Optional. Defaults to False. TRUE will allow for an empty string to be sent as a parameter value.  | 
| bool | logCommand Defaults to True.  False prevents this API’s content from being logged. |

### Usage Note
The logCommand parameter may be useful if sensitive data is being passed through the API and it is desirable for that data to not appear in logs.


### Returns

`None`


### Usage Note:
There are some limitations associated with network broadcasting. These include the inability for it to work beyond the local network. Messages are not broadcast to the Internet, for example. Also, there is no confirmation that the message was received.


### Example

Toggles the Light registered with the system as device 41:

```
C4:SendToDevice(41,"TOGGLE",{})
Ramps the Light registered with the system as device 41 to 60% over 3 seconds:
C4:SendToDevice(41,"RAMP_TO_LEVEL", {LEVEL = 60, TIME = 3000})
```