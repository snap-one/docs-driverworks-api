## InvalidateState

Function to notify director that data from this driver has been modified and needs to be persisted. This API should not be invoked during OnDriverInit.


### Signature

`C4:InvalidateState()`


### Usage Note

Prior to Operating System 2.10, overuse of C4:InvalidateState() was an issue as persisting extraneous data through a driver had performance implications. Beginning with Operating System 2.10, it is no longer necessary to cause driver data to be persisted. Drivers should use the PersistSetValue and PersistGetValue functions to store data that will be required across system restarts.