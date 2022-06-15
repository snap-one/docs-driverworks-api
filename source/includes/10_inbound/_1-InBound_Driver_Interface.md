## InBound Driver Interface

The functions listed below represent Lua functions that are not Control4 APIs but are however included in this documentation. The functions below are implemented within a DriverWorks driver and can be called by an API, Director or another external process.

For example, the Lua function UIRequest isn't a Control4 API. However, it is an InBound Driver Function that needs to be implemented in your driver if you intent to use the Control4 API:[SendUIRequest][1]. SendUIRequest sends a request to another driver. It uses the proxy or protocol ID value of the driver as a means to target the driver where the request will be sent. The driver receiving the SendUIRequest must have the InBound Driver Function UIRequest configured, which will contain the return values requested by the SendUIRequest call.

Here is an example of using SendUIRequest in a driver:

`C4:SendUIRequest(231, "GET_MY_DRIVER_DATA", tParams)`

In this example, the API contains a value of 231. This is the proxy ID value of the driver where the request is being sent. This is followed by a request called  `GET_MY_DRIVER_DATA`. This is an expected request by the driver receiving the SendUIRequest. A table of parameters follows the command.

To the right is an example of the required UIRequest InBound Driver Function found in the driver receiving the SendUIRequest. In this example, when the request is received it takes the values in the tParams table and, if they are not a specified value of 640 or 480, multiplies them by 10. It then formats the values into XML and returns them through retValue to the driver that initiated the SendUIRequest.

```lua
function UIRequest(sRequest, tParams)
    tParams = tParams
    local param_x = tonumber(tParams["PARAM_X"]) or 640
    local param_y = tonumber(tParams["PARAM_Y"]) or 480
               
         local value_x = param_x * 10
         local value_y = param_y * 10
               
         local retValue = "<driver_data>"
         retValue = retValue .. "<value_x>" .. value_x .. "</value_x>"
         retValue = retValue .. "<value_y>" .. value_y .. "</value_y>"
         retValue = retValue .. "</driver_data>"
               
    return retValue
end

--The XML below is the returned value.
<driver_data>`
    <value_x>10240</value_x>
    <value_y>7680</value_y>
</driver_data>
```

### List of InBound Driver Functions:
- [OnBindingChanged][2]
- [OnDriverDestroyed][3]
- [OnDriverLateInit][4]
- [OnDriverInit][5]
- [OnPropertyChanged][6]
- [SendUIRequest][7]
- [ExecuteCommand][8]
- [ReceivedFromSerial][9]
- [ReceivedFromProxy][10]
- [ReceivedFromNetwork][11]
- [GetPrivateKeyPassword][12]
- [OnVariableChanged][13]
- [OnWatchedVariableChanged][14]
- [OnConnectionStatusChanged][15]
- [OnServerConnectionStatusChanged][16]
- [OnServerDataIn][17]
- [OnNetworkBindingChanged][18]
- [OnZigbeeOnlineStatusChanged][19]
- [OnReflashLockGranted][20]
- [OnReflashLockRevoked][21]

[1]:	https://snap-one.github.io/docs-driverworks-api/#senduirequest
[2]:	https://snap-one.github.io/docs-driverworks-api/#onbindingchanged
[3]:	https://snap-one.github.io/docs-driverworks-api/#ondriverdestroyed
[4]:	https://snap-one.github.io/docs-driverworks-api/#ondriverlateinit
[5]:	https://snap-one.github.io/docs-driverworks-api/#ondriverinit
[6]:	https://snap-one.github.io/docs-driverworks-api/#onpropertychanged
[7]:	https://snap-one.github.io/docs-driverworks-api/#senduirequest
[8]:	https://snap-one.github.io/docs-driverworks-api/#executecommand
[9]:	https://snap-one.github.io/docs-driverworks-api/#receivedfromserial
[10]:	https://snap-one.github.io/docs-driverworks-api/#receivedfromproxy
[11]:	https://snap-one.github.io/docs-driverworks-api/#receivedfromnetwork
[12]:	https://snap-one.github.io/docs-driverworks-api/#getprivatekeypassword
[13]:	https://snap-one.github.io/docs-driverworks-api/#onvariablechanged
[14]:	https://snap-one.github.io/docs-driverworks-api/#onwatchedvariablechanged
[15]:	https://snap-one.github.io/docs-driverworks-api/#onconnectionstatuschanged
[16]:	https://snap-one.github.io/docs-driverworks-api/#onserverconnectionstatuschanged
[17]:	https://snap-one.github.io/docs-driverworks-api/#onserverdatain
[18]:	https://snap-one.github.io/docs-driverworks-api/#onnetworkbindingchanged
[19]:	https://snap-one.github.io/docs-driverworks-api/#onzigbeeonlinestatuschanged
[20]:	https://snap-one.github.io/docs-driverworks-api/#onreflashlockgranted
[21]:	https://snap-one.github.io/docs-driverworks-api/#onreflashlockrevoked