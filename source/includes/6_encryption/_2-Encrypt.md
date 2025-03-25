## Encrypt

Encrypts a given string with the specified cipher, using the specified key and IV.

In conjunction with the release of O.S. 4.0.0, low level AES, Blowfish, Camellia, CAST, DES, IDEA, RC2, RC4, RC5 and SEED cipher functions have been deprecated and are no long supported with the C4:Encrypt function. As support for various cipher function can change in the future, it is recommended to review the release notes for OpenSSL 3.0: [https://openssl-library.org/news/openssl-3.0-notes/index.html][1]

###### Available in 1.6.0.
###### Updated in 4.0.0: End of life for low level cipher functions.

### Signature

`C4:Encrypt (cipher, key, iv, data, options)`


| Parameter | Description                                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------- |
| str       | cipher: Valid cipher (see [GetSupportedCiphers][2]).                                                             |
| str       | key : Valid key for specified cipher. Short keys will be padded, long keys will be rejected.                     |
| str       | iv: Valid IV for specified cipher. Short IVs will be padded (including empty/nil IVs), long IVs will be rejected |
| str       | data: Data to encrypt.                                                                                           |
| table     | Options: (Optional) Options to specify encoding of inputs and outputs                                            |

Valid key/value pairs for options parameter:

| Key  | Description                                                          |
| ---- | -------------------------------------------------------------------- |
| str  | return\\\_encoding:  return\\\_encoding: 'NONE' / 'HEX' / 'BASE64'   |
| str  | key\\\\\\\_encoding:  'NONE' / 'HEX' / 'BASE64'                      |
| str  | iv\\\\\\\_encoding : 'NONE' / 'HEX' / 'BASE64’                       |
| str  | data\\\\\\\_encoding: 'NONE' / 'HEX' / 'BASE64'                      |
| bool | padding: True. Controls the padding requirements for the cipher used |



### Returns

`result, err`

A successful operation will return `nil` for *err*.  If an error occurs, then *result* will be nil and *err* will contain the description of the error.

| Value | Description                                  |
| ----- | -------------------------------------------- |
| str   | result: Encrypted data                       |
| str   | err : Description of any error that occurred |

### Example

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

[1]:	https://openssl-library.org/news/openssl-3.0-notes/index.html
[2]:	https://snap-one.github.io/docs-driverworks-api/#encryption-interface-getsupportedciphers