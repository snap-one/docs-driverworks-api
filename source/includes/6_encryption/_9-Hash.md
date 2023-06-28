## Hash

Hashes a given string with the specified digest.

###### Available in 1.6.0.


### Signature

`C4:Hash (digest, data, options)`


| Parameter | Description | 
| --- | --- |
| str | digest: Valid digest (see [GetSupportedDigests][1]). |
| str | data: Data to hash. |
| table | options: (Optional) Options to specify encoding of inputs and outputs: |

Valid key/value pairs for options parameter:

| Key | Description |
| --- | --- |
| str | return encoding: 'NONE' / 'HEX' / 'BASE64' |
| str | data encoding:  'NONE' / 'HEX' / 'BASE64' |


### Returns

A successful operation will return `nil` for *err*.  If an error occurs, then *result* will be nil and *err* will contain the description of the error.

|Value | Description |
| --- | --- |
| str | result: Encrypted data |
| str | err : Description of any error that occurred |


### Example

```lua
local digest = 'SHA256'
local data = 'Hello World, this is London calling'
local options = {
	return_encoding = 'HEX',
	data_encoding = 'NONE',
}
local digest_output, err = C4:Hash (digest, data, options)
print (type (digest_output), digest_output)

> Output:

string	3fa83003c1c41282cac40d71b680d85f981f1517e5ac4941bd871955aeecbfec
```

[1]:	https://snap-one.github.io/docs-driverworks-api/#encryption-interface-getsupporteddigests