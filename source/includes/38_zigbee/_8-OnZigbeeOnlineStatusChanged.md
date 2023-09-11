## OnZigbeeOnlineStatusChanged

This function gets called when the Online status of a Zigbee node changes.

###### Available from 1.6.0.


### Signature

`OnZigbeeOnlineStatusChanged (strStatus, strVersion, strSkew)`


| Parameter | Description |
| --- | --- |
| str | Status: OFFLINE, ONLINE, REBOOT, UNKNOWN |
| str | Version |
| str | Skew |


### Example

```lua
function OnZigbeeOnlineStatusChanged (strStatus, strVersion, strSkew)
  print("Zigbee Status Changed: " .. strStatus)
  gZigbeeStatus = strStatus
end
```
