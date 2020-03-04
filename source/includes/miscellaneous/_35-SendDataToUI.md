## SendDataToUI

Function to send data to subscribed navigators. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:SendDataToUI (xml)`


| Parameter | Description |
| --- | --- |
| str |  xml string to send |


### Returns

`None`


### Usage Note

The xml must be properly formatted and escaped for the function to succeed. Only navigators that have set up subscriptions to receive data from this device will receive sent data.


### Example

`C4:SendDataToUI("<myxml>xml data to be sent to navs</myxml>")`
