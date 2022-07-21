# C4SSH Interface

## CreateSSHClient
The C4SSH API enables Lua drivers to establish an SSH client connection to a remote device and execute a series of commands. A driver creates an instance of a C4SSH object by calling the C4:CreateSSHClient function.

_This interface was released in conjunction with O.S. 3.3.0_


### Signature

`C4:CreateSShClient ()`


### Parameters

None


### Returns

An instance of a C4SSH object that can be used to establish an SSH client connection to a remote device. The C4SSH object enables a Lua driver to establish an SSH client connection to a device, and then to interact with that device by executing a series of commands. The C4SSH object API provides the following methods: 

- Connect
- Send
- Disconnect
- SetConnectTimeout
- SetOnConnected
- SetOnData
- SetOnDisconnected

These methods are defined below:


## Connect

The Connect method attempts to establish a connection to a remote device. There are three methods that set callback functions which enable a driver to receive various notifications about the connection. These are:

SetOnConnected: Provides notification when a connection is established.
SetOnData: Provides notification when data is read from the connection.
SetOnDisconnected: Provides notification when the connection is disconnected, or has otherwise failed.

Additionally, a driver may control how long the C4SSH object waits before determining that the connection has failed. This is accomplished with: SetConnectTimeout which specifies the amount of time to wait when attempting to connect to an endpoint.


### Signature

`Connect(endpoint, username, password, string)`


| Parameters | Description |
| --- | --- |
| Endpoint | string. The endpoint to which the SSH connection is to be established. This can be either a host name or an IP address. If the caller specifies a host name, the C4SSH object will attempt to resolve the IP address of the endpoint before connecting.|
| Username | string. The username with which to log in to the remote device. |
Password | string. The password to use when logging in to the remote device. This value can be empty if no password is required.|
| Port | Integer. The port to use when establishing a connection to the remote device. If omitted, then the default port of 22 is used.|


### Returns

The Connect method may return multiple values. On success, Connect returns the following:

- The instance of the C4SSH object on which Connect was invoked.

On failure, Connect returns the following:

- nil
- A string describing the failure


#### See Also:

- SetOnConnected
- SetOnData
- SetOnDisconnected
- SetConnectTimeout
- OnConnected
- OnData
- OnDisconnected



## Send

Sends a command to a remote device. A driver may set a callback function to receive notification when data has been read from the connection by calling the SetOnData method.

### Signature

`Send(command)`

| Parameters | Description |
| --- | --- |
|Command| string. The command to be sent to the remote device.|


### Returns

The Send method may return multiple values. On success, Send returns the following:

- The instance of the C4SSH object on which the Send method was invoked.

On Failure, Send returns the following:

- nil
- A string describing the failure

### Usage Note

Due to the asynchronous nature of the C4SSH API, a driver must wait for a connection to be established before calling Send. A driver can be notified that a connection has been established successfully by calling SetOnConnected to register an OnConnected callback function.


#### See Also:

- SetOnData
- OnData



## Disconnect

Closes the connection. A driver may set a callback function to receive notification when the connection has been disconnected by calling the SetOnDisconnected method.

### Signature

`Disconnect()`

### Parameters

None


### Returns

The Disconnect method returns a single value which is the instance of the C4SSH object on which the Disconnect method was invoked.


#### Set Also

- SetOnDisconnected
- OnDisconnected



## SetConnectTimeout

Sets the amount of time the C4SSH object waits before determining that an attempt to establish a connection to an endpoint has failed. The C4SSH object notifies a driver that a connection has timed out by invoking the OnDisconnected callback function. A driver may set the OnDisconnected callback function by calling SetOnDisconnected.


### Signature

`SetConnectTimeout(Timeout)`


| Parameters | Description |
| --- | --- |
|Timeout| integer.The number of seconds to wait before determining that an attempt to establish a connection has failed. The default is 30 seconds. |


### Returns

The SetConnectTimeout method may return multiple values. On Success, SetConnectTimeout returns the following:

- The instance of the C4SSH object on which SetConnectTimeout was invoked.

On failure, SetConnectTimeout returns the following:

- nil
- A string describing the failure.


#### See Also

- Connect
- SetOnDisconnected
- OnDisconnected



## SetOnConnected

Sets the callback function that is invoked when a client connection has been established. See OnConnected for specific details about the function signature of this callback.

### Signature

`SetOnConnected(Callback)`


| Parameters | Description |
| --- | --- |
|Callback| function. A callback function to be invoked when a connection has been established.|


### Returns

The SetOnConnected method returns a single value which is the instance of the C4SSH object on which SetOnConnected was invoked.


#### See Also

- OnConnected



## SetOnData

Sets the callback function that is invoked when data has been read from a connection. See OnData for specific details about the function signature of this callback.

### Signature

`SetOnData(Callback)`


| Parameters | Description |
| --- | --- |
|Callback| function.A callback function to be invoked when data has been read from a connection.|


### Returns
The SetOnData method returns a single value which is the instance of the C4SSH object on which the SetOnData method was invoked.


#### See Also

- OnData



## SetOnDisconnected

Sets the callback function that is invoked when a connection is disconnected or has otherwise failed. Note that the C4SSH object invokes the OnDisconnected callback to notify a driver when an error has forced the closure of a connection. See OnDisconnected for specific details about the function signature of this callback.


### Signature
`SetOnDisconnected(Callback)`


| Parameters | Description |
| --- | --- |
|Callback| function. A callback function to be invoked when a connection is disconnected or has otherwise failed.|


### Returns

The SetOnDisconnected method returns a single value which is the instance of the C4SSH object on which SetOnDisconnected was invoked.


#### See Also

- OnDisconnected




**C4SSH Callbacks**

The C4SSH object provides the following callback functions that enable a driver to receive various notifications about the connection. These include the following:

- OnConnected
- OnData
- OnDisconnected


## OnConnected

The OnConnected callback is invoked to notify a driver that a connection has been established.

### Signature

`OnConnected(client)`


### Parameters

| Parameters | Description |
| --- | --- |
|client| `[C4SSH]`: The instance of the C4SSH object that connected successfully.|

#### See Also

- SetOnConnected


### Example

```js
function OnData(client, data)
    print(client, "OnData")
    print(data)
    client:Disconnect()
end
 
function OnConnected(client)
    print(client, "OnConnected")
    client:Send("ls")
end
 
function OnDisconnected(client, error)
    print(client, "OnDisconnected", error)
end
 
sshclient = C4:CreateSSHClient()
 
sshclient:SetOnDisconnected(OnDisconnected)
sshclient:SetOnConnected(OnConnected)
sshclient:SetOnData(OnData)
 
sshclient:Connect("192.168.1.42", "username", "password")
```



## OnData

The OnData callback is invoked to notify a driver when data has been read from a connection.

### Signature

`OnData(client, data)`


| Parameters | Description |
| --- | --- |
|client| `[C4SSH]`: The instance of the C4SSH object that received the data.|
|Data| string. A string containing the data that was read from the connection.|


#### See Also

- SetOnData


### Example

```js
function OnData(client, data)
    print(client, "OnData")
    print(data)
    client:Disconnect()
end
 
function OnConnected(client)
    print(client, "OnConnected")
    client:Send("ls")
end
 
function OnDisconnected(client, error)
    print(client, "OnDisconnected", error)
end
 
sshclient = C4:CreateSSHClient()
 
sshclient:SetOnDisconnected(OnDisconnected)
sshclient:SetOnConnected(OnConnected)
sshclient:SetOnData(OnData)
 
sshclient:Connect("192.168.1.42", "username", "password")
```



## OnDisconnected
The OnDisconnected callback is invoked to notify a driver that a connection has been disconnected. If an error forced the closure of the connection, then the Error argument provides a string describing the error.


### Signature

`OnDisconnected(client, Error)`


| Parameters | Description |
| --- | --- |
|client| `[C4SSH]`: The instance of the C4SSH object that was disconnected.|
|Error| string. A string describing the failure if an error forced the closure of the connection. If no error occurred, then the value of the Error argument is nil. |


#### See Also

- SetOnDisconnected



### Example

```js
function OnData(client, data)
    print(client, "OnData")
    print(data)
    client:Disconnect()
end
 
function OnConnected(client)
    print(client, "OnConnected")
    client:Send("ls")
end
 
function OnDisconnected(client, error)
    print(client, "OnDisconnected", error)
end
 
sshclient = C4:CreateSSHClient()
 
sshclient:SetOnDisconnected(OnDisconnected)
sshclient:SetOnConnected(OnConnected)
sshclient:SetOnData(OnData)
 
sshclient:Connect("192.168.1.42", "username", "password")
```
