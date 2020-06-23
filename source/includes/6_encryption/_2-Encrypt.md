## Encrypt

```lua
local cipher = 'AES-256-CBC'
local key = 'Super Secret Key'
local iv = 'IV For C4'
local data = 'Hello World, this is London calling'
local options = {
	return_encoding = 'BASE64',
	key_encoding = 'NONE',
	iv_encoding = 'NONE',
	data_encoding = 'NONE',
	padding = true,
}
local encrypted_data, err = C4:Encrypt (cipher, key, iv, data, options)
print (type (encrypted_data), encrypted_data)
```

> Output:

```lua
string	HMQ9QXyBFUBnTAXBl2zi6k6abipQYQjpc37B0nA3WaxK9vBNrqKKAEzIglxWkA46
```

Encrypts a given string with the specified cipher, using the specified key and IV.

###### Available in 1.6.0.


### Signature

`C4:Encrypt (cipher, key, iv, data, options)`


| Parameter | Description |
| --- | --- |
| str | cipher: Valid cipher (see [GetSupportedCiphers][1]). |
| str | key : Valid key for specified cipher. Short keys will be padded, long keys will be rejected. |
| str | iv: Valid IV for specified cipher. Short IVs will be padded (including empty/nil IVs), long IVs will be rejected |
| str | data: Data to encrypt. |
| table | Options: (Optional) Options to specify encoding of inputs and outputs|

Valid key/value pairs for options parameter:

| Key | Description |
| --- | --- |
| str | return\_encoding:  return\_encoding: 'NONE' / 'HEX' / 'BASE64' |
| str | key\_encoding:  'NONE' / 'HEX' / 'BASE64' |
| str | iv\_encoding : 'NONE' / 'HEX' / 'BASE64’ |
| str | data\_encoding: 'NONE' / 'HEX' / 'BASE64' |
| bool | padding: True. Controls the padding requirements for the cipher used |



### Returns

`result, err`

A successful operation will return `nil` for *err*.  If an error occurs, then *result* will be nil and *err* will contain the description of the error.

|Value | Description|
| --- | --- |
| str | result: Encrypted data |
| str | err : Description of any error that occurred |


[1]:	#getsupportedciphers