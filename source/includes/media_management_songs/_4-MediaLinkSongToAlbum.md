## MediaLinkSongToAlbum

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaLinkSongToAlbum()` 


| Parameters | Description |
| --- | --- |
| num | The Media ID of the album |
| num | The Media ID of the song |
| num | Track-based sequence that this song belongs within the album |


### Returns

`None`


### Example

`C4:MediaLinkSongToAlbum(mediaIdAlbum, mediaIdSong, 1)`
