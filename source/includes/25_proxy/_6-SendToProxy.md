## SendToProxy

Function called from DriverWorks driver to send a Control4 BindMessage to the proxy bound to the specified binding. This API should not be invoked during OnDriverInit. 

###### Added in OS 1.6.0


### Signature

`C4:SendToProxy(idBinding, strCommand, tParams, strmessage)`

or

`C4:SendToProxy(idBinding, strCommand, strParam)`

or

`C4:SendToProxy(idBinding, strCommand, tParams, strmessage, allowEmptyValues)`


| Parameter | Description |
| --- | --- |
| num | Binding ID for the proxy you wish to send to |
| str | Command to send to the proxy |
| table | Lua table containing parameters to the command. |
| str | COMMAND or NOTIFY – Overrides the default message for SendToProxy. See Note below. |
| bool | Optional. When set to TRUE will allow for an empty string to be sent as a parameter value. |


### Usage Note
SendToProxy will send a NOTIFY if the paramater is equal to or more than a 1000 and a Command if it is less than a 1000.


### Returns

`None`


### Examples

Notify the attached contact binding that the contact has closed. Note that tParams is required, if there are no parameters, send an empty Lua table:

 `C4:SendToProxy(11, "CLOSED",{}, "NOTIFY")`

Notify the attached thermostat binding that the temperature is now 76:

`C4:SendToProxy(5001, "TEMPERATURE_CHANGED", {TEMPERATURE = 76})`

Send the ‘System Armed’ text to the attached security proxy Display Text:

`C4:SendToProxy(5001, "DISPLAY_TEXT", "<text>SYSTEM ARMED</text>")`

Optional allowEmptyValues parameter set to True:

`C4:SendToProxy(5001, "ALLOWED_FAN_MODES_CHANGED", tParams, "NOTIFY", true)`

Optional allowEmptyValues parameter set to True and a table defined:

`C4:SendToProxy(5001, "ALLOWED_FAN_MODES_CHANGED", {MODES = ""}, "NOTIFY", true)`

Optional allowEmptyValues parameter set to True and an empty string:

`C4:SendToProxy(5001, "ALLOWED_FAN_MODES_CHANGED", "", "NOTIFY", true)`

Optional allowEmptyValues parameter set to True and a number:

`C4:SendToProxy(5001, "ALLOWED_FAN_MODES_CHANGED", 213, "NOTIFY")`

Send the ‘System Armed’ text to the attached security proxy Display Text:

`C4:SendToProxy(5001, "DISPLAY_TEXT", "<text>SYSTEM ARMED</text>")`

