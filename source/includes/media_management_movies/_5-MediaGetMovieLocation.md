## MediaGetMovieLocation

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4: MediaGetMovieLocations()`


| Parameters | Description |
| --- | --- |
| num | The Media ID of the movie. |


`Returns`

| Value | Description |
| --- | --- |
| str | The location of this media as stored in the database. |


### Example

`myLocation = C4:MediaGetMovieLocation(mediaId1)`