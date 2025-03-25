## ReceivedFromNetwork

Function which is called when data is received on a network binding. It is typically used to evaluate the data for specific delimiters and extracts the necessary components which are then used to do something.

###### Available from 1.6.0
###### Enhanced in 4.0.0 with from param


### Signature

`ReceivedFromNetwork(binding, port, data, from) `


| Parameter | Type | Description                                             |
| --------- | ---- | ------------------------------------------------------- |
| binding   | num  | The id of the binding for which the data was received.  |
| port      | num  | he port of the binding for which the data was received. |
| data      | str  | he data that was received.                              |
| from      | str  | The IP address from which the message originated.       |


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
