## MediaAddMovieInfo

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaAddMovieInfo ()`


| Parameters | Description |
| --- | --- |
| str | location |
| str | title |
| table | Table information. The table may have entries for: |
| | string location |
| | string title |
| | string directors – comma separated |
| | string description |
| | string cast – comma separated |
| | string rating |
| | string rating reason |
| | string reviews |
| | string genre |
| | string aspect ratio | 
| | string release date |
| | string release company |
| | string length – time span in minutes |
| | string cover art – this is a base64 encoded JPEG file of the cover art. |


### Returns

| Values | Description |
| --- | --- |
| num  | The new Media ID for the movie |


### Example

`mediaId1 = C4:MediaAddMovieInfo("http://127.0.0.1/movies/shrek1", "shrek1", shrekMovie)`