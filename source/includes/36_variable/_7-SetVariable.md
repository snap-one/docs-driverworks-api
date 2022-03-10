## SetVariable

Function called from a DriverWorks driver to set the value of the current driver's variable. This API should not be invoked during OnDriverInit

###### Available from 1.6.0.


### Signature

`C4:SetVariable(identifier, strValue)`	


| Parameter | Description |
| --- | --- |
| identifier | A string or number that uniquely identifies the variable to be added. If the identifier value is a string, then the variable is located by name. If the value is a number, then the variable is located by ID. In addition, the value of a numeric identifier must be greater than zero. |
| strValue | The value passed here is variable type dependent. | 


### Returns

`None`


### Examples

Sets the value of the device variable named “Driver Variable” to 90:

`C4:SetVariable("Driver Variable", 90)`


