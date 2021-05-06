## GetProjectItems

If no parameter is passed, this API returns the entire project as an .XML string. This string can then be parsed to retrieve variable IDs. The API supports several parameters (filters) that will return specific XML. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:GetProjectItems()`


| Parameter | Description |
| --- | --- |
| str | Filter: Optional. see usage note below. |


### Returns

| Value | Description |
| --- | --- |
| str | Project in XML format. |


### Example

`print(C4:GetProjectItems())
`

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

 
For example, to return general information about the project i.e. location, dealer info, etc:


`print(C4:GetProjectItems("LOCATIONS", "LIMIT_DEVICE_DATA","NO_ROOT_TAGS"))`









