## FileDelete

Used to delete a file on the file system.  This call will fail if there is a opened handle to the file. This function takes a file name to delete and returns a bool if the delete succeeded. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileDelete()`



| Parameter | Description |
| --- | --- |
| string | File name |



### Returns

| Value | Description |
| --- | --- |
| bool | True/False |



### Example

`C4:FileDelete("1.txt")`