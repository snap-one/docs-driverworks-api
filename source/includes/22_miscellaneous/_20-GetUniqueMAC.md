## GetUniqueMAC

Function to get the unique MAC address of the Director box. This API can be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:GetUniqueMAC()`


Parameter

`None`


### Returns

`None`


### Usage Note

The unique MAC may not be the active MAC if multiple NICs are present. For example, for systems using a wireless interface the MAC returned will be the MAC of the wired Ethernet card. When using Virtual Director, the MAC returned will be the PC's MAC address.


### Example

`print("Unique mac is " .. C4:GetUniqueMAC())`
Output: `Unique mac is 000FFF102F73`
