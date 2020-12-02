## SendDataToUI

Function to send data to subscribed navigators. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

This API has a dual signature. It can be used to send an XML string or a command with parameters.

`C4:SendDataToUI (xml)`


| Parameter | Description |
| --- | --- |
| str |  xml string to send |

`C4:SendDataToUI (strCommand, tParams)`


| Parameter | Description |
| --- | --- |
| strCommand |  Command to be sent to subscribed navigators. |
| tParams | Lua table of parameters for the command. |

### Returns

`None`


### Usage Note

The xml must be properly formatted and escaped for the function to succeed. Only navigators that have set up subscriptions to receive data from this device will receive sent data.


### Example

Sending XML string:

`C4:SendDataToUI("<myxml>xml data to be sent to navs</myxml>")`

Sending command with parameters:

`C4:SendDataToUI("DRIVER_COMMAND", { PARAM1 = "Data1", PARAM2 = "Data1" })`
