## SetVariable

Function called from a DriverWorks driver to set the value of the current driver's variable. This API should not be invoked during OnDriverInit

###### Available from 1.6.0.


### Signature

`C4:SetVariable(identifier, strValue)`	


| Parameter | Description |
| --- | --- |
| str/num | A string or number that uniquely identifies the variable to be set.
| num | Numerical value specifying the Variable Type: 0 = true, 1 = false. |


### Usage Note

If the value is a string, then the variable is located by name. If the value is a number, then the variable is located by ID. In addition, the value of a numeric identifier must be greater than zero. 


### Returns

`None`


### Examples

Sets the value of the device variable named “Driver Variable” to 90:

`C4:SetVariable("Driver Variable", 90)`


