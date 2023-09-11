## GetProxyDevicesById

Function that returns all associated proxies for a device. Return values are in ID format (numerical value). This API should not be invoked during OnDriverInit.

###### Added in OS 1.6.0


### Signature

`C4:GetProxyDevicesById()`


| Parameter | Description |
| --- | --- |
| num | Device ID |


### Returns

| Value | Description |
| --- | --- | 
| num | Proxy ID |


### Example

```lua
dev1, dev2, dev3 = C4:GetProxyDevicesById(C4:GetDeviceID())
C4:GetProxyDevicesById(C4:GetDeviceID())
print("dev1 is " .. dev1)
print("dev2 is " .. dev2)
print("dev3 is " .. dev3)
```
