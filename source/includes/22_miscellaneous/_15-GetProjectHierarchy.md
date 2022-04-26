## GetProjectHierarchy

This API returns a table. The table is a representation of the project. The table consists of key/value pairs where the key is the ID of the location. The value is a table with entries of all of the location’s children if any. It also contains the locations name and type.

###### Available from 2.10.0


### Signature

`C4:GetProjectHierarchy()`


| Parameter | Description |
| --- | --- |
| str | location (optional) – The location parameter can be passed to identify a specific place in the project where project hierarchy data will be returned. All children of the location specified (including itself) will be included in the results.|


### Returns

| Value | Description |
| --- | --- |
table | Table that represents the project hierarchy.