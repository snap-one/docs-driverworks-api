## FileWriteString

Function to write a string to an opened file handle.

###### Available from 1.6.0.



### Signature

`C4:FileWriteString`


| Parameter | Description |
| --- | --- |
| int | File handle |
| str | String to be written |


### Returns

| Value | Description |
| --- | --- |
| int | Number of bytes written or -1 if there is an error. |



### Usage Note

Use the `C4:FileOpen()` call to obtain a valid file handle.



### Example

```
fh = C4:FileOpen("test.txt")
if (fh == -1) then
  	-- the file failed to open
 return
 end

numWritten = C4:FileWriteString(fh, "test1234")
 print("Bytes written " .. numWritten)

C4:FileClose(fh)
Output: Bytes written
```