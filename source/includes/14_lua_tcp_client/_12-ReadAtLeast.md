
## ReadAtLeast

This method requests to read at least as many bytes as specified by the min argument. Once at least this amount of data is available, all available data is passed to the [OnRead][1] callback. This API should not be invoked during OnDriverInit.

###### Available in 1.6.0


### Signature

`C4:ReadAtLeast(min)`


| Parameters | Description |
| --- | --- |
| num | Number and must be greater than 0 and is currently limited to 1024 kb |
 

### Returns

This method returns a reference to itself, or nil in case of an error.

[1]:	https://control4.github.io/docs-driverworks-api/#onread