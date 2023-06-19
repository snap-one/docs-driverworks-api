## GetBindingAddress

Returns a physical (IP) address of a network binding. This API should not be invoked during OnDriverInit

###### Available from 1.6.0.


### Signature

`C4:GetBindingAddress (idBinding)`

| Parameter | Description |
| --- | --- |
| num | Binding value. |


### Returns

| Value | Description |
| --- | --- |
| str | Network address or hostname that this network connection will use. |
| int | IP address of a network binding |


