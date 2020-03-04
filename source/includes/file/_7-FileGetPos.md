## FileGetPos

Used to get the current read or write position for the file.  This function takes a file handle and returns the current position. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileGetPos`



### Example

`pos = C4:FileGetPos(fh)`