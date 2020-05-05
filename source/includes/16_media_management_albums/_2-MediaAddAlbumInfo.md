## MediaAddAlbumInfo

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaAddAlbumInfo ()`


| Parameters | Description |
| --- | --- |
| str | location |
| str | title |
| table | Songs information is required. Table must contain the songs you want added to the album. |
| data |  Data from MediaGetSongInfo: required fields are: `title, location, track_no` unique for that table |


### Returns

| Value | Description |
| --- | --- |
| num  | The new Media ID for the movie |


### Example

`mediaId = C4:MediaAddAlbumInfo("http://127.0.0.1/music/Album1", "Funky Music", Album1)`