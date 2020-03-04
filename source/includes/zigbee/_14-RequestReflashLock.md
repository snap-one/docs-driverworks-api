## RequestReflashLock

Function that requests permission of Director to update the device. The driver receives permission when it receives the OnReflashLockGranted call. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:RequestReflashLock()`