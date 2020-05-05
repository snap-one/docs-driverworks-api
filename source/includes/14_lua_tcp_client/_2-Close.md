
## Close

This method closes an established connection, or cancels a pending resolve or connection request. If a resolve or connection request is canceled, the OnError callback function will get called. This API should not be invoked during OnDriverInit. Once you call this method, no more data will be read from the socket and you can no longer write additional data to the socket. Also, the OnWrite callback will not be called anymore, even if the flush argument is set to true.

###### Available in 1.6.0


### Signature

`C4:Close(flush)`


| Parameters | Description |
| --- | --- |
| bool | flush: Value that indicates whether any queued-up write requests should be sent out prior to closing the connection. |
