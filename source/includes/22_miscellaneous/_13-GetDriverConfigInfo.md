## GetDriverConfigInfo

Function that returns the XML contents of a driver's config.xml file. This API should not be invoked during OnDriverInit.

###### Available from 2.8.0


### Signature

`C4:GetDriverConfigInfo(str)`


| Parameter | Description                                                                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| str       | Required. XML tag for the inner XML that is being requested. This is passed in a string format without the XML brackets. Note that the only XML tags that can be passed here are root level tags. |


### Returns

| Value | Description                                   |
| ----- | --------------------------------------------- |
| xml   | XML of the tag that is passed as a parameter. |


### Usage Note

User defined XML tags can also be returned using this function.


### Example

`C4:GetDriverConfigInfo("version")`