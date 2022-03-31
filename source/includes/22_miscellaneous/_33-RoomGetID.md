## RoomGetId

Function to get the ID value of the room containing the driver. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:RoomGetId()`


### Parameters

`None`


### Returns

| Parameter | Description |
| --- | --- |
| int | Device ID of containing room. |


### Example

```
idRoom = C4:RoomGetId()
print("Room id is " .. idRoom)
```