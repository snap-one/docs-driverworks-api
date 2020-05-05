## ModifyOptions

Modifies the options of an Event. A driver can only modify events which were created by that driver.

###### Available from 3.0.0


### Signature

`C4Scheduler:ModifyStartDate(event_id, options)`


| Parameter | Description |
| --- | --- |
| num | Number value of the Event. |
| table | Table of additional, optional parameters that includes:|
| | hidden - Boolean. Defaults to false. Setting to true prevents the Event from displaying in the Scheduler Agent in ComposerPro |  | | `user_hidden` - Boolean. Defaults to false. Setting user hidden to true prevents the Event from displaying on Navigators. |
| | category - String value that is available to the driver writer to use however they see fit. Can be used to categorize events. |
| | bool - Defaults to true. Setting enabled to false will disable the Event. |
| | bool  - Defaults to false. Setting enabled to true will place the Event in a read only state. |

