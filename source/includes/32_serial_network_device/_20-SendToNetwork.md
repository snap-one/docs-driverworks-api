## SendToNetwork

Function which sends an HTTP request to a network binding / port. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:SendToDevice(idDevice, strCommand, tParams, logCommand))`


| Parameter | Description |
| --- | --- |
| num | Binding ID of the network interface to send on |
| num | Network port to send on |
| str | Data to send out the specified network interface |


### Returns

`None`


### Usage Note:

Data to be sent can contain NULL characters. NULL (‘\0’) is a valid character and Lua strings handle embedded NULL characters. 


### Example

`C4:SendToNetwork(6001, 80, g_URLPacket)`