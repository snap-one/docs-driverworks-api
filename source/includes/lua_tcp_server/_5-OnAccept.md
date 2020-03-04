## OnAccept

This method sets a callback method that will be called whenever a new client connection has been accepted by the TCP server.

###### Available in 1.6.0


### Signature

`C4:OnAccept(func)`


| Parameters | Description |
| --- | --- |
| func | should have this function signature: function(server, client) |
| server | server is this C4LuaTCPServer instance |
| client | server is this C4LuaTCPServer instance |


### Returns

This method returns a reference to itself.