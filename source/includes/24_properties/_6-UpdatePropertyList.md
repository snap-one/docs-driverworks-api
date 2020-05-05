## UpdatePropertyList

Function called from DriverWorks driver to update driver properties. This API should not be invoked during OnDriverInit.

###### Added in OS 2.7.0
###### The strValue parameter was changed to strValueList in conjunction with OS 3.
###### The strValueDefault parameter was added in conjunction with OS 3.


### Signature

`C4:UpdatePropertyList (strName, strValueList, strValueDefault) `


| Parameter | Description |
| --- | --- |
| str | Name of Property to update. |
| str | New list for the property. This list needs to be a comma delimited list. |
| str | Optional but Recommended New Value of the property. This value needs to be included in the list. |


### Returns

`None`


### Examples

`C4:UpdatePropertyList("Test Dynamic List No Default", "Item 7,Item 8,Item 9", "Item 8")`