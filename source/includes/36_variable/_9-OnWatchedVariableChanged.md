## OnWatchedVariableChanged

Function called by Director when a Control4 variable changes value.

###### Available from 1.6.0.


### Signature

`C4:OnWatchedVariableChanged(idDevice, idVariable, strValue)`	

| Parameter | Description |
| --- | --- |
| num | Device ID of the device that owns the changed variable |
| num | Variable ID of the changed variable |
| str | New value of variable that has changed |


### Returns

`None`


### Usage Note

Watched variables are variables that belong to other devices in the system, not variables that necessarily belong to a DriverWorks driver.


### Example

This example function prints the value of the device ID, variable ID, and variable value when any watched variable changes: 

```lua
function OnWatchedVariableChanged(idDevice, idVariable, strValue)
  print("Variable changed...")
  print("  device: " .. idDevice)
  print("  variable: " .. idVariable)
  print("  value: " .. strValue)
  print("-----------")
end
```