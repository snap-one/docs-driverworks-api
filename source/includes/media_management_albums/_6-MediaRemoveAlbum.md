## MediaRemoveAlbum

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaRemoveAlbum() `


| Parameters | Description |
| --- | --- |
| num | The Media ID of the album.  Note, all songs associated with this album will be removed as well. |


### Returns

`None`


### Example

`C4:MediaRemoveAlbum(mediaId1)`