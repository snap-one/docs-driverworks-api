## TEADecrypt

Decrypt the input string with Corrected Block TEA (XXTEA) Algorithm, using the specified key. This API can be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:TEADecrypt(strBuf, strKey)`


| Parameter | Description |
| --- | --- |
| str | String to be decrypted |
| key  | Key to use for decryption. Keys are 32 hex digits, encoded as a string (128-bit). |


### Returns

| Parameter | Description |
| --- | --- |
| str | Decrypted version of input string. |


### Usage Note

Key must be the same for encryption / decryption to function properly. The input string (strBuf) must be padded to a 4-byte boundary. More information about the Corrected Block TEA algorithm (XXTEA) as well as a compatible C implementation of XXTEA may be found at Wikipedia: http://en.wikipedia.org/wiki/XXTEA


### Example

Encrypt then Decrypt a string, then print the original string out:

```
local key = "1234567887654321abcdefabcabcdefa"
e = C4:TEAEncrypt("Control4 Rocks! ", key)
print(C4:TEADecrypt(e, key))

  	-- prints "Control4 Rocks! 
```
