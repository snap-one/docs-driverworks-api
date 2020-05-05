## AddEvent

Function called from DriverWorks driver to add a new Event.  This API should not be invoked during OnDriverInit.

###### Available in  2.8.0.


### Signature

`C4:AddEvent(num,str,str)`


| Parameter  | Description |
| --- | --- |
| number | ID value of the Event |
| str |  Event Name |
| str | Event Description where NAME is replaced by the driver name. See Event Description example below.|  


### Returns

`True or False`

True on successful addition of the Event


### Example

The example below would be displayed in Composer Pro Programming as: "When the Theater-\>AV Switch TEST DYNAMIC 3 Event Changes" This example assumes a room of Theater and a driver named AV Switch. 

`C4:AddEvent(3, "TEST_DYNAMIC_3", "When the NAME TEST_DYNAMIC_3 Event Changes")`


### Usage Note

The AddEvent function will update an event if the event ID passed in the function is already in the driver.
