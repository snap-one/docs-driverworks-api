## OnVariableChanged

Function called by Director when one of this driver’s variables’ values is changed.

###### Available from 1.6.0.


### Signature

`C4:OnVariableChanged(strName)`	


| Parameter | Description |
| --- | --- |
| str | Name of variable that has changed |


### Returns

`None`


### Usage Notes

OnVariableChanged is NOT called on a driver when it changes its own variable’s value. The value of the variable that has changed can be found with: Variables strName


### Example

This simple function prints to the Lua Output window in Composer when any variable on that device changes and includes the variable name and value.

```lua
function OnVariableChanged(strName)
  print("Variable value changed - variable named: " .. strName)
  print(" ... new value is: " .. Variables[strName])
end
```