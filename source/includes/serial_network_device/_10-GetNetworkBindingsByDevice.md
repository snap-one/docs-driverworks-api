## GetNetworkBindingsByDevice

Function that returns network binding information for a device. Related: See GetBindingsByDevice

###### Available from 3.0.0

### Signature

`C4:GetNetworkBindingsByDevice()`


| Parameter | Description |
| --- | --- |
| num | The id of the device returning network binding information. |


### Usage Note

Note that for devices with a protocol and one or more proxy devices, the device id should be that of the proxy (not the .lua protocol device id). A device id of 0 will use the current device id.


### Returns
Network Binding information for the device.


### Example

`C4:GetNetworkBindingsByDevice(20)`

Returns:

```
deviceid: 20
type: 1
autobind: false
class: RS_232
1: Serial3X
rank: 0
bindingid: 15
binding_info: 
flags: 0
isbound: false
name: SERIAL 3
provider: true

deviceid: 20
type: 1
autobind: false
class: IR_OUT
1: Serial4X
rank: 0
bindingid: 401
binding_info: 
flags: 0
isbound: false
name: IR OUT 2
provider: true
```