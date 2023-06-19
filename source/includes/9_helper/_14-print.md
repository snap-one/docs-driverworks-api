## print

Function called from DriverWorks driver to prints items out the drivers’ properties page console. Note that for 
convenience, the print function can be called without prefacing with "C4:" This API can be invoked during
OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:print(strPrintText)`


| Parameter  | Description |
| --- | --- |
| str | Text to print. |


### Returns

`None`


### Usage Note

The Lua output window in ComposerPro does not necessarily display output in the order in which code is actually executed. The print API is a function implemented in Lua which causes the driver to send a DataToUI message.

DataToUI commands are not guaranteed to be in any particular order. ComposerPro simply captures this DATA and displays it. If the order of data appearing in the ComposerPro Lua window is important, Control4 suggests the use of the Director log.