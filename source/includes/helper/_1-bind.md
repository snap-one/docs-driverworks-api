## Bind

Note the order of the parameters passed in the Bind API. Each has a "Provider" and "Consumer" designation. The Provider designation represents the Device ID value of the device providing the data within the binding. To verify if a device driver is a Provider, go to the driver's `<Connections>` XML.This API provides the ability to create a binding between two devices: a "Provider Device" and a "Consumer Device." The binding creation through this API is the same as manually creating a binding in ComposerPro's The `<consumer>` XML tag for this device's driver will be False or:  `<consumer>False</consumer>`. Subsequently, the Provider Binding ID value is the Provider device's binding value.

###### Available from 2.9.0.



### Signature

`C4:Bind(idDeviceProvider, idBindingProvider, idDeviceConsumer, idBindingConsumer, strClass)`



| Parameter | Description |
| --- | --- |
| idDeviceProvider | ID value of the device providing data. |
| idBindingProvider | Binding ID value of the binding for the Provider Device |
| idDeviceConsumer  | ID value of the device consuming data. |
| Class | String. The binding connection class. |

The Parameters with the Consumer designation represent the device that consumes data from the Provider device.
The `<consumer>` XML tag for this device's driver will be True or:  `<consumer>True</consumer>`. Subsequently, the
Consumer Binding ID value is the Consumer device's binding value.



### Returns

`None`

