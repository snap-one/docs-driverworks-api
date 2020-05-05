## ReceivedFromNetwork

Function which combines the data received from the network into a variable for processing when the connection status changes. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:ReceivedFromNetwork(idBinding, nPort, strData) `


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

```
function ReceivedFromNetwork(idBinding, nPort, strData)
  -- Save up things coming back on HTTP port, process when done 	
	sending to us...
  g_Receivebuffer = g_Receivebuffer .. strData
end
```