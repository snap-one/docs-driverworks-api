## FileGetSize

File to get the current size of an opened file handle. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileGetSize`



| Parameter | Description |
| --- | --- |
| int | File handle |



### Return

| Value | Description |
| --- | --- |
| int | Size of the file in byte size. |



### Usage Note

Use the `c4:FileOpen()` call to obtain a valid file handle



### Example

```lua
fh = C4:FileOpen("test.txt")
	if (fh == -1) then
  	-- the file failed to open
  return
end

fileSize = C4:FileGetSize(fh)
print("File size is " .. fileSize)

C4:FileClose(fh)
```


