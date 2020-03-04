
## ReadUpTo

This method requests to read any available data up to (and including) the number of bytes specified by the max argument.  Once data is available, the OnRead callback will be called with whatever data was available, but no more than the limit specified in the max argument. This API should not be invoked during OnDriverInit

###### Available in 1.6.0


### Signature

`C4:ReadUpTo(max)`


| Parameters | Description |
| --- | --- |
| num | max  is a number and must be greater than 0 and it is currently limited to 4096 kb |


### Returns

This method returns a reference to itself, or nil in case of an error.