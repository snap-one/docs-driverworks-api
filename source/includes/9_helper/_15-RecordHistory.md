## RecordHistory

Function to record a history event in the history database. This will return the UUID of the history event after it is added to the data. The UUID is used to access the database record for review or for subsequent updates. This will only record the history event if the History Agent database is initialized and running. This API can be invoked after OnDriverLateInit.

###### Available from 1.6.0.


### Signature

`C4:RecordHistory(severity, eventType, category, subcategory, event table)`


| Parameter | Description                                                         |
| --------- | ------------------------------------------------------------------- |
| string    | event severity string, value may be "Critical", "Warning" or "Info" |
| string    | event type string                                                   |
| string    | event category string                                               |
| string    | optional event subCategory string                                   |
| table     | optional event metadata table of name-value pairs, can be nil       |



### Returns

| Value  | Description                                                        |
| ------ | ------------------------------------------------------------------ |
| string | UUID string of the history event record if recorded, nil otherwise |



### Example

```lua
print ("UUID of the event is " .. C4:RecordHistory("Info", "Motion", "Cameras", "IP Camera", "This is a test", ""))


Output: 

UUID of the event is hist-evnt-recd-uuid
```
