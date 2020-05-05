## GetSupportedDigests

```lua
local supportedDigests = C4:GetSupportedDigests ()
for k,v in pairs (supportedDigests ['SHA256']) do
	print (k, v)
end
```

> Output:

```lua
Size	32
```

Returns the list of digests supported by the [Hash][1], [HMAC][2] and [PBKDF2][3] functions.

###### Available in 1.6.0.


### Signature

`C4:GetSupportedDigests ()`


### Returns

| Value | Description |
| --- | --- |
| table | digests: Table of supported digests.  Each element is a key/value pair, where the key is the digest name and the value is the list of parameters for that digest. |

Valid key/value pairs for digest element value:

| Value | Description |
| --- | --- |
| num | Size: The size (in bytes) of the output of this digest |

[1]:	#hash
[2]:	#hmac
[3]:	#pbkdf2