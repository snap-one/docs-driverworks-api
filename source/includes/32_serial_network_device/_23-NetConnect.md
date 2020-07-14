## NetConnect

Function used to tell the system to make a connection (static or dynamic). Connections are created using the [CreateNetworkConnection][1] API. Further, port-specific configuration can be configured for a connection through the [NetPortOptions][2] API. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:NetConnect(idBinding, nPort, strIPType,)`


| Parameter | Description |
| --- | --- |
| num | Binding ID of the network interface |
| num | Network port to connect to. If NetPortOptions API is used with NetConnect, the remaining parameters are ignored. |
| str | IP Type. Optional. TCP is assumed or UDP or MULTICAST |


### Returns

`None`


### Examples

` C4:NetConnect(6001, 80, UDP)`

[1]:	https://control4.github.io/docs-driverworks-api/#createnetworkconnection
[2]:	https://control4.github.io/docs-driverworks-api/#netportoptions