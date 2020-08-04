## MediaAddSongInfo

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaAddSongInfo()`


### Parameters

`None`


### Returns

| Value | Description |
| --- | --- |
| table | Information for location and title. |


### Example

```lua
mySongInfo = C4:MediaGetSongInfo(mediaId1)
print(mySongInfo["name"])
```