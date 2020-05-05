## OnError

This method sets a callback method that will be called when an error occurs during an asynchronous operation.

###### Available in 1.6.0


### Signature

`C4:OnError(func)`


| Parameters | Description |
| --- | --- |
| func | should have this function signature: function(server, code, msg) |
| code | number with the system error code |
| msg | string with a description of the error |


### Returns

This method returns a reference to itself.