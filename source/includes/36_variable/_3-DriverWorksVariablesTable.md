## DriverWorks Variable Table

The Lua Table ‘Variables’ contains the current value of this driver’s variables.  Although you can read directly from this table, to change the value of a device variable, you should use: `C4:SetVariable(strName, strValue)`

###### Available from 1.6.0.


### Examples

```lua
Use Variables in a comparison:
if (Variables["Power State"] == "OFF") then
    C4:SendToSerial(idSerialBinding, "__ON__")
    C4:SetVariable("Power State", "ON")
end
```

Print out all Variables:

```lua
for VariableName, VariableValue in pairs(Variables) do 
    print(VariableName, VariableValue) 
end
```

