## AddDaysOfTheWeekEntry


This API adds an event which occurs on defined days of the week.


###### Available from 3.0.0


### Signature

`C4Scheduler:AddDaysOfTheWeekEntry(name, days_of_the_week, start_time, end_date, options)`


| Parameter | Description |
| --- | --- |
| str | String value of the name of the event being added. |
| str | Weekday values of: SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY |
| table | start time includes year, month, day, hour using 24 hour clock. minute is optional  The default time is 12:00 AM. |  
| table  | end date. optional. includes: year, month, day |
| table | Table of additional, optional parameters that includes: |
| | hidden - Boolean. Defaults to false. Setting to true prevents the Event from displaying in the Scheduler Agent in ComposerPro |
| | `user_hidden` - Boolean. Defaults to false. Setting user hidden to true prevents the Event from displaying on Navigators. |
| | category - String value that is available to the driver writer to use however they see fit. Can be used to categorize events. |
| | enabled - Boolean which defaults to true. Setting enabled to false will disable the Event. |
| | locked - Boolean which defaults to false. Setting enabled to true will place the Event in a read only state. |


### Returns

| Valuer | Description |
| --- | --- |-
| value | The added Event ID value. |


### Examples

```lua
function AddDaysOfTheWeekEntry()
	local name = "AddDaysOfTheWeekEntry Scheduled Event"
	local days_of_the_week = {"MONDAY", "WEDNESDAY", "FRIDAY"}

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
	
	local eventId = C4Scheduler:AddDaysOfTheWeekEntry(name, days_of_the_week, start_time, options)
end
AddDaysOfTheWeekEntry()
```
