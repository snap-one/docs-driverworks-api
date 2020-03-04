## FileWrite

Used to write data to a file.  This function returns the number of bytes written or -1 if file is not valid (example file has been closed). This function takes a file handle, the number of bytes of the string to be written, and a string of data to be written. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileWrite`



| Parameter | Description |
| --- | --- |
| int | File handle |
| num | Number of bytes to be written. |
| str | Data to be written |



### Returns

| Value | Description |
| --- | --- |
| num | Number of bytes written or -1 if file is not valid. |



### Example

```
foo = "\000\001\002\003\004\005\006\007\008\009"
bytesWritten = C4:FileWrite(fh, string.len(foo), foo)
```