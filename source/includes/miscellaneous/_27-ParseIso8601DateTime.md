## ParseIso8601DateTime

Parses a ISO 8601 date/time stamp to UTC (Coordinated Universal Time). This API can be invoked during OnDriverInit.

###### Available from 2.7.0


### Signature

`C4:ParseIso8601DateTime(str[, strict])`


| Parameter | Description |
| --- | --- |
| str | The string to be parsed. |
| bool | Optional. Strict parsing type,. Defaults to false.  If enabled, leading or trailing  whitespace will cause the function to fail. |


### Returns

| Parameter | Description |
| --- | --- |
| table | similar to what a os.date("t") call would return, except that the isdst field will be missing due to it being UTC. |
| num  | The Number of the second epoch in UTC. |
| num | The fraction of a second, expressed in microseconds. |


### Usage Note

If the functions fails, nothing is returned.


### Example

```
local t, epoch, microsecs = C4:ParseIso8601DateTime("2014-01-01T12:01:00.750+01:00")
print(os.date("%x %X", os.time(t)) .. " and " .. microsecs .. " microseconds")
print("Seconds since epoch (utc) = " .. epoch)
t = C4:ParseIso8601DateTime("   2014-01-01T12:01:00.750+01:00  ", true)
print("t = " .. tostring(t))
--[[
  Example output:
   01/01/14 11:01:00 and 750000 microseconds
   Seconds since epoch (utc) = 1388574060
   t = nil
--]]
```