## MediaGetSongLocation

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaGetSongLocation( `


| Parameters | Description |
| --- | --- |
| num | The Media ID of the song. |


`Returns`

| Value | Description |
| --- | --- |
| str | The location of this media as stored in the database. |


### Example

`print(C4:MediaGetSongLocation(mediaId1))`