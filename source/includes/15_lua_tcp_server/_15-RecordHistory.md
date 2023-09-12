## RecordHistory

Function to record a history event in the history database. Beginning with O.S. 3.4.0, this function will return a UUID of an Event. This will return the UUID of the history event after it is added to the data. The UUID is used to access the database record for review or for subsequent updates. This will only record the history event if the History Agent database is initialized and running. The History Agent uses this API to include the link in a push notification. This API can be invoked after OnDriverLateInit.

###### Available in 3.4.0


### Signature

`C4:RecordHistory()`


### Parameters

| Parameter | Description                                                                                                                            |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| str       | Device ID. The Proxy ID. This is what the Navigator UI will deep link into when the user opens the Control4 app from the notification. |
| str       | Event severity string, value may be "Critical", "Warning" or "Info”.                                                                   |
| str       | Event type string.                                                                                                                     |
| str       | Event category string.                                                                                                                 |
| str       | Event subCategory string. (optional)                                                                                                   |
| str       | Event description string. (optional)                                                                                                   |
| str       | Event metadata table of name-value pairs, can be nil. (optional)                                                                       |
| table     | Event metadata table of name-value pairs, can be nil. (optional)                                                                       |

### Returns

| Value | Description                                                     |
| ----- | --------------------------------------------------------------- |
| str   | UUID string of the history event record, returns nil otherwise. |



### Example
**TODO: Need example for case with metadata and need template for metadata table format**

```xml
print ("UUID of the event is " .. C4:RecordHistory("Info", "Motion", "Cameras", "IP Camera", "This is a test", ""))

Output: 

UUID of the event is hist-evnt-recd-uuid

```



