## GetBlobByName

Returns the un-encoded string containing the firmware update data of the specified BLOB (Binary Large Object). This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:GetBlobByName(name)`


| Parameter | Description |
| --- | --- |
| name | Name of the Binary Large Object to retrieve from the .c4i file. |


### Returns
Binary data from the driver file.


### Example

`C4:("Blob1")`
