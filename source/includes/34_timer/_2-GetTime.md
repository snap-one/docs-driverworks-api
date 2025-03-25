## GetTime

This API enables Lua drivers to retrieve the number of milliseconds since the epoch (1 January 1970 00:00:00 UT). 
See: [https://en.wikipedia.org/wiki/Epoch\_(computing)][1]


This API was added in conjunction with O.S. 3.2.3. The units and fractional arguments were added in conjunction with O.S. 4.0.0 to give driver developers greater control over the values that are returned.


### Signature

`C4:GetTime()`


### Params
`None`


### Returns

| Valuer | Description                                                                                                                                                                                                                            |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| num    | sec: Number of milliseconds since the epoch.                                                                                                                                                                                           |
| str    | units (optional) Specifies the units for the returned value. If omitted or given an invalid value, the default behavior is to return the number of milliseconds that have elapsed since the epoch. Valid values include the following: |
|        | **us**: microseconds **ns**: nanoseconds **min**: minutes **s**: seconds **h**: hours **d**: days **w**: weeks **y**: years dec: decades                                                                                               |
| bool   | fractional (optional): Specifies whether the returned value includes the fractional portion of the elapsed time element.                                                                                                               |


### Examples

`C4:GetTime("min", true)` 
Returns the fractional number of minutes that have elapsed. This value might be something like the following: 28818247.1205

`C4:GetTime("min")` 
Returns the whole number of minutes that have elapsed. This value might be something like the following: 28818247

[1]:	https://en.wikipedia.org/wiki/Epoch_(computing) "Epoch Date in Computing"