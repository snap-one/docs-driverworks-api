
## ReadUntilOneOf

This method requests to read data until (and including) one of the bytes in the str argument is encountered. This API should not be invoked during OnDriverInit.

###### Available in 1.6.0


### Signature

`C4:ReadUntilOneOf(str)`


| Parameters | Description |
| --- | --- |
|str | string with all bytes that can trigger a match. This argument cannot be an empty string. |


### Returns

This method returns a reference to itself, or nil in case of an error.