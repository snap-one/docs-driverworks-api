## MediaGetAlbumInfo

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4: MediaGetAlbumInfo`


| Parameters | Description |
| --- | --- |
| num | This is the Media ID of the album. |


`Returns`

| Value | Description |
| --- | --- |
| str | location |
| str  | title |
| table | Table information. The table may have entries for:
| | artist |
| | record label |
| | release date |
| | description |
| | genre |
| | cover\_art – this is a base64 encoded JPEG file of the cover art. |
| | songs – an array of songs. Each song is a table, and must contain entries for |
| | name |
| | track number |
| | location |


### Example

```
MyAlbumInfo= C4:MediaGetAlbumInfo(mediaId1)
print(MyAlbumInfo["name"])
```