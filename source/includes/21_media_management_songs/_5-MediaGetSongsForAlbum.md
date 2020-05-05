## MediaGetSongsforAlbum

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaGetSongsforAlbum() 
`

| Parameters | Description |
| --- | --- |
| num | The Media ID of the album containing songs |


### Returns

| Value | Description |
| --- | --- |
| table | Values including Media ID and location for each song. |


### Example

```

AllSongs= C4:MediaGetSongsForAlbum(mediaIdAlbum)
for key,value in pairs(AllSongs) do
print("mediaId is "..key.. " location is "..value)
end
```
