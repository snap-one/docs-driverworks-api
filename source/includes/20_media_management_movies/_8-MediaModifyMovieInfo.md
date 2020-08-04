## MediaModifyMovieInfo

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaModifyMovieInfo()`


| Parameters | Description |
| --- | --- |
| num | media ID |
| str | location |
| str | name |
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

`None`


### Usage Note

A modify call does not change the media’s ID number where a delete or add call will. Modify calls are useful if programming relies on the current Media ID. For example, if a button push has is programmed to play the media, and a modify call is used, the media’s current ID is maintained and programming is not impacted.


### Example

`C4:MediaModifyMovieInfo(mediaId1,"http://127.0.0.1/movies/shrek1Modified","shrek1",shrekMovie)`
