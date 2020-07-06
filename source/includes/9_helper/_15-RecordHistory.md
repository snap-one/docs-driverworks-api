## RecordHistory

Helper Function that writes history events to the History Agent database. 

###### Available from 1.6.0.


### Signature

`C4:RecordHistory(severity, eventType, category, subcategory, description)`


|Parameter  | Description |
| --- | --- |
| str | Severity: Valid parameters include: “Critical”, “Warning”, or “Info" |
| str | eventType: Describes the type of event within a category. Each category would define specific types of history event. For example, the Security category could define the following event types: Arm, Disarm, Open, Close, Alarm, etc. |
| str | Category: Represents the high level logical group that the device or source belongs to. These  categories may correlate to Navigator categories, but could include additional categories. For example: Security, Lighting, Comfort, System etc. |
str | Subcategory: An optional subcategory can be included. The sub category provides additional event criteria that may be used to query for events. |
| str | Description: Brief description. |


### Returns

`None`


### Example

`C4:RecordHistory(“Critical”,"Disarm”,"Security”,”Front Door”,”The front door was disarmed.")`