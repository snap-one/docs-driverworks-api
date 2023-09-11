## tohex

Function called from DriverWorks driver to convert a text string of hex into a string with hex values in it. Typically used when a protocol sends commands that are hex values. Note that for convenience, the print function can be called without prefacing with C4: This API can be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`tohex(strHex)`


| Parameter  | Description |
| --- | --- |
| str | Text to convert to binary hex. |


### Returns

`None`


### Example

Store the HEX code for a discrete Power On command for a Mitsubishi TV: 

`POWER_ON = tohex("DF 80 70 F8 02 00 00")`	
