## MediaModifyAlbumInfo

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaModifyAlbumInfo() `


| Parameters | Description |
| --- | --- |
| num | media ID |
| str | location |
| str | name |
| table | Song information is required. Table must contain the songs you want added to the album. |
| | Song Table info: data from  MediaGetSongInfo. Required fields are title, location and track number unique for that table. |


### Returns

`None`


### Usage Note

Usage Note:A modify call does not change the media’s ID number where a delete or add call will. Modify calls are useful if programming relies on the current Media ID. For example, if a button push is programmed to play the media, and a modify call is used, the media’s current ID is maintained and programming is not impacted.


### Example

```lua
C4:MediaModifyAlbumInfo(mediaId1,"http://127.0.0.1/music/Album1M
"Modified","Some New Name", Album1)
```