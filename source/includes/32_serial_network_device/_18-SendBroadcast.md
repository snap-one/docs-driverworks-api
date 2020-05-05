## SendBroadcast

Function that enables a Lua driver to send network broadcast messages. The function opens a UDP connection, sets the `SO_BROADCAST` socket option and then sends a specified payload to the directed broadcast address. For example, 192.168.1.255. If the directed broadcast address is unavailable for any reason then the limited broadcast address is used instead, for example: 255.255.255.255.

This function must be used judiciously as there are network performance implications associated with its use. Network broadcasting requires that the router send the message to every device connected to the network. Overuse of this function can cause significant performance problems that affect the entire network.

###### Available from 2.10.0


### Signature

`C4:SendBroadcast(payload, port))`


| Parameter | Description |
| --- | --- |
| str | Payload of the message to be broadcast | 
| num | Port identifying the port to which the payload is broadcast. |


### Returns

`None`


### Usage Note:
There are some limitations associated with network broadcasting. These include the inability for it to work beyond the local network. Messages are not broadcast to the Internet, for example. Also, there is no confirmation that the message was received.


### Example

`C4:SendBroadcast("This is a message, 42) `
