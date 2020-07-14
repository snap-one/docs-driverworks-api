## urlSetOption

This function changes the option specified in the option argument to the value provided. The options and their respective value parameters can be one of the two defined in the parameter section below. This API should not be invoked during OnDriverInit.

###### Available from 2.8.1.

### Signature

`C4:urlSetOption(option, value)`	

| Parameter | Description |
| --- | --- |
| num | Number of concurrent transfers allowed per host. |
| bool | pipelining. Sets whether HTTP pipelining should be enabled. | 

### Usage Notes

Note that if the concurrent transfers  value is being changed to anything other than 1, the "pipelining" option will automatically get disabled.

Note that If the pipelining boolean is being changed to true, the `max_host_connections` option will automatically be set. Changing this option will not have any effect until there are no active transfers running. Also, it will not apply to new transfers created until then. Once all transfers are completed, this setting will apply to any transfers created from that point on.  You can use the [C4:urlCancelAll()][1] method to cancel all transfers prior to setting this option, or you can use the [C4:urlGetTickets()][2] method to determine whether any transfers are currently pending.


### Returns

`None`


### Examples

`C4:urlSetOption("max_host_connections", 1)`

`C4:urlSetOption("pipelining", true)`


[1]:	https://control4.github.io/docs-driverworks-api/#urlcancelall
[2]:	https://control4.github.io/docs-driverworks-api/#urlgettickets