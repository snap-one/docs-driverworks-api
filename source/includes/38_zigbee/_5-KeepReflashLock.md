## KeepReflashLock

If a driver takes longer than a minute to upload the firmware data to the device, it should call C4:KeepReflashLock. This request will maintain the reflash lock while updating. If a driver does not call KeepReflashLock, the Reflash Lock will be revoked after approximately one minute. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:KeepReflashLock()`
