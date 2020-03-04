
## OnDisconnect

This method sets a callback method that will be called when the client gets disconnected.

###### Available in 1.6.0


### Signature

`C4:OnDisconnect(func)`


| Parameters | Description |
| --- | --- |
| func | Function should have this function signature:  function (client, errCode, errMsg) |

### Usage Note

- client is this C4LuaTCPClient instance. 
- errCode is a number with an error code, if the connection was disconnected due to an error. If the connection was disconnected  gracefully, this value will be 0. 
- errMsg is a string with a description of the error indicated by errCode. 


### Returns

This method returns a reference to itself.