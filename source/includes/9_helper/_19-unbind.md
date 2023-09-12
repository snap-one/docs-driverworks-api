## Unbind

This API provides the ability to unbind bound devices. The unbinding of the devices binding through this API is the same as manually unbinding two devices in ComposerPro's Connections area. Note the parameters passed in the API. Both have "Consumer" designation. These parameters represent the device that consumes data from the Provider device. To verify if a device driver is a Consumer, go to the driver's \<Connections\> XML. The \<consumer\> XML tag for this device's driver will be True or:  \<consumer\>True\</consumer\>. Subsequently, the Consumer Binding ID value is the Consumer device's binding value.

###### Available from 2.9.0.


### Signature

`C4:Unbind(idDeviceConsumer, idBindingConsumer)`


| Parameter | Description |
| --- | --- |
| num | idDeviceConsumer - ID value of the device consuming data. |
| num | idBindingConsumer - Binding ID value of the binding for the Consumer Device |


### Returns

`None`


### Example

`C4:Unbind(81,1)`
