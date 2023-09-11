## FileDelete
This function has been modified in conjuction with O.S. release 3.3.0.  As part of Control4’s plan to tighten driver security, the io.popen() call has been removed. In doing this, driver developers need to use C4:File commands to accomplish what they previously did with io.popen (). Two new parameters have been added to specify an allowed Alias and a sub path and file name to a file to delete. 


### Signature

`C4:FileDelete()`


| Parameters | Description |
| --- | --- |
| string| filename |
| string | PATH\_ALIAS: Path representation/alias to an allowed location as to where a file may deleted. |
| string | SubPath: A path relative to PATH\_ALIAS and the file name for the file to delete. |


| Path Alias | Path |
| --- | --- |
| SANDBOX | /lua/sandbox/15  (location for driver with device id 15) |
| LOGGING | /var/log/debug |
| MEDIA | /media |
| C4Z |  /opt/control4/var/drivers/c4z/\<driver\_name\>  |

Note that path aliases are required and cannot be replaced with the actual path. 


### Example

Assuming that the device id of the driver is 15, the following command will delete /lua/sandbox/15/data/datafile.dat. 

`C4:FileDelete(SANDBOX, "data/datafile.dat")`



### Example

`C4:FileDelete("1.txt")`
