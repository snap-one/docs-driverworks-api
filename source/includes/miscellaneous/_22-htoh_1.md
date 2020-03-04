## htoh  2

Converts the numeric value passed in to network byte order. This API can be invoked during OnDriverInit.

###### Available from 1.6.0

### Signature

`C4:htoh_1()`


| Parameter | Description |
| --- | --- |
| int | Number to be converted |


### Returns

| Value | Description |
| --- | --- |
| str | 8 byte string representing the converted network byte order |

### Usage Note

This function is typically used to convert numeric values to be passed over a network, when the byte order of the two ends is unknown or may be different from each other. This way, ‘little-endian’ and ‘big-endian’ machines can communicate without confusion. ‘Host’ byte order is the byte order of values on the local machine, and ‘Network’ byte order is the standard byte order on Ethernet networks.

### Example

```
nbo = C4:ntoh_l(0x34120000)
print("network val is " .. nbo)
Output: network val is 00001234
```
