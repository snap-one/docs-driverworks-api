## GetProjectProperty

GetProjectProperty takes a single string parameter from a list of property names. The API returns the value of that property, if it exists.

###### Added in OS 3.0.0


### Signature

`C4:GetProjectProperty(propertyName)`


| Parameter | Description |
| --- | --- |
| str | Name of Property. Includes the following: |

- ZipCode
- Latitude
- Longitude
- CountryCode
- CountryName
- CityName
- Use24HourClock
- CIDRules
- TemperatureScale
- CustomColors
- PushSettings
- SSLOnly
- DinRailPanel
- DinRailArcFail
- NominalVoltage
- KeyCapFinish
- BackLight
- TextSize
- TextAlignment
- TopLEDOn
- TopeLEDOff
- BottomLEDOn
- BottomLEDOff
- ToggleLEDOn
- ToggleLEDOff


### Example

```lua
Use Properties in a comparison:
if (Properties[“CalculateWindShear”] == “true”) then
    	CalculateWindShear()
end

Print out all Properties:
for PropertyName, PropertyValue in pairs(Properties) do 
  print(PropertyName, PropertyValue)
end
```