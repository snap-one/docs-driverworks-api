## OnResolve
This method sets a socket option.

###### Available in 1.6.0


### Signature

`C4:Option(name, value[, ...])`


| Parameters | Description |
| --- | --- |
| name | string specifying the option to set. It can be one of the following: 
| | ” reuseaddr" Enables or disables the socket's reuse address option based on the boolean value supplied in the value argument. |
| | ”linger": Enables or disables the sockets' linger option based on the boolean value supplied in the value argument.  This  option requires a 3rd argument of type number that indicates the timeout period (in seconds). |


### Returns

This method returns a reference to itself.