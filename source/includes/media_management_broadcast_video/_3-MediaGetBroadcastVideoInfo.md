## MediaGetBroadcastVideoInfo

This function is used to get information about an existing broadcast audio media entry. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaGetBroadcastVideoInfo() `


| Parameters | Description |
| --- | --- |
| num | media ID of the station |
| str | location |
| str | name |


### Returns

| Value | Description |
| --- | --- |
| str | location |
| str | genre |
| str | description |
| str | name |
| str | image.  this is a base64 encoded JPEG file of the cover art. |


### Example

```
myStationInfo = C4:MediaGetBroadcastVideoInfo(mediaId1)
print(myStationInfo[“name”])
```