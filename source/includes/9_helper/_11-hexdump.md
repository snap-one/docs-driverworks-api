## hexdump

Prints out the values of a string in both hex and ascii representation.  All characters that are not ‘A-Z’ or ‘0-9’ are printed as a ‘.’ in the ascii representation. The print goes to the Lua tab on the properties page of the driver. This API can be invoked during OnDriverInit.

###### Available from 1.6.0



### Signature

`hexdump(strDump)`


| Parameter | Description |
| --- | --- |
| strDump | Text to print out in a hexdump. |



### Returns

`None`



### Example

```
hexdump(tohex("00 ff de ad be ef ") .. "Test Text")

Prints out the following:
00000000  00 FF DE AD BE EF 54 65  ......Te
00000008  73 74 20 54 65 78 74     st.Text
```