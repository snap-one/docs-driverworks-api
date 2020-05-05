## GetText

Function to get a string translated into the current locale from a “C” 9English)input string. This will only return translated strings if there is a corresponding input -\> translation match in the current translated string for the set locale. If no translation is found the input string is returned. This API can be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:GetText()`


| Parameter | Description |
| --- | --- |
| str | String to be translated |


### Returns

|Value | Description |
| --- | --- |
| str | Translated string |


### Example

`print("Translation of stop is " .. C4:GetText("stop"))`
Output: `Translation of stop is stop`

