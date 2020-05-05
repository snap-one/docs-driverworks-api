## FileGetOpenedHandles

Used to retrieve a table of all the opened file handles in your sandbox or nil if none are opened. The table is index = file handle and value=file name. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:FileGetOpenedHandles()`


### Parameters

`None`


### Returns

| Value | Description |
| --- | --- |
| table | Index= File handle |
|          | Value = File Name |


### Example

Closing all opened handles:

```
  fileHandles = C4:FileGetOpenedHandles()
  if (fileHandles) then
     for index,value in pairs(fileHandles) do
       C4:FileClose(index)
     end
  end
```