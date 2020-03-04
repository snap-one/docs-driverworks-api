
## Option

This method sets a socket option. This API should not be invoked during OnDriverInit.

###### Available in 1.6.0


### Signature

`C4:Option(name, value[, ...])`


| Parameters | Description |
| --- | --- |
|str | Name is a string specifying the option to set.  It can be one of the following:
| | ”keepalive": Enables or disables the socket's keep-alive option based on the boolean value supplied in the value argument. |
| | ”nodelay": Enables or disables the socket's no-delay option based on the boolean value supplied in the value argument. |
| | ”linger": Enables or disables the sockets' linger option based on the boolean value supplied in the value argument.  This option requires a 3rd argument of type number that indicates the timeout period (in seconds). |
 

### Returns

This method returns a reference to itself, or nil in case of an error.