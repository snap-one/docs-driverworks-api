## OnPropertyChanged

Function called by Director when a property changes value.

###### Added in OS 1.6.0


### Signature

`OnPropertyChanged(strName)`


| Parameter | Description |
| --- | --- |
| str | Name of property that has changed. |


### Usage Note:

The value of the property that has changed can be found with: `Properties[strName]`.  Note that OnPropertyChanged is not called when the Property has been changed by the driver calling the UpdateProperty command, only when the Property is changed by the user from  the Properties Page.This function is called by Director when a property changes value.


### Example

An example function used to process property value changes.


```
function OnPropertyChanged(strProperty)
  propertyValue = Properties[strProperty]
  print("strProperty = "  .. strProperty .. " changed to: " .. propertyValue)
  if (strProperty == "Security State") then
    if propertyValue == "Disarmed" then
      -- do stuff
    elseif propertyValue == "Armed Stay" then
      -- do stuff
    elseif propertyValue == "Armed Away" then
      -- do stuff
    elseif propertyValue == "Alarm Activated" then
      -- do stuff
    end
  elseif (string.find(strProperty,"Zone") ~= nil) then
    -- do stuff 
  else
    print("No action performed for " .. strProperty .. " which has been set to: " .. Properties[strProperty])
  end
end
```
