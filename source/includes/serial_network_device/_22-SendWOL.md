## SendWOL

Function that enables a Lua driver to broadcast a Wake-On-Lan magic packet. 

###### Available from 2.10.0

### Signature

`C4:SendWOL(macAddress, port) `


| Parameter | Description |
| --- | --- |
| macAdress | MAC address of the device. |
| num | Optional. ID of the port the WOL magic packet is broadcast. If omitted, the WOL default port 9 is used. |

### Usage Note

The MAC address parameter can be formatted in one of two ways: 
Using a colon character (:) to delineate the six numeric values. For example: 00:0a:95:9d:68:16 
or
Using no delimiter: 000a959d6816


### Returns

`None`


### Usage Note:

Although using WOL can be useful for devices that do not provide a full network stack when powered off, there are some limitations:
- Many network devices do not support Wake-On-Lan.
- Requires that the MAC address of the destination device is known.
- Does not work over WiFi.
- Does not work beyond the local network (i.e., the Internet).
- Does not provide confirmation that the intended device received the message.


### Examples

`C4:SendWOL("00:0a:95:9d:68:16")`

In the example above, the port argument is omitted. The WOL magic packet is broadcast on port 9 which is default.

`C4:SendWOL("000a959d6816", 42)`

The example above broadcasts the WOL magic packet on port 42.
