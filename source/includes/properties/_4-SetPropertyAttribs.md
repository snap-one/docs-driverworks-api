## SetPropertyAttribs

Function called from DriverWorks driver to display or hide Properties in Composer's Lua Properties page. This API should not be invoked during OnDriverInit.

###### Added in OS 1.6.0


### Signature

`C4:SetPropertyAttribs(strName, int)`

| Parameter | Description |
| --- | --- |
| str | Name of Property |


### Returns

`None`


#### Example

The example below will prevent the property named "Resolution" from being displayed in the Lua Property page for this driver.

`C4:SetPropertyAttribs("Resolution", 1)`