## GetBoundConsumerDevices

Call to retrieve the devices bound to (the consumers of) a binding provided (an output binding) by this device. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.

### Signature

`C4:GetBoundConsumerDevices ()`

| Parameter | Description |
| --- | --- |
| num | The id of the device to check the bindings on. |  
| num | Binding ID. |


### Usage Note
Note that for devices with a protocol and one or more proxy devices, the device id should be that of the proxy (not the lua protocol device id).  A device id of 0 will use the current device id.



### Returns

null if no bindings or a table of device id/device name pairs of bound devices.


### Examples

First get the proxy device id to check  on.  In this case, the 0 means this device, and the 5001 is the proxy id for the receiver.  

`C4:GetBoundConsumerDevices(0, 5001)`


```lua
if (devs ~= nil) then
 for id,name in pairs(devs) do
   --should be only one
   g_recProxyId = id
 end
end
```

Now that we have the device id of the receiver proxy device, check to see what is bound to binding id 2000: 

`C4:GetBoundConsumerDevices(g_recProxyId, 2000)`

```lua
if (devs ~= nil) then
 for id,name in pairs(devs) do
   print ("id " .. id .. " name " .. name)
 end
end

```

```lua
Output:
id 19 name Television
id 67 name Television2
```