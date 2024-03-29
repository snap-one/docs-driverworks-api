## ReceivedFromSerial

Function which is called when serial data is received on a serial binding. It is typically used to evaluate the data for specific delimiters and extracts the necessary components which are then used to do something.

###### Available from 1.6.0


### Signature

`ReceivedFromSerial(idBinding, strData)`


| Parameter | Description |
| --- | --- |
| num | ID of the serial interface the data was received on | 
| str | Data received from the serial interface |


### Returns

`None`


### Usage Note

Serial data received may contain NULL characters. NULL (‘\0’) is a valid character and Lua strings handle embedded NULL characters. Serial data received may only include part of a protocol command from the connected device. It is the driver’s responsibility to re-constitute and parse the commands received from the device.


### Example

```lua
function ReceivedFromSerial(idBinding, strData)
   print("Received something from serial on binding " .. idBinding)
   hexdump(strData)
   responseCount=0
   l_string = strData
   for w in string.gmatch(strData, "!1(...)") do
      retType = w
      responseCount=responseCount +1
      delimPos = string.find(l_string,tohex("1A"))
      retValue = string.sub(l_string,6, tonumber(delimPos)-1)
      l_string = string.sub(l_string,delimPos+1)
      sendNotify()
   end
end
```
