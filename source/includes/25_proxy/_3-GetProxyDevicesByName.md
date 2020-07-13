## GetProxyDevicesByName

Function that returns the all proxy devices by proxy name. For example, if passed light.c4i it will return a list of all lights in the project. This API should not be invoked during OnDriverInit.

###### Added in OS 1.6.0


### Signature

`C4:GetProxyDevicesByName()`


| Parameter | Description |
| --- | --- |
| str | Driver name |


### Returns

| Value | Description |
| --- | --- |
| str | Proxy name |


### Example

```lua
local proxydevs = C4:GetDevicesByC4iName("light.c4i")
if (proxydevs ~= nil) then
  print("Proxy Devices:")
  for k,v in pairs(proxydevs) do print(k,v) end
end
```