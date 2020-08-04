## PBKDF2

Performs a Password-Based Key Derivation Function 2 (PKCS#5) ([PBKDF2][1]) for a given password using the specified digest, salt, number of iterations and desired output key length.

###### Available in 1.6.0.


### Signature

`C4:PBKDF2 (digest, password, salt, iterations, key_length, options)`


| Parameter | Description |
| --- | --- |
| str | digest: Valid digest (see [GetSupportedDigests][2]). |
| str | password: Input password to generate PBKDF2 output for |
| str | salt: Cryptographic salt to use |
| num | iterations: Number of iterations to run |
| num | key\_length:  Number of bytes to generate as output |
| table |options: (Optional) Options to specify encoding of inputs and outputs: |

Valid key/value pairs for options parameter:

|Key | Description |
| --- | --- |
| str | return\_encoding: 'NONE' / 'HEX' / 'BASE64' |
| str | salt\_encoding: ‘NONE' / 'HEX' / 'BASE64' |


### Returns

`result, err`

A successful operation will return `nil` for *err*.  If an error occurs, then *result* will be nil and *err* will contain the description of the error.

|Value | Description |
| --- | --- |
| str | result: Computed HMAC value |
| str | err : Description of any error that occurred |


### Example

```lua
local digest = 'SHA256'
local password = 'My Voice Is My Passport'
local salt = 'NaCl is one of many'
local iterations = 100000
local keyLen = 32
local options = {
	return_encoding = 'HEX',
	salt_encoding = 'NONE',
}
local pbkdf2_output, err = C4:PBKDF2 (digest, password, salt, iterations, keyLen, options)
print (type (pbkdf2_output), pbkdf2_output)

> Output:

string	12675672222506b342f05c0406f43e2af944bcb4ba592bf45e1c7cebad0fcdee
```

[1]:	https://en.wikipedia.org/wiki/PBKDF2
[2]:	#getsupporteddigests