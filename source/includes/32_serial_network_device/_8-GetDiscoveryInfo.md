## GetDiscoveryInfo

Returns a table that contains the device's discovery information.

###### Available from 2.10.0

### Signature

`C4:GetDiscoveryInfo(idBinding)`

| Parameter | Description |
| --- | --- |
| num | Network Binding ID value for the identified device |


### Returns

Table that contains the discovery information.


### Example

```lua
info = C4:GetDiscoveryInfo(6001)

print(info["uuid"])
```



Usage Note: Return table values are based on the discovery mechanism of the device. Values included in the return table can include:

- uuid // SDDP DDDP UPNP
- host // SDDP
- ip // SDDP DDDP UPNP
- type // SDDP DDDP UPNP
- driver // SDDP     
- manufacturer // SDDP UPNP
- model // SDDP DDDP UPNP
- primary_proxy // SDDP
- proxies_ // SDDP
- make_ // DDDP
- sdk_class_ // DDDP
- name_ // UPNP
- description_ // UPNP
- location_ // UPNP



Note that C4:GetDiscoveryInfo() is not available at the time that OnDriverLateInit() is executed when Director is starting. Director doesn't startup it's discovery mechanism until well after late initialize, so providing discovery info at that point is not possible. It is recommended recommendation here is to listen for the [OnSDDPDeviceStatus (#78)][1] system event. This event includes the UUID by which the device was identified, and a boolean indicating whether the device is online. It's either that or set a timer and poll until GetDiscoveryInfo returns what you're looking for.

SDDP is a royalty-free technology that enables your device to be automatically detected by and added into customers’ Control4 systems. SDDP greatly reduces the potential for mistakes and time required for installations. Our 3,500+ dealers much prefer (and seek out) products with SDDP. SDDP is very simple to implement and we can assist you as needed.

[1]:	https://snap-one.github.io/docs-driverworks-api/#registering-for-system-events