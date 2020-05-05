## FileList

Used to retrieve a table of all the files that are present or nil if none exist. This API can be invoked during
OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileList`



### Example  

Deleting all files:

```
  fileNames = C4:FileList()
  if (fileNames) then
     for index,value in pairs(fileNames) do
       C4:FileDelete(value)
     end
  end
```