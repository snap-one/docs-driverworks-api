## Listen

This method starts a listen request to listen on a particular host/service.  Once the host/service has been resolved and an endpoint has been chosen, the [OnListen][1] callback function will be called. This indicates that the server is now ready to accept incoming connections.  If errors occur, the [OnError][2] callback function will be called instead. This API should not be invoked during OnDriverInit.

###### Available in 1.6.0


### Signature

`C4:Listen(host, service[, backlog])`


| Parameters | Description |
| --- | --- |
| host | IP address or host name to listen on.  It can also be one of these special values: `“*", "!all", or "!any”` |
| ”!local" or "!loopback" | Listens on the loopback device |
| service | port number or a string with the service (e.g. 80 or "http").  If this argument is 0, a random available port will be |
| chosen. |
|backlog | number indicating the size of the connection accept backlog. This argument is optional |


### Returns

This method returns a reference to itself, or nil in case of an error.

[1]:	https://snap-one.github.io/docs-driverworks-api/#onlisten
[2]:	https://snap-one.github.io/docs-driverworks-api/#onerror