## MediaSetDeviceContext

Function that sets a device id to be used for media related call.  If set to any value other than “0” then adding, modifying, retrieving or removing functionality will use the supplied device id. Note that this API must be called in the OnDriverLateInit area of the device driver.

###### Available from 1.6.0


### Signature

`C4:MediaSetDeviceContext()`

| Parameters | Description |
| --- | --- |
| num | New device id to be associated with media related api’s. |


### Usage Note

 If the number parameter is set to “0” then the media related APIs will use the current driver’s device id. 