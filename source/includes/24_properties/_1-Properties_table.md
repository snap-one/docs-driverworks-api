## Properties Table

The Lua Table ‘Properties’ contains the current value of this driver’s properties.  Although you can read from this table, and change properties’ values on the devices’ Properties page, to change the value of a device property programmatically, you should use C4: UpdateProperty.

###### Added in 1.6.0.


### Signature

`Properties[strName]`


### Example

```
Use Properties in a comparison:
if (Properties[“CalculateWindShear”] == “true”) then
    	CalculateWindShear()
end

Print out all Properties:
for PropertyName, PropertyValue in pairs(Properties) do 
  print(PropertyName, PropertyValue)
end
```