## AddEveryXMonthsEntry

This API adds an event which occurs set number of months. For example, an event that occurs every 4 months.

###### Available from 3.0.0


### Signature

`C4:Scheduler:AddEveryXMonthsEntry(name, num_months, start_time, end_date, options`

| Parameter | Description |
| --- | --- |
| str | String value of the name of the event being added. |
| table | number of months. range (1-100) |
| table | start time includes year, month, day, hour using 24 hour clock. Minute is optional  The default time is 12:00 AM. 
| table  | end date. optional. includes: year, month, day |
| table | Table of additional, optional parameters that includes: |
| | hidden - Boolean. Defaults to false. Setting to true prevents the Event from displaying in the Scheduler Agent in ComposerPro |
| | `user_hidden` - Boolean. Defaults to false. Setting user hidden to true prevents the Event from displaying on Navigators. |
| | category - String value that is available to the driver writer to use however they see fit. Can be used to categorize events. |
| | enabled - Boolean which defaults to true. Setting enabled to false will disable the Event. |
| | locked - Boolean which defaults to false. Setting enabled to true will place the Event in a read only state. |


### Returns

| Value | Description |
| --- | --- |
| value | The added Event ID value. |


### Examples

```
function AddEveryXMonthsEntry()
	local name = "AddEveryXMonthsEntry Scheduled Event"
	local num_months = 3

	local start_time = {
	year = 2018,
	month = 6,
	day = 12,
	hour = 8,
	minute = 15
	}
	
	local options = {
	hidden = false,
	user_hidden = false,
	category = "",
	enabled = true,
	locked = false
	}
	
	local eventId = C4Scheduler:AddEveryXMonthsEntry(name, num_months, start_time, options)
end
AddEveryXMonthsEntry()
```

