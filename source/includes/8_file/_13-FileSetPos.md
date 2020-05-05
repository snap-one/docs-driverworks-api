## FileSetPos

Used to set the position within the file to read or write from. This function takes a file handle and number for the new position. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileSetPos`



| Parameter | Description |
| --- | --- |
| int | File handle |
| num | Number of position. |



### Example

`C4:FileSetPos(fh, 50)`