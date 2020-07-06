## FileGetName

Used to get the name of an opened file handle.  This function takes a file handle and returns a string of the file name. An empty string is returned if the file handle is not valid. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileGetName`



### Example

	name = C4:FileGetName(fh)
	print(“Name is “ .. name)