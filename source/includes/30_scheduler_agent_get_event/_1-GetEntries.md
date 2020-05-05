## GetEntries

Deletes an Event based on the Event ID value passed. A driver can only delete events which were created by that driver.

###### Available from 3.0.0


### Signature

`C4Scheduler:GetEntries()`


| Parameter | Description |
| --- | --- |
| Value| Description |
| table | ID/Name key value pairs. The entries returned are only entries created by the driver. For example: |

```
{
 1  entry1name
 2  entry2name
 3  entry3name
 4  entry4name
}   
```