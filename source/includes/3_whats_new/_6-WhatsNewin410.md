
## What’s New in 4.1.0


### Additions to the Helper Interface

The [GetCommands ][1]function has been added to return a table of information containing elements of commands that will be created dynamically in ComposerPro.

The [GetRoomID][2] function has been added to provide a Room ID value to assist with AV Pathing.

The [GetNonBindingConsumerDevices][3] function has been added to return the devices that consume the data delivered through a non-binding connection.


### Additions to the Zigbee Interface

A new, optional parameter has been added to the following APIs:

- [OnZigbeePacketIn][4]
- [OnZigbeePacketFailed][5]
- [OnZigbeePacketSuccess][6]

This parameter is the numerical value of the EUID.

[1]:	https://snap-one.github.io/docs-driverworks-api/#helper-interface-getcommands
[2]:	https://snap-one.github.io/docs-driverworks-api/#helper-interface-getroomid
[3]:	https://snap-one.github.io/docs-driverworks-api/#helper-interface-getnonbindingconsumerdevices
[4]:	https://snap-one.github.io/docs-driverworks-api/#zigbee-interface-onzigbeepacketin
[5]:	https://snap-one.github.io/docs-driverworks-api/#zigbee-interface-onzigbeepacketfailed
[6]:	https://snap-one.github.io/docs-driverworks-api/#zigbee-interface-onzigbeepacketsuccess