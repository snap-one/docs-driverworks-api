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

_See example to the right._

```lua
fh = C4:FileOpen(“somefile.ext”)
if (fh == -1) then
	-- the file failed to open
end
```


### Usage Note

The `C4:FileOpen()` function always opens a file so that the position is at end-of-file. For example:

`local f = io.open(fullfilePath, "rba")`

Opening the file as illustrated above opens the file for read, binary, and append (rba). This means that anything written to the file occurs at the end of the file. This ensures that writes don't overwrite existing data.

However, this also means that attempts to read the file will not return any data because the current read position is at end-of-file.

The example given above can be corrected by using the [C4:FileSetPos()][1] function to reset the position to the beginning of the file before reading. See the example to the right.

```lua
C4:FileSetDir(parentdir)
local fh = C4:FileOpen(fileName without path)
if (fh ~= -1) then
    C4:FileSetPos(fh, 0)
    local fileSize = C4:FileGetSize(fh)
    local fileContents = C4:FileRead(fh,fileSize)
    C4:FileClose(fh)
end
```

[1]:	https://snap-one.github.io/docs-driverworks-api/#file-interface-filesetpos