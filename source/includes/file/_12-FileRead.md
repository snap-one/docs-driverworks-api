## FileRead

Used to read data from a file.  Returns an empty string if no bytes are read. This function takes a file handle and number of bytes to be read. If an end of file is reached with this read operation, a string of what data was read is returned and any subsequent calls to FileRead will return an empty string. Use the FileIsValid() call to see if and end of file condition has been reached. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileRead`



| Parameter | Description |
| --- | --- |
| int | File handle |
| num | Number of bytes to be read. |



### Returns

| Value | Description |
| --- | --- |
| string | Read data or empty string |



### Example

`fileData = C4:FileRead(fh, 10)`