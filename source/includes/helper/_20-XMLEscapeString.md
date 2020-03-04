## XmlEscapeString

"Escapes" the passed in string rendering any XML characters (only &, \<, and \>) in the string as characters thatare valid in an XML value. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:XMLEscapeString(strRawInput)`


| Parameter | Description |
| --- | --- |
| str | strRawInput: Raw input string, with possibly invalid characters for an XML value. |


### Returns

| Value  | Description |
| --- | --- |
| str | strEscaped: The passed in string, with all XML characters properly escaped. |


### Example

Builds an XML string with a string that could have invalid XML characters in it:

`strXmlListItem = "<text>" .. C4:XMLEscapeString .. "</text>"`