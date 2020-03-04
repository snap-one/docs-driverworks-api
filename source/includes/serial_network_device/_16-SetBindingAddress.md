## SetBindingAddress

Function that allows a TCP/IP device, with an existing connection, to use a different IP Address for connection purposes. This API can be used with both statically created connections (XML) as well as dynamically created ones. It is recommended that the NetConnect API is called after SetBindingAddress. This API should not be invoked during OnDriverInit.

###### Available from 2.8.0


### Signature

`C4:SetBindingAddress(idBinding, strIPaddress) `


| Parameter | Description |
| --- | --- |
| num | Binding ID of the existing network binding |
| str | New IP address for the connection |


### Returns

`None`


### Example

`C4:SetBindingAddress(6002, '192.168.1.225')`