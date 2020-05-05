## MediaAddBroadcastVideoInfo

This function is used to add a new broadcast video station media entry. This API should not be invoked during OnDriverInit.  

###### Available from 1.6.0


### Signature

`C4:MediaAddBroadcastVideoInfo()`


| Parameters | Description |
| --- | --- |
| str | location |
| str | title |
| table | The table will have key of the media id and the stations locations as the values |


### Returns

| Value | Description |
| --- | --- |
| num | The new Media ID for the station |


### Example

`mediaId1 = C4:MediaAddBroadcastVideoInfo("https://kutv.com/watch,"KUTV",bcVideoKUTV)`