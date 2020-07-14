## ServerCloseClient

Close a previously open Server Socket connection. This API should not be invoked during OnDriverInit.

###### Available from 2.10.0


### Signature

`C4:ServerCloseClient(nHandle)`	

| Parameter | Description |
| --- | --- |
| num | Server Socket handle received in [OnServerConnectionStatusChanged][1]. |


### Returns

`None`


### Example

This function closes the server socket previously received.

`C4:ServerCloseClient(nHandle)`

[1]:	https://control4.github.io/docs-driverworks-api/#onserverconnectionstatuschanged