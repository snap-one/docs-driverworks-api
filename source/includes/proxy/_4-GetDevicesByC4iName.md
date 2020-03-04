## GetDevicesByC4iName

Function that returns specific devices by .c4i (driver) name. For example, if passed `light_ip_control4_ldz-102-w-c4i `it will return a list of all Control4 Wireless dimmers in the project. This API should not be invoked during OnDriverInit.

###### Added in OS 1.6.0


### Signature

`C4:GetDevicesByC4iName()`


| Parameter | Description |
| --- | --- |
| str | Driver name |


### Returns

| Parameter | Description |
| --- | --- |
| table | Table of device IDs. |


### Example

```
local devs = C4:GetDevicesByC4iName("rf_internet.c4i")
	if (devs ~= nil) then
	   print("Devices:")
	   for k,v in pairs(devs) do print(k,v) end
	end
```