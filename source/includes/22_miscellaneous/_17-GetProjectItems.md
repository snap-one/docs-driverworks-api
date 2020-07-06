## GetProjectitems

Returns the project as an .XML string. This string can then be parsed to retrieve variable IDs. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:GetProjectItems()`


| Parameter | Description |
| --- | --- |
| str | Project name |


### Returns

| Value | Description |
| --- | --- |
| str | Project in XML format. |


### Usage Note

Filters can be applied to GetProjectItems(). Each filter is a separate string parameter to the function. The list of filters include:

`ALL`

`LOCATIONS`

`PROXIES`

`DEVICES`

`AGENTS`

`LIMIT_DEVICE_DATA`

`JUST_CAPABILITIES`

`NO_ROOT_TAGS`

 
For example to get just the general information about the project i.e. location, dealer info, etc.. call:


`local proj = C4:GetProjectItems("LOCATIONS", "LIMIT_DEVICE_DATA","NO_ROOT_TAGS")`


### Example

`Print (C4:GetProjectItems(projectname))`







