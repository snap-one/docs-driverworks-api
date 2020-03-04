## SetBindingStatus

Function that enables a Lua driver to explicitly set the "connected" state for a connection binding. This can particularly useful for connection bindings that aren't persistent (i.e., always connected), such as HTTP. Such non-persistent connections are marked as Offline (yellow) in the Network Tools windows in Composer. The C4:SetBindingStatus function enables a driver to manage the "connected" state of a connection binding, effectively overriding the default behavior provided by Director

###### Available from 2.10.0


### Signature

`C4:SetBindingStatus(idBinding, strStatus)`


| Parameter | Description |
| --- | --- |
| num | Binding ID of the existing network binding |
| str | String that specifies the status to set. |

### Usage Note

The string parameter can be one of the following values: unknown: This is the default if there have been no prior calls to `C4:SetBindingStatus` or if the value of the status parameter is anything other than "online" or "offline".


### Returns

`None`


### Example

`C4:SetBindingStatus(6001, "online") `
