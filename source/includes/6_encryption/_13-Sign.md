## Sign

Sign enables drivers to crypto-graphically sign an arbitrary payload using a specified key.  The API currently supports both HMAC & RSA signing. Control4 strongly recommends that driver developers implement this new API beginning with OS Release 3.1.0. This API is the best solution to cryptographically sign a payload. Control4 recommends its use rather than other Lua libraries.

###### Available in 3.1.0.


### Signature

`C4:Sign(operation, digest, key, data, [options])`


| Parameter | Description | 
| --- | --- |
| str | Specifies which signing operation to perform. Valid values are: **HMAC:** Use the HMAC (hash-based message authentication code) signing algorithm. **RSA:** Use the RSA (Rivest-Shamir-Adleman) signing algorithm. |
| str | Identifies which digest to use when signing. This can be one of the following values: **HMAC:** Any supported hashing digest can be used. **RSA:** Must be one of `SHA1, SHA224, SHA256, SHA384, SHA512, MD5, MD5_SHA1, MD2, MD4, MDC2, or RIPEMD160.` |
| key | The key to use for signing. The `key_encoding` option identifies the format of the key (see options below). **HMAC:** The key can be of any length, but cannot be empty.  Control4 recommends that the size of the key be the same as the digest. For example, a 256-bit key for SHA256 or a 160-bit key for RIPEMD160. **RSA:** The key must be an RSA key that is valid for signing. Note that RSA public keys are typically not valid for signing. |
| data | The data to be signed. The `data_encoding` option identifies the format of the data (see options below).

Options:

`key_encoding`
 
Identifies the format of the key. Valid values for this option are:

- NONE: The key is not encoded.
- HEX: The key is hex encoded.
- Base64: The key is base64 encoded.
- PEM: The key a PEM encoded private key.
\- 

`data_encoding`

Identifies the format of the data. Valid values for this option are:

- NONE: The data is not encoded.
- HEX: The data is hex encoded.
- BASE64: The data is base64 encoded.
\- 

`return_encoding`

Identifies the format of the result (signature). Valid values for this option are:

- NONE: Do not encode the result.
- HEX (default): Hex (lowercase) encoding.
- `HEX_UPPER`: Hex (uppercase) encoding.
- BASE64: Base64 encoding.


### Returns

Success: Returns a string containing the signature.

Failure: Returns the following multiple results:

|Value | Description |
| --- | --- |
| nil | A value of nil indicates that an error occurred. |
|str |  A string containing a description of the error. |


### Examples

```lua
options = {}
options["key_encoding"] = "PEM"
options["return_encoding"] = "BASE64"
key = [[-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC8cDObD4DjL3TnUR7JxObq+pwb4XX6UYjXuM1zzl/4gvQ8KzA4
CDl8S5FQeaPe4vdrLHEJudxSJc7JWehMwcS+jP6xO1pRA68SBphq9I5G/itBw5zx
RSGi26NDTiu7XczTRTPGRyBRNxBiln4hWg3ordY5gn0PYe30Fem9vTyZ1QIDAQAB
AoGAPTNfv1uwq5iNKleRXUyjBuwv6Wo3a/4xKIbvy03ao5a8hhIszfX13aWZY36u
N0SVwOwlJliD8vYui/y0UsGYCRCKrBFh5iBlL4bd4bOg/3uD9EXqiZQiT/BeYAD5
TYozqtsBU8DhZytdX3OcmLlKwhX+fzKMC2/UWPkEQ2TlSX0CQQDd/DgdI6WbCn3f
sIJo6yEA98ZivayuoePfRP8CHaIAOVO6KOa1wYwR/nmrUmPSFZDUpvwB7mvel4WN
3VqNO9sXAkEA2VAKopLmgdL+KNZdpg2BB3eVMMDefhXC04tBmUpWX6qaFEVsw+gl
DYnDel3gv43iq3xqszaKEJy+1T+bR9tV8wJAc4ecvK2ctsATGqQGewxENPi/KwyE
Hq7qpXyHK1a4xV0QkkZPLDD68TJ7qApNIT1QDxyI84heY46AV4Doa7DHKQJBAMj0
l6EXL0nGj3m8IgW4XyVElBXthNIb1XpCQHs8nvsAjFNKj/Xp6rnGN5okzfzVfFMQ
TqtDOBF8oYwZscKVNbkCQFolrfE1I7DMTuQNHmF6kMXr/0gjhDTbUOOP3kzCSK14
iSpRAwom9R5BWUMFoRCn0j0TWFsTIBNSuOcMrw5n6NU=
-----END RSA PRIVATE KEY-----]]
signature=C4:Sign("RSA", "SHA256", key, "Walla Walla Washington", options)
print(signature)

﻿
options = {}
options["key_encoding"] = "BASE64"
options["return_encoding"] = "HEX"
key = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2cu"
signature = C4:Sign("HMAC", "SHA256", key, "Walla Walla Washington", options)
print(signature)

﻿
options = {}
options["key_encoding"] = "BASE64"
options["return_encoding"] = "HEX"
key = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2cu"
signature = C4:Sign("HMAC", "SHA256", key, "Walla Walla Washington", options)
print(signature)
```
