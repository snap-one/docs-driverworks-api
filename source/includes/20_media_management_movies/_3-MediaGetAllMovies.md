## MediaGetAllMovies

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaGetAllMovies()`


Parameters

`None`


`Returns`

| Value | Description |
| --- | --- |-
| Table | Table containing Media IDs and locations. |


### Example

```
allMovies = C4:MediaGetAllMovies()
for key,value in pairs(allMovies) do
   print("mediaId is "..key.. " location is "..value)
end
```