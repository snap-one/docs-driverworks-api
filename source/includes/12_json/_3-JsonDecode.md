## JsonDecode

JSON function that takes data from the JSON formatted string message and decodes it into the Lua table. On success, this function returns a single value which is as designed. On failure, the function returns two
values:

1. nil
2. A string describing the error.

This API should not be invoked during OnDriverInit.


### Signature

`C4:JsonDecode(json)`


| Parameter | Description |
| --- | --- |
| json | A string containing the JSON to be decoded.An error will be raised if the string contains invalid JSON. The actual value returned depends on the value of the json parameter and can be any of the following: Number, String, Boolean, Table
| decodeNull | Optional. Boolean flag value indicating how null values are decoded. By default (false), null values are converted to an empty table. A value of true specifies that null values are decoded as a lightuserdata object with a value of null.


### Returns

A value decoded from the specified JSON string.


### Examples

Primitive
`C4:JsonDecode("{":number:":42}")`

The preceding example will return a Number with the value: 42. In most cases, however, the decoder will return a table. Consider the following code:

```
Table
local value  = '{"Contents":["Asia", "Africa", "North America", "South America", "Europe", "Australia"]}'
local Foo = C4:JsonDecode(value)

The preceding example produces the following Lua table:

local Foo = {
	"Continent" = {
		"Asia",
		"Africa", 
		"North America", 
		"South America", 
		"Europe", 
		"Australia"
	}
}
```