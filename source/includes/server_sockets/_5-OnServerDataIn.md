## OnServerDataIn

This function gets called when data is coming in on an open Server Socket.

###### Available from 2.10.0


### Signature

`OnServerDataIn(nHandle, strData, strclientAddress, strPort`


| Parameter | Description |
| --- | --- |
| num | Server Socket handle received in OnServerConnectionStatusChanged. Used to reply or disconnect this Server Socket. |
| str | Data received |
| str | IP of the remote client. For TCP servers this is the remote IP address of the connected client. |
| | For UDP servers this is the IP address of the sender. |
| num | Port of the remote client. For TCP servers this is the remote port number of the connected client. |
| | For UDP servers this is the port number of the sender. |


### Returns

`None`


### Example

This example prints the incoming data from an open Server Socket (assumes the data is ASCII printable)

```
function OnServerDataIn(nHandle, strData, strclientAddress, strPort)
  print("Received Data on Handle: " .. nHandle .. ": " .. strData .. ":"  strclientAddress  ": "  strPort))
end
```