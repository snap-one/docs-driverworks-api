## MediaGetAllAlbums

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaGetAllAlbums() `


Parameters

`None`


`Returns`

| Value | Description |
| --- | --- |
| Table | Table containing Media IDs and locations. |


### Example

```
Example
allAlbums = C4:MediaGetAllAlbums()
for key,value in pairs(allAlbums) do
print("mediaId is "..key.. " location is "..value)
end
```