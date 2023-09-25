## NetConnect

Function used to tell the system to make a connection (static or dynamic). Connections are created using the [CreateNetworkConnection][1] API. Further, port-specific configuration can be configured for a connection through the [NetPortOptions][2] API. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:NetConnect(idBinding, nPort, strIPType, bool)`


| Parameter | Description                                                                                                                                                                                                                                                                                                                                             |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| num       | Binding ID of the network interface                                                                                                                                                                                                                                                                                                                     |
| num       | Network port to connect to. If NetPortOptions API is used with NetConnect, the remaining parameters are ignored.                                                                                                                                                                                                                                        |
| str       | IP Type. Optional. TCP is assumed or UDP or MULTICAST                                                                                                                                                                                                                                                                                                   |
| bool      | True/False.  Optional. Specifies whether Director should suppress OnDeviceOnline and OnDeviceOffline events for the connection. By default, Director does suppress events for all connections created this way. The events can be enabled by passing “false” for this parameter. For more information, please refer to: [Suppressing System Events][3]. |


### Returns

`None`


### Examples

` C4:NetConnect(6001, 80, UDP)`

[1]:	https://snap-one.github.io/docs-driverworks-api/#serial-and-network-interface-createnetworkconnection
[2]:	https://snap-one.github.io/docs-driverworks-api/#serial-and-network-interface-netportoptions
[3]:	https://snap-one.github.io/docs-driverworks-api/#event-interface-suppressing-system-events