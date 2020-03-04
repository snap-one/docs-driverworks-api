## ToStringLocaleC

String helper function to convert a number to a string using the ‘C’ locale regardless of the locale setting of the Control4 Operating System. Some countries use commas instead of decimal points for floating point numbers.
Lua ‘tostring’ command and string concatenation (..) with a number variable will convert the decimal value from a decimal point to a comma in some countries (locales). There may be instances where you do not want this conversion to take place and want the floating-point number to always be represented using a decimal point as opposed to a comma. In these cases, the C4:ToStringLocaleC(num) command can be used to convert the number to a string using decimal points.

###### Available from 1.6.0.


### Signature

`C4:ToStringLocaleC (num)`


| Parameter | Description |
| --- | --- |
| num | The number to convert (may be a floating-point number) |


### Example

The xml schema for extras functionality for thermostat proxy drivers requires that all floating-point numbers be represented using a period for the (decimal point). Using string concatenation to generate the extras xml would produce xml with the comma for the floating-point number if the locale is set to a country that uses commas.
 
For example, if you have a thermostat that supports an “Auto Temperature” that is not supported by the proxy that you would like displayed under “Extras” in the Thermostat UI you would need to generate the “Extras” xml to send to the UI. If the temperature represented is a floating-point number then when this number is converted to a string with ‘tostring’ or string concatenation (..), it would be converted to a number represented with a comma. In this case you would want to use the C4:ToStringLocaleC() API to convert the floating number appropriately.