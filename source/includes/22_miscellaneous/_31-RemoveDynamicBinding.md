## RemoveDynamicBinding

Function called by a DriverWorks driver to remove a dynamically created binding. This API should not be invoked during OnDriverInit. No Events will be sent prior to OnDriverlateInit. If an event is required, this method must be invoked in OnDriverlateInit.

###### Available from 1.6.0


### Signature

`C4:RemoveDynamicBinding(idBinding)`


| Parameter | Description |
| --- | --- |
| num | ID of the dynamic binding to remove. |


### Returns

`None`




