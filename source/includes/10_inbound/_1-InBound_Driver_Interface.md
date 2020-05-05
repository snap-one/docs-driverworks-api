## InBound Driver Interface

The functions listed below represent Lua functions that are not Control4 APIs but are however included in this documentation. The functions below are implemented within a DriverWorks driver and can be called by an API, Director or another external process.  

For example, the Lua function UIRequest isn't a Control4 API. However, it is an InBound Driver Function that needs to be implemented in your driver if you intent to use the Control4 API:SendUIRequest. SendUIRequest sends a request to another driver. It uses the proxy or protocol ID value of the driver as a means to target the driver where the request will be sent. The driver receiving the SendUIRequest must have the InBound Driver Function UIRequest configured, which will contain the return values requested by the SendUIRequest call. 

Here is an example of using SendUIRequest in a driver: 

`C4:SendUIRequest(231, "GET_MY_DRIVER_DATA", tParams)`

In this example, the API contains a value of 231. This is the proxy ID value of the driver where the request is being sent. This is followed by a request called  `GET_MY_DRIVER_DATA`. This is an expected request by the driver receiving the SendUIRequest. A table of parameters follows the command.

Below is an example of the required UIRequest InBound Driver Function found in the driver receiving the SendUIRequest. In this example, when the request is received it takes the values in the tParams table and, if they are not a specified value of 640 or 480, multiplies them by 10. It then formats the values into XML and returns them through retValue to the driver that initiated the SendUIRequest.

```
function UIRequest(sRequest, tParams)
   ` tParams = tParams` 
    `local param_x = tonumber(tParams["PARAM_X"]) or 640`
   ` local param_y = tonumber(tParams["PARAM_Y"]) or 480`
               
        ` local value_x = param_x * 10`
        ` local value_y = param_y * 10`
               
        ` local retValue = "<driver_data>"`
         `retValue = retValue .. "<value_x>" .. value_x .. "</value_x>"`
        ` retValue = retValue .. "<value_y>" .. value_y .. "</value_y>"`
        ` retValue = retValue .. "</driver_data>"`
               
   ` return retValue`
`end`
```

The XML below is the returned value.

```
`<driver_data>`
    `<value_x>10240</value_x>`
    `<value_y>7680</value_y>`
`</driver_data>`
```

### List of InBound Driver Functions:
- OnBindingChanged
- OnDriverDestroyed
- OnDriverLateInit
- OnDriverInit
- OnPropertyChanged
- UIRequest
- ExecuteCommand
- ReceivedFromSerial
- ReceivedFromProxy
- ReceivedFromNetwork
- GetPrivateKeyPassword
- OnVariableChanged
- OnWatchedVariableChanged
- OnConnectionStatusChanged
- OnServerConnectionStatusChanged
- OnServerDataIn
- OnNetworkBindingChanged
- OnTimerExpired
- OnZigbeeOnlineStatusChanged
- OnReflashLockGranted
- OnReflashLockRevoked
- OnSystemEvent
- ListMIBReceived
- ListNewControl
- ListNewList
- ListEvent