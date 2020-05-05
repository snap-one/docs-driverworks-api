## GetSerialSettings

Returns the \<serialsettings\> string from the driver that is connected to the provided control binding. The control binding should be an RS232 provider binding. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:GetSerialSettings (idBinding)`


| Parameter | Description |
| --- | --- |
| num | Control Binding Value |


### Returns

| Value | Description |
| --- | --- |
| str | Serial Settings Data in string format. |