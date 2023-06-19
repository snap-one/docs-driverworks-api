## RoomSelectNav

Function to force the selection of onscreen for the selected room. This API should not be invoked during OnDriverInit.


###### Available from 1.6.0


### Signature

`C4:RoomSelectNav (int)`


| Parameter | Description |
| --- | --- |-
| int | Device ID of the room to force onscreen selection |


### Returns

`None`


### Example

`C4:RoomSelectnav(C4:RoomGetId())`