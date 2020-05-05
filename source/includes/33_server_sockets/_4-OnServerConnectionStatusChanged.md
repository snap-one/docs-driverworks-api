## OnServerConnectionStatusChanged

This function gets called when Server Socket connection status has changed.

###### Available from 2.10.0


### Signature

`OnServerConnectionStatusChanged(nHandle, nPort, strStatus) `


| Parameter | Description |
| --- | --- |
| num | Server Socket handle. May be used to respond to this instance of a connection on the port, or to close this connection. |
| num | Port for Socket Connection |
| str | Status of the connection. Valid values include: ONLINE, OFFLINE |


### Returns

`None`


### Example

This function prints the current status as it changes to the Lua Output window.

```
function OnServerConnectionStatusChanged(nHandle, nPort, strStatus)
  if (strStatus == "ONLINE") then
    print("Server Connection Established: " .. nHandle)
  else
    print("Server Connection Disconnected: " .. nHandle)
  end
end
```