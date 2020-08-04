## MediaGetMovieInfo

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaGetMovieInfo()`


| Parameters | Description |
| --- | --- |
| num | This is the Media ID of the movie. |
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


### Example

```lua
myMovieInfo = C4:MediaGetMovieInfo(mediaId1)
print(myMovieInfo[“title”])
```