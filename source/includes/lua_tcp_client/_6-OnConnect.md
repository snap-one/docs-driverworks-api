
## OnConnect

This method sets a callback method that will be called once the endpoint has been chosen and the connection is successfully established.

###### Available in 1.6.0


### Signature

`C4:OnConnect(func)`


| Parameters | Description |
| --- | --- |
| func | Function should have this function signature: function(client). The client is this C4LuaTCPClient instance |


### Returns

This method returns a reference to itself.