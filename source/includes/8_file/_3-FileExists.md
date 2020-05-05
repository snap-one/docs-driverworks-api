## FileExists

Used to see if a file exists on the file system.  This function takes a file name and returns a bool if the file exists. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileExists()`


| Parameter | Description |
| --- | --- |
| string | File name |



### Returns

|Value | Description |
| --- | --- |
| bool |True/False |



### Example

```
    bexist = C4:FileExists("1.txt")
    if (bexist) then
	-- the file is already present on the file system
    end
```