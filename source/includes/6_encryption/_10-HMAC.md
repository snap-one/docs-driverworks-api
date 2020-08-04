## HMAC


Computes a hash-based message authentication code ([HMAC][1]) for a given string using the specified key.

###### Available in 1.6.0.


### Signature

`C4:HMAC (digest, key, data, options)`


|Parameter | Description|
| --- | --- |
| str | digest: Valid digest (see [GetSupportedDigests][2]). |
| str | key: Key to use for computing HMAC. |
| str | data:	 Data to compute HMAC for. |
| table | options: (Optional) Options to specify encoding of inputs and outputs: |

Valid key/value pairs for options parameter:

| Key | Description |
| --- | --- |
| str | return\_encoding: 'NONE' / 'HEX' / 'BASE64' |
| str |  ey\_encoding: ‘NONE' / 'HEX' / 'BASE64' |
| str | data\_encoding’: ‘NONE' / 'HEX' / 'BASE64' |


### Returns

A successful operation will return `nil` for *err*.  If an error occurs, then *result* will be nil and *err* will contain the description of the error.

| Value | Description |
| --- | --- |
| str | result: Computed HMAC value |
| str |err: Description of any error that occurred |


### Example

```lua
local digest = 'SHA256'
local key = 'Super Secret Key'
local data = 'Hello World, this is London calling'
local options = {
	return_encoding = 'HEX',
	key_encoding = 'NONE',
	data_encoding = 'NONE',
}
local hmac_output, err = C4:HMAC (digest, key, data, options)
print (type (hmac_output), hmac_output)

> Output:

string	6402b5430d06db90c84e91a3ed605ba12964ff29e7bbd197b54109ac72aa58ce
```

[1]:	https://en.wikipedia.org/wiki/HMAC
[2]:	#getsupporteddigests