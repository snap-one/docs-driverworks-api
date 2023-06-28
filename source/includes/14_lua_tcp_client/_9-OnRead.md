
## OnRead

This method sets a callback method that will be called once data has been read on the socket.  If you would like to keep reading more data, you should call one of the Read() methods prior to returning from this callback function.

###### Available in 1.6.0


### Signature

`C4:OnRead(func)`


| Parameters | Description |
| --- | --- |
| func | Function should have this function signature:  function (client, data) |


### Usage Note

- client is this C4LuaTCPClient instance
- data is a string with the data that has been read. This can also be any object if you used the [ReadUntil][1]() method with a custom function that returns an object (e.g. pre-parsed data).


### Returns

This method returns a reference to itself.

[1]:	https://snap-one.github.io/docs-driverworks-api/#tcpclient-interface-readuntil