## AddSingleDayEntry

This API adds an event which occurs once.

###### Available from 3.0.0


### Signature

`C4:Scheduler:AddSingleDayEntry(name, start_time, options)`


| Parameter | Description |
| --- | --- |
| str | String value of the name of the event being added. |
| table | Optional table that includes: year, month, day, hour using the 24 hour clock, minute. Default  time is 12:00 AM |
| table | Table of additional, optional parameters that includes: |
| | hidden - Boolean defaults to false.  True prevents the Event from displaying in the Scheduler Agent in ComposerPro |
| | `user_hidden` - Boolean defaults to false. Setting to true prevents the Event from displaying on Navigators. |
| | category - String value available to the driver writer to use however they see fit. Can be used to categorize events. |
| | enabled - Boolean defaults to true. Setting enabled to false will disable the Event. |
| | locked - Boolean which defaults to false. Setting enabled to true will place the Event in a read only state. |


### Returns

| Value | Description |
| --- | --- |
| value | The added Event ID value. |


### Example

```lua
function AddSingleDayEntry()
	local name = "AddSingleDayEntry Scheduled Event"

	local start_time = {
	year = 2018,
	month = 7,
	day = 2,
	hour = 21,
	minute = 30
	}
	
	local options = {
	hidden = false,
	user_hidden = false,
	category = "",
	enabled = true,
	locked = false
	}
	
	local eventId = C4Scheduler:AddSingleDayEntry(name, start_time, options)
end
AddSingleDayEntry()
```