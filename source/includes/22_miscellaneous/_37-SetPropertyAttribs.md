## SetPropertyAttribs

Function to modify the visibility of properties as viewed from Composer. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:SetPropertyAttribs(string, int)`

| Parameter | Description |
| --- | --- |
| str | Name of property to modify |
| int | 0 (to show) or 1 (to hide) |


### Returns

`None`


### Example

The following code would hide the property named “resolution” in the Lua property page for this driver:
`C4:SetPropertyAttribs("Resolution", 1)`
