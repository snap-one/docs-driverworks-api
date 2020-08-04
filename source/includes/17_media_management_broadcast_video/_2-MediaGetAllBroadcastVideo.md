## MediaGetAllBroadcastVideo

This function is used to retrieve all the broadcast video stations associated with this device. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaGetAllBroadcastVideo() `


Parameters

`None`


`Returns`

| Values | Description |
| --- | --- |
| Table | Table containing Media IDs and the stations locations as the values. |


### Example

```lua
local stations = C4:MediaGetAllBroadcastVideo()
  for mediId,loc in pairs(stations) do
    print("id " .. mediId .. " location " .. loc)
end
```