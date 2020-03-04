## ServerCloseClient

Close a previously open Server Socket connection. This API should not be invoked during OnDriverInit.

###### Available from 2.10.0


### Signature

`C4:ServerCloseClient(nHandle)`	

| Parameter | Description |
| --- | --- |
| num | Server Socket handle received in OnServerConnectionStatusChanged. |


### Returns

`None`


### Example

This function closes the server socket previously received.

`C4:ServerCloseClient(nHandle)`