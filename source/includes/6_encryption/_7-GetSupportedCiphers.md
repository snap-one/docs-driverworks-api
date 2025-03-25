## GetSupportedCiphers

Returns the list of ciphers supported by the [Encrypt][1] and [Decrypt][2] functions.

In conjunction with the release of O.S. 4.0.0, low level AES, Blowfish, Camellia, CAST, DES, IDEA, RC2, RC4, RC5 and SEED cipher functions have been deprecated and are no long supported with the C4:Encrypt function. As support for various cipher function can change in the future, it is recommended to review the release notes for OpenSSL 3.0: [https://openssl-library.org/news/openssl-3.0-notes/index.html][3]


###### Available in 1.6.0.


### Signature

`C4:GetSupportedCiphers ()`


### Returns

`ciphers`

| Value | Description                                                                                                                                                        |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| table | ciphers: Table of supported ciphers.  Each element is a key/value pair, where the key is the cipher name and the value is  the list of parameters for that cipher. |

Valid key/value pairs for *ciphers* element value:

| Value | Description                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------- |
| num   | BlockSize: The size (in bytes) of each block for this cipher                                    |
| num   | KeyLength: The maximum size (in bytes) of the key for this cipher (shorter keys will be padded) |
| num   | IVLength: The maximum size (in bytes) of the IV for this cipher (shorter IVs will be padded)    |


### Example

```lua
local supportedCiphers = C4:GetSupportedCiphers ()
for k,v in pairs (supportedCiphers ['AES-256-CBC']) do
	print (k, v)
end

> Output:

BlockSize	16
KeyLength	32
IVLength	16
```



[1]:	https://snap-one.github.io/docs-driverworks-api/#encryption-interface-encrypt
[2]:	https://snap-one.github.io/docs-driverworks-api/#encryption-interface-decrypt
[3]:	https://openssl-library.org/news/openssl-3.0-notes/index.html