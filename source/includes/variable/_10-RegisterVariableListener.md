## RegisterVariableListener

Function called from a DriverWorks driver to set a listener on a particular device’s variable.
When a listener is set on a variable, whenever the variable changes, the Lua OnWatchedVariableChanged call is called.

###### Available from 1.6.0.


### Signature

`C4:RegisterVariableListener(idDevice, idVariable) `	


| Parameter | Description |
| --- | --- | 
| num | Device ID of the device that owns the changed variable |
| num | Variable ID of the changed variable |


### Returns

`None`


### Usage Notes

User Variables belong to the Variable Agent, with a DeviceID of 100001. The OnWatchedVariableChanged function will be called immediately after the listener is successfully set.

This API will fail if the variable does not exist.

### Example

This example watches the value of the temperature and HVAC mode variables on a Control4 Thermostat registered with the system as device 84.  It also registers to watch for changes to the user variable 209: 

```
C4:UnregisterVariableListener(84, 1000)
C4:UnregisterVariableListener(84, 1003) C4:UnregisterVariableListener(100001, 209)
C4:RegisterVariableListener(84, 1000)
C4:RegisterVariableListener(84, 1003)
C4:RegisterVariableListener(100001, 209)

function OnWatchedVariableChanged(idDevice, idVariable, strValue)
  print("Variable changed...")
  print("  device: " .. idDevice)
  print("  variable: " .. idVariable)
  print("  value: " .. strValue)
  print("-----------")
end
```
