## GetProxyDevices

Function that returns the proxy device id(ids if device has multiple proxies) associated with the current driver. This API should not be invoked during OnDriverInit.

###### Added in OS 1.6.0


### Signature

`C4:GetProxyDevices(strName)`


### Parameters

`None`


### Returns

| Value | Description |
| --- | --- |
| num | Proxy ID |


### Example

```
local proxyId = C4:GetProxyDevices()
print("proxy is: " .. proxyId)

prints: proxy is: 393
```


