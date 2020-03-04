
## OnError

This method sets a callback method that will be called when an error happens during an asynchronous operation.

###### Available in 1.6.0


### Signature

`C4:OnError(func)`


| Parameters | Description |
| --- | --- |
| func | Function should have this function signature:  function (server, code, msg)


### Usage Note

- server is this C4LuaTCPServer instance 
- code is a number with the system error code 
- msg is a string with a description of the error 
	  

### Returns

This method returns a reference to itself.