## DestroyServer

Destroys any Server Sockets. This API should not be invoked during OnDriverInit.

###### Available from 2.10.0

### Signature

`C4:DestroyServer(nPort)`

| Parameter | Description |
| --- | --- |
| num |  TCP Port to stop listening on (Should be the same as initially given) |


### Examples

This function stops listening on all ports: 

`C4:DestroyServer()`

This function stops listening on port 8080: 

`C4:DestroyServer(8080)`