## ntoh  1

Function called from DriverWorks driver to get a capability from the driver’s .c4z file. This API should not be invoked during OnDriverInit.


###### Available from 1.6.0
 

### Signature

`C4:ntoh_1()`


| Parameter | Description |
| --- | --- |
| str | The name of the capability to retrieve |



### Returns

| Value | Description |
| --- | --- |
| str | The value of the capability retrieved from the driver file |


### Example

If this device supports discrete volume control, send discrete volume, otherwise, send a Volume Up or Volume Down command:

```lua
if (C4:GetCapability("has_discrete_volume_control") == "False") then
  if (VolumeValue > CurVolumeValue) then
    SendVolumeUp()
  else
    SendVolumeDown()
  end
else
  SendVolumeDiscrete(VolumeValue)
End
OnBindingChanged
```
