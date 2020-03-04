## GetEntry

The entry returned can only be an entry created by the driver.

###### Available from 3.0.0


### Signature

`C4Scheduler:GetEntry(event_id) `


| Parameter | Description |
| --- | --- |
| num |  ID number of the event. |


### Returns

| Value | Description |
| --- | --- |
| table | Enabled - true/false |
| Description | \<string\> |
| Eventid | \<event id\> |
| `creator_state` | \<string\> |
| hidden | true/false |
| creatorid |\<creator id\> |
| category |  \<string\> |
| locked | true/false |
| xml | \<xml string\> (see example below) |
| `user_hidden` | true/false |
 

### Example

```
Sample XML – Varies depending on the settings of the event
<entry>
    <eventid>10</eventid>
    <description>AddDailyRepeatRandomOffsetEntry Scheduled Event</description>
    <category>daily_repeat</category>
    <enabled>False</enabled>
    <locked>True</locked>
    <creatorid>6</creatorid>
    <creatorstate></creatorstate>
    <hidden>False</hidden>
    <user_hidden>True</user_hidden>
    <start>
        <offset>0</offset>
        <offset_minutes>1293</offset_minutes>
        <start_date>
            <start_day>2</start_day>
            <start_month>7</start_month>
            <start_year>2018</start_year>
            <start_period>0</start_period>
            <start_weekday>0</start_weekday>
        </start_date>
        <randomize>12</randomize>
    </start>
    <repeat>
        <frequency>1</frequency>
        <rate>1</rate>
        <daymask>0</daymask>
        <end_date>
            <end_month>9</end_month>
            <end_day>23</end_day>
            <end_year>2019</end_year>
        </end_date>
    </repeat>
</entry>
```