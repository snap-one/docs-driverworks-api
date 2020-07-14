## SendToSerial

Simple function which sends the command out serial port on binding 1 and adds the \r terminator to the end of the command being sent. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:SendToSerial(idBinding, strData)`


| Parameter | Description |
| --- | --- |
| num | Binding ID of the network interface to send on |
| str | Data to send out the specified network interface |


### Returns

`None`


### Usage Note:

Serial data to be sent can contain NULL characters. NULL (‘\0’) is a valid character and Lua strings handle embedded NULL characters


### Example

```lua
function emit(strCommand)
   print("Emit: " .. strCommand)
   C4:SendToSerial("1", strCommand .. "\r")
end
```
