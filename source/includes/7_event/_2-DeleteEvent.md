## DeleteEvent

Function called from DriverWorks driver to delete an Event. This API should not be invoked during OnDriverInit.

###### Available in  2.8.0.


### Signature

`C4:DeleteEvent(num)`


| Parametr | Description |
| --- | --- |
| num| ID value of the Event |


### Returns

`None`


### Usage Note

The DeleteEvent API should not be used to remove Events which are defined in the driver's XML. Events defined in the XML are intended to be static. If an Event in the XMl needs to be deleted, it should be removed manually from the XML and the driver re-compiled and a new version assigned to it.

Events can be deleted regardless of their location within a set of Events. Empty Event IDs that result from this are acceptable.