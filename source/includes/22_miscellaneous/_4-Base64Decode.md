## Base64Decode

Function called in a DriverWorks driver to decode the specified string from a Base64-encoded string. This API can be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:Base64Decode(strToDecode)`


| Parameters | Description |
| --- | --- |
| str | String to be decoded from [Base64 encoding][1] |


### Returns

| Value | Description |
| --- | --- |
| str | Decoded from Base64 encoding. |

[1]:	https://snap-one.github.io/docs-driverworks-api/#miscellaneous-interface-base64encode