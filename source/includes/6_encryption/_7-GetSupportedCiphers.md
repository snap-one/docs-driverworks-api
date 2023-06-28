## GetSupportedCiphers

Returns the list of ciphers supported by the [Encrypt][1] and [Decrypt][2] functions.

###### Available in 1.6.0.


### Signature

`C4:GetSupportedCiphers ()`


### Returns

`ciphers`

| Value | Description |
| --- | --- |
| table | ciphers: Table of supported ciphers.  Each element is a key/value pair, where the key is the cipher name and the value is  the list of parameters for that cipher. |

Valid key/value pairs for *ciphers* element value:

| Value | Description |
| --- | --- |
| num | BlockSize: The size (in bytes) of each block for this cipher |
| num | KeyLength: The maximum size (in bytes) of the key for this cipher (shorter keys will be padded) |
| num | IVLength: The maximum size (in bytes) of the IV for this cipher (shorter IVs will be padded) |


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