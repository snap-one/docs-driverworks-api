## Close

This method stops the server socket, or cancels pending resolve or endpoint selection.  If a pending resolve or endpoint selection was canceled, the [OnError][1] handler will be called.  However, if the server is already accepting connections, the OnError handler will NOT be called and the server simply ceases to accept further connection requests.  Note that the server does not manage accepted client connections and will not close any of these connections. it it is up to your implementation to manage client connections and how to act when you stop the TCP server.

###### Available in 1.6.0


### Signature

`C4:Close()`


### Parameters

`None`


### Returns

This method returns a reference to itself, or nil in case of an error.


[1]:	https://snap-one.github.io/docs-driverworks-api/#tcpserver-interface-onerror