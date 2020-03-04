## GetLocale

Function to get the current locale of the system. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:GetLocale()`


### Parameters

`None`


### Returns

String of local.


### Example

```
print("Current locale is " .. C4:GetLocale())
 Output: Current locale is C

```
