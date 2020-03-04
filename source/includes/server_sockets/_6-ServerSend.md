## ServerSend

This function is used to send data over an open Server Socket connection. This API should not be invoked during OnDriverInit.

###### Available from 2.10.0


### Signature

`C4:ServerSend(nHandle, strData)`	

| Parameter | Description |
| --- | --- |
| num | Server Socket handle received in OnServerConnectionStatusChanged. Replies to or disconnects this same Server Socket. 
| str | Data to be sent over the open Server Socket connection. |


### Returns

`None`


### Example

This function shows sending data over a Server Socket:

`C4:ServerSend(nHandle, strData)`

