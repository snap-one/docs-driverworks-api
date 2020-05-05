## UpdateProperty

Function called from DriverWorks driver to update driver properties. This API should not be invoked during OnDriverInit.

###### Added in OS 1.6.0


### Signature

`C4:UpdateProperty(strName, strValue)`


| Parameter | Description |
| --- | --- |
| str | Name of Property to update.
| str | New value of Property. |


### Returns

`None`


### Examples

Examples of how the properties are updated by the driver. 

`C4:UpdateProperty("Security State","Armed "..armMode)`

`C4:UpdateProperty("Security State","Disarmed")`
