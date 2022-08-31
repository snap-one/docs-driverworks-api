## GetBoundProviderDevice

Call to retrieve what device is attached to an input binding of the specified device. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.

### Signature

`C4:GetBoundProviderDevice()`

| Parameter | Description |
| --- | --- |
| num | The id of the device to check the bindings on.  
| num | Binding ID. |


### Usage Note
Note that for devices with a protocol and one or more proxy devices, the device id should be that of the proxy (not the lua protocol device id).  A device id of 0 will use the current device id.


### Returns
null if no bindings or a table of device id/device name pairs of bound devices.


### Example

First get the proxy device id to check on. In this case, the 0 means this device and the 5001 is the proxy ID for the receiver. 

`C4:GetBoundConsumerDevices(0,5001)`

```lua
if (devs ~= nil) then
for id,name in pairs(devs) do
--should be only on g_recProxyId = id
end
end
-- the id 1011 is the video 2 input for this device
id = C4:GetBoundProviderDevice(g_recProxyId, 1011)
print("Id is " .. id)
```

```lua
Output:
Id is 44
```