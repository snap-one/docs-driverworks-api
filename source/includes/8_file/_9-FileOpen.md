## FileOpen

Used to open (if file exists) or create a new file.  This function takes a file name, returns a handle. A value
of -1 is returned if an error.  This API can be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:FileOpen` 


| Parameter | Description |
| --- | --- |
| str | File name |



### Returns

| Value | Description |
| --- | --- |
| int | File handle |



### Example

```
fh = C4:FileOpen(“somefile.ext”)
if (fh == -1) then
	-- the file failed to open
end
```