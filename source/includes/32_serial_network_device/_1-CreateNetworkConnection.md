## CreateNetworkConnection

Function that defines a dynamic Network Connection so no Connection XML is required. Further (port-specific configuration) can be accomplished through the use of the [NetPortOptions][1] API. Connections are actually made using the [NetConnect][2] API. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:CreateNetworkConnection (idBinding, strAddress, strConnectionType)`

| Parameter | Description |
| --- | --- |
| num | id of the Network Binding to create. |
| str | Network address or hostname that this network connection will use. |
| str | Optional string designating connection type |


### Returns

`None`


### Usage Notes

This is an alternative to having the connection section in the XML that creates the network connection

This binding parameter is used for other network calls: OnNetworkStatusChanged, [C4:NetConnect][3] & [C4:NetDisconnect][4]. Note that all Binding ID values must be unique. Duplication of Binding IDs is not permitted within the same system. Binding Ranges include:

- Control Bindings	= 1 -\> 999
- Video Inputs		= 1000 -\> 1099
- Video Outputs		= 2000 -\> 2999
- Audio Inputs		= 3000 -\> 3099
- Audio Outputs		= 4000 -\> 4999
- Proxy Bindings	= 5000 -\> 5999
- Network Bindings	= 6000 -\> 6999
- Room Bindings	= 7000 -\> 7999
- Power Manager	= 8000 -\> 8999


### Example

`C4:CreateNetworkConnection (6000, "196.120.10.10", "SSL")`

[1]:	https://control4.github.io/docs-driverworks-api/#netportoptions
[2]:	https://control4.github.io/docs-driverworks-api/#netconnect
[3]:	https://control4.github.io/docs-driverworks-api/#netconnect
[4]:	https://control4.github.io/docs-driverworks-api/#netdisconnect