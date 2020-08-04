## Overview

In conjunction with OS 3, drivers can now create, modify and delete scheduled events. These events appear in the Schedule Agent in ComposerPro. Once created, System programming can be created using the events. 

Of note is the use of a unique namespace for the Scheduler APIs. Historically, API calls have been created in the same C4 namespace. For example: `C4:ApiName`. The Scheduler Agent APIs use their own namespace. For example: C4Scheduler:ApiName

As mentioned above, device drivers can now contain code to create, modify and delete scheduled events. A driver can only modify or delete events which were created by that driver. For example, consider that a driver has the need to create a simple, scheduled event which occurs on a single day. This event needs to occur on July 2nd, 2019. The Scheduler API AddSingleDayEntry can be used to accomplish this: 

### Example

```lua
function AddSingleDayEntry()
 local name = "AddSingleDayEntry Scheduled Event"
 local start_time = {
 year = 2019,
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


This newly created Event can be used in ComposerPro programming.

Numerous date and time parameters are used by the Scheduler APIs. The acceptable ranges for those parameters are as follows:

Date Parameters:

- Year: Any year greater 1970.
- Month: Value between 1 and 12, 1 being equal to January.
- Day: Value between 1 and 31, 
- Hour: Value between 0 and 23
- Minute: Value between 0 and 59

Time Parameters

- Randomize time by +/-: 0-60 minutes
- Sunrise / Sunset, Before / After: -360-360 minutes. Note that Before Sunrise and Sunset requires the use of a negative number.
- Repeats -\> Daily -\> Every \<x\> day(s): 1-100 days
- Repeats -\> Weekly -\> Every \<x\> weeks(s): 1-100 weeks
- Repeats -\> Monthly -\> Every \<x\> months(s):  1-100 months
- Repeats -\> Yearly -\> Every \<x\> day(s): 1-100 days