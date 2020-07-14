## GetDeviceMAC

Returns the MAC Address associated with a device that has already been identified in the Control4 Project. The API uses address resolution protocol (ARP) queries to lookup MAC hardware addresses. It will return a value of nil if the MAC address is not found in the controller's ARP tables. Considerations when using GetDeviceMAC include:

1. If a device responds to a search protocol (SSDP/SDDP/DDDP), a high probability exists that there will be an entry for the device in the ARP tables.
2. If a device doesn't respond to a search protocol, establishing a connection to the device is usually sufficient to ensure that there's an entry in the ARP tables.
3. If a device goes to sleep or is otherwise offline for any reason, then there is a low probability that there will be an entry in the ARP tables.

###### Available from 2.10.0


### Signature

`C4:GetDeviceMAC ()`


| Parameter | Description |
| --- | --- |
| num | Network Binding ID value for the identified device |


### Returns

Single MAC address.


### Example

```lua
local mac = C4:GetDeviceMAC(6001)
print(mac)
```

```lua
 The output would appear as:

 28:39:5E:45:1F:F7
```
