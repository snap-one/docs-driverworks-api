## DeleteVariable

Function called from a DriverWorks driver to delete a Control4 variable for the driver. This API should not be invoked during OnDriverInit

###### Available from 1.6.0.

### Signature

`C4:DeleteVariable(identifier) `	

| Parameter | Description |
| --- | --- |
| str/num | A str or num that uniquely identifies the variable to be deleted. |

### Usage Note

If string is used, then the variable is located by name. If the value is a number, then the variable is located by ID. In addition, the value of a numeric identifier must be 
 | greater than zero. 


### Returns

`None`


### Example

Deletes the device variable named Driver Variable" from the Control4 system

`C4:DeleteVariable("Driver Variable")`
