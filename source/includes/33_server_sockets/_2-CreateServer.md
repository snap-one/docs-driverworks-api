## CreateServer

Creates a Server Socket, that listens on port nPort, and sends messages to the driver upon receipt of the delimiter, strDelimiter (or upon timeout). This API should not be invoked during OnDriverInit.

###### Available from 2.10.0


### Signature

`C4:CreateServer(nPort, strDelimiter, bUseUDP) `

| Parameter | Description |
| --- | --- |
| num | TCP Socket to listen for connections on. See note below for additional port information. | 
| str | Optional: Delimiter to separate messages. If no delimiter is specified, packets are delivered as they are received. |
| bool | bUseUDP: When True, the server socket connection is a UDP server socket. The default is TCP. |


### Returns

`None`


### Usage Note

The Listening socket may accept multiple connections, which can be active at the same time. See note below for additional port information.


### Examples

Server Sockets Interface:

`C4:CreateServer(5080, "\r\n")`

Creates a Listening Socket Server on port 8080, with no delimiter (packets will be sent as received):

`C4:CreateServer(8080)`

To the right is an example that creates a UDP server socket connection:

```
C4:CreateServer(600, "", true)
function OnServerDataIn(nHandle, strData)
 print("OnServerDataIn" .. nHandle .. ": " .. strData)
end
```

Prior to operating system 2.9.0, it was not possible to specify a port in the C4:CreateServer API that was guaranteed to be safe. While the system could choose a port for you, the caller could not get that port to pass to clients for use. The end result was that driver writers would create drivers that would steal ports from Director or from each other. 

Beginning with 2.9.0, callbacks have been modified or added where needed to allow getting the ephemeral port from the C4:CreateServer API and to get the IP address of client connecting to the server created with C4:CreateServer. It is still possible to pass 0 for the port to have the OS select an available port for you. I the example to the right, `C4:CreateServer` specifying an Ephemeral Port:

```

function run()
    dbg("run called")
    C4:CreateServer(0, '\n', false)
end

OnServerStatusChannged Callback to Get the Correct Port:

function OnServerStatusChanged(nPort, strStatus)
    print("OnServerStatusChanged port: " .. nPort .. " status: " .. strStatus)
end
```


OnServerConnectionStatusChanged now Reports Client IP:

```
function OnServerConnectionStatusChanged(nHash, nPort, strStatus, strIP)
    print("OnServerConnectionStatusChanged hash: " .. nHash .. " port: " .. nPort .. " status: " .. strStatus .. " ip: " .. strIP)
end
```




Example of executing the Lua code in an example driver with output to a console:

```
Property Changed: Driver Status
run called
Driver enabled
OnServerStatusChanged port: 53319 status: ONLINE
OnServerConnectionStatusChanged hash: 162938911 port: 53319 status: ONLINE ip: 192.168.200.100
OnServerDataIn hash: 162938911 data: lkasjdfl ip: 192.168.200.100
```

