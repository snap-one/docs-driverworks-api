## OnBindingValidate

The OnBindingValidate API supports validation by a driver before Director adds a new binding. This enables drivers to reject bindings that aren't valid due to some internal, dynamic state.

###### Available from 1.6.0


### Signature

`OnBindingValidate(idBinding, strClass) `


| Parameter | Description |
| --- | --- |
| num | ID of the network binding being validated |
| str  |  Class of the Binding. |