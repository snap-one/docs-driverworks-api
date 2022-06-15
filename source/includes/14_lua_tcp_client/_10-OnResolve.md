
## OnResolve

This method sets a callback method that is called once the host/service has been resolved.  If implemented, it allows you to choose a particular endpoint to connect to, or to cancel the connection request.

###### Available in 1.6.0


### Signature

`C4:OnResolve(func)`


| Parameters | Description |
| --- | --- |
| func | Function should have this function signature:  function(client, endpoints, choose) |


### Usage Note

- client is this C4LuaTCPClient instance
- endpoints is an array of endpoint tables, describing all endpoints that the host/service could be resolved to. Each entry has the following fields:  ip (string): The IP address to connect to and  port (number) -  The port number to connect to
- choose is a completion function with this signature:

`function([index])`

Using this closure is optional and can be used to delay making a choice. The index argument is of type number, and it is optional.  If not provided, default behavior is requested (first endpoint, if available). If the index argument is provided, it should be an index into the endpoints array.  If the index argument is 0, the listen request will be canceled and the [OnError][1] callback will be called with an invalid argument error (code 22). func may return a number value that describes the index into the endpoints array, which will be the endpoint that the server should listen on. If this value is 0, the listen request will be canceled and the OnError callback will be called with an invalid argument error (code 22). If the function doesn't return anything, default behavior is chosen unless the choose function is being used to delay making a choice.  Note that if you call the choose function prior to returning from this callback function, that choice will be used rather than whatever the callback may return (if anything). Also, note that modifying the endpoints array (or any table in it) in any way has no effect.|


### Returns

This method returns a reference to itself.

[1]:	https://snap-one.github.io/docs-driverworks-api/#onerror