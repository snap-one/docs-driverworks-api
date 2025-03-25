## SendBroadcast

Function that enables a Lua driver to send network broadcast messages. The function opens a UDP connection, sets the `SO_BROADCAST` socket option and then sends a specified payload to the directed broadcast address. For example, 192.168.1.255. If the directed broadcast address is unavailable for any reason then the limited broadcast address is used instead, for example: 255.255.255.255.

This function must be used judiciously as there are network performance implications associated with its use. Network broadcasting requires that the router send the message to every device connected to the network. Overuse of this function can cause significant performance problems that affect the entire network.

###### Available from 2.10.0
###### Enhanced in 4.0.0 with sourcePort param


### Signature

`C4:SendBroadcast(payload, destinationPort, [sourcePort])`


| Parameter       | Type | Description                                                                                                                                                                                                                                                                                                                                                       |
| --------------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| payload         | str  | payloadA string containing the data to be broadcast. Note that there is risk of fragmentation for payloads that exceed the minimum guaranteed MTU size of 576 bytes. Nevertheless, fragmentation depends on many factor such as the configuration of networking gear, and the devices involved. We generally have no control over networking so plan accordingly. |
| destinationPort | num  | The destination port used for the broadcast. Note that the destination port is generally ignored because broadcasts are sent to all devices connected to the network, regardless of the port.                                                                                                                                                                     |
| sourcePort      | num  | Optional. The source port used for the broadcast. When given, the connection is bound to the "any" address (0.0.0.0) using the specified port. This ensures that the broadcast is sent from a specific port rather than an ethereal port.                                                                                                                         |


### Returns

`None`


### Usage Note:
There are some limitations associated with network broadcasting. These include the inability for it to work beyond the local network. Messages are not broadcast to the Internet, for example. Also, there is no confirmation that the message was received.


### Example

`C4:SendBroadcast("This is a message, 42) `
