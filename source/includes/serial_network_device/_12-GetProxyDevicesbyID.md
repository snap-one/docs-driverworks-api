## GetProxyDevicesbyID

Returns the Proxy ID value when passed a Device ID value. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:GetProxyDevicesbyID (idDevice)`


| Parameter | Description |
| --- | --- |
| num | ID value of a device. Optional |


### Returns

| Value | Description |
| --- | --- |
num | Proxy ID value |


### Usage Note

Usage Note: If parameter passed is zero (0), this function will return the current Proxy ID for the driver selected in the Composer Project. If multiple proxies are associated with a device, the first Proxy ID displayed will be the first proxy as displayed in the Composer device tree.