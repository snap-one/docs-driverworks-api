## ReceivedFromNetwork

Function which is called when data is received on a network binding. It is typically used to evaluate the data for specific delimiters and extracts the necessary components which are then used to do something.

###### Available from 1.6.0


### Signature

`ReceivedFromNetwork(idBinding, nPort, strData) `


| Parameter | Description |
| --- | --- |
| num | Binding ID of the interface the data was received from |
| num | Network Port the data was received on |
| str | Network data from the specified binding and port |


### Returns

`None`


### Usage Note

Network data received may contain NULL characters. NULL (‘\0’) is a valid character and Lua strings handle embedded NULL characters.Network data received may only include part of a protocol command from the connected device. It is the driver’s responsibility to re-constitute and parse the commands received from the device.


### Example

```lua
function ReceivedFromNetwork(idBinding, nPort, strData)
  -- Save up things coming back on HTTP port, process when done 	
	sending to us...
  g_Receivebuffer = g_Receivebuffer .. strData
end
```
