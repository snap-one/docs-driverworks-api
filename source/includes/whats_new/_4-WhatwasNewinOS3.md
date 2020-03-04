## What was New in O.S.3

**New Interfaces that  were Added**

The Notification Interface allows device drivers to include .jpeg files within notifications. These images are displayed as part of the notification. The .jpeg file can be retrieved from a cloud service that supports the device, from the device itself or from a location on a Control4 Controller.

The Scheduler Agent Interface has been added which supports a driver's ability to create scheduled events that can be used in Programming in ComposerPro.


**New APIs that were Added**

The GetBindingsByDevice API returns all of the Binding information for a device.
The GetNetworkBindingsByDevice API return all of the Network Binding information for a device.
The GetNetworkConnections API returns connection information based on connection type.
The GetProjectProperty API uses a single string parameter from a list of property names and returns the value of that property, if it exists. 


**Interfaces that were Modified**

The Media Management Interface has been enhanced with content supporting Device Level Context and Broadcast Video APIs

The Timer Interface has been updated to identify legacy APIs that, while still valid, are not recommenced for new driver development. Additionally, a sample driver using the (recommended) SetTimer API has been included with the SDK.

The WebService Interface has been updated with a new sample driver that demonstrates how to perform basic C4:url calls.


**Interfaces that were Modified**

The AddVariable API has been enhanced with additional Parameter Types.

The JsonDecode API has been enhanced with a new optional parameter: decodeNull which indicates how null values are decoded. Additionally, c4json.null has been added. This can can be used to insert a null value into a JSON document or to test for a null value that was encountered in a JSON document.

The OnBindingChanged API has been updated to include missing parameters.

The PersistGetValue API has been updated with an option third parameter: encrypted.

The PersistSetValue API has been updated with an option third parameter: encrypted.

The RenameDevice API has updated content regarding passing a ProxyID or DeviceId value.

The UpdatePropertyList API has been modified with a parameter re-name and an additional, optional parameter.


**APIs that were Deprecated**

The Debug Interface content has been removed from the DriverWords SDK. The APIs that were defined in the Debug Interface were used in conjunction with an executable that supported remote debugging. Support for the debugging utility was discontinued several years ago. As a result, the following APIs have been removed:

- Attach
- DisableremoteDebugging
- EnableRemoteDebugging
- OnEndDebugSession