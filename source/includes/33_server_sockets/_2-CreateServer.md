## CreateServer

Creates a Server Socket that listens on port nPort and sends messages to the driver upon receipt of the delimiter, strDelimiter (or upon timeout). Note that this API API was modified in O.S. 3.3.1 to accommodate the addition of an identifier that is associated with an instance of a server. This identifier enables a Lua driver to determine which instance of a server is active. This API should not be invoked during OnDriverInit.

###### Available from 2.10.0


### Signature

```
C4:CreateServer(port,[delimiter], [useUDP], [identifier])`
```

| Parameter | Description |
| --- | --- |
|int| port: The port number to which the server is to be bound. If this value is zero (0), then an ephemeral port will be assigned automatically.|
|str| delimiter: The delimiter to use when reading the socket. This can be any combination of characters. When specified, the server will automatically deliver complete payloads to the driver up to, and including, the delimiter. When empty or not otherwise specified, the server will deliver packets to the driver as they arrive.|
|bool| useUDP: A boolean flag indicating whether the server should be established using the UDP protocol. When false, or not otherwise specified, the server is established using the TCP stream protocol.|
|str| identifier: A string that is associated with the instance of the server that is created. This identifier is passed as an argument to the various callbacks.|


### Returns

The CreateServer() function may return multiple values. 
On failure, the function returns the following:

- false
- A string describing the error that occurred.

On Success, the C4:CreateServer() functions returns the following:

- true

### Callbacks

There are three callbacks associated with servers created using the C4:CreateServer() function. These include:

- OnServerStatusChanged
- OnServerConnectionStatusChanged
- OnServerDataIn

### OnServerStatusChanged
The OnServerStatusChanged callback is invoked to notify a driver that the status of a server has changed. More specifically, that the server is now either online or offline.

### Signature

`OnServerStatusChanged(port, status, identifier)`

| Parameter | Description |
| --- | --- |
| int | port: The port on which the server is listening.|
|status| A string containing the status of the server. This is either "ONLINE" or "OFFLINE”.|
|identifier| The identifier that was specified when the server was created with either C4:CreateServer.|

### OnServerConnectionStatusChanged
The OnServerConnectionStatusChanged callback is invoked to notify a driver that either: a) a new connection has been accepted by the server; or b)  a previously accepted connection is now closed.

### Signature
`OnServerConnectionStatusChanged(handle, port, status, address, identifier)`

| Parameter | Description |
| --- | --- |
|int| handle: A handle to the connection. A driver can use this handle to address the connection in subsequent calls to C4:ServerSend() and C4:ServerCloseClient().|
|int| port: The port on which the server is listening.|
|str| string: A string containing the status of the connection. This is either "ONLINE" or "OFFLINE”.|
|str| address: The IP address of the remote endpoint that is connected to the server.|
|str| identifier: The identifier that was specified when the server was created with C4:CreateServer.|


### OnServerDataIn
The OnServerDataIn callback is invoked to notify a driver that data has received on a server connection.

### Signature
`OnServerDataIn(handle, data, address, port, identifier)`

| Parameter | Description |
| --- | --- |
|int| handle:  A handle to the connection. A driver can use this handle to address the connection in subsequent calls to C4:ServerSend() and C4:ServerCloseClient().|
|str| data: The data that was received from the connection.|
|str| address: The IP address of the remote endpoint that is connected to the server.|
|int| port: The port of the remote endpoint that is connected to the server.
|str| identifier: The identifier that was specified when the server was created with C4:CreateServer |


### Usage Note

The Listening socket may accept multiple connections, which can be active at the same time. See note below for additional port information.


### Examples

Server Sockets Interface:

`C4:CreateServer(5080, "\r\n")`

Creates a Listening Socket Server on port 8080, with no delimiter (packets will be sent as received):

`C4:CreateServer(8080)`

To the right is an example that creates a UDP server socket connection:

```lua
C4:CreateServer(600, "", true)
function OnServerDataIn(nHandle, strData)
 print("OnServerDataIn" .. nHandle .. ": " .. strData)
end
```

Prior to operating system 2.9.0, it was not possible to specify a port in the C4:CreateServer API that was guaranteed to be safe. While the system could choose a port for you, the caller could not get that port to pass to clients for use. The end result was that driver writers would create drivers that would steal ports from Director or from each other.

Beginning with 2.9.0, callbacks have been modified or added (OnServerStatusChanged) where needed to allow getting the ephemeral port from the C4:CreateServer API and to get the IP address of a client connecting to the server created with C4:CreateServer. It is still possible to pass 0 for the port to have the OS select an available port for you. In the first example to the right, `C4:CreateServer` is specifying an ephemeral Port:

```lua

function run()
    dbg("run called")
    C4:CreateServer(0, '\n', false)
end

OnServerStatusChannged Callback to Get the Correct Port:

function OnServerStatusChanged(nPort, strStatus)
    print("OnServerStatusChanged port: " .. nPort .. " status: " .. strStatus)
end
```


Next, [OnServerConnectionStatusChanged][1] now Reports Client IP:

```lua
function OnServerConnectionStatusChanged(nHash, nPort, strStatus, strIP)
    print("OnServerConnectionStatusChanged hash: " .. nHash .. " port: " .. nPort .. " status: " .. strStatus .. " ip: " .. strIP)
end
```


The last example to the right shows executing the Lua code in an example driver with output to a console:

```lua
Property Changed: Driver Status
run called
Driver enabled
OnServerStatusChanged port: 53319 status: ONLINE
OnServerConnectionStatusChanged hash: 162938911 port: 53319 status: ONLINE ip: 192.168.200.100
OnServerDataIn hash: 162938911 data: lkasjdfl ip: 192.168.200.100
```


[1]:	https://snap-one.github.io/docs-driverworks-api/#onserverconnectionstatuschanged