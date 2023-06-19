## RenameDevice

The ReNameDevice API supports the ability to rename a device that is currently in a Control4 project from a driver. This API can be also called from a driver other than that of the device's. This supports that ability to rename project devices externally. This API should not be invoked during OnDriverInit.


###### Available from 1.6.0


### Signature

`C4:RenameDevice(proxyId, name)`
or
`C4:RenameDevice(deviceId, name)`


| Parameter | Description |
| --- | --- |
| num | The Proxy ID value of the device being renamed |
| num | Device ID of the device being renamed. |
| str | New device name. |


### Returns

`None`


### Usage Note

Note that ComposerPro shows the Proxy Device and not the protocol drivers id.  In most cases, the Lua Driver’s deviceId is the protocol ID and is probably not the id to be changed. When this API is executed it will refresh the project. This API works if called in OnDriverLateInit. It will not work in onDriverInit.


### Example

`C4:RenameDevice(9, "Testing")`