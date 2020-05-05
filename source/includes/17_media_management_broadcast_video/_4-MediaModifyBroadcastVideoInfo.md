## MediaModifyBroadcastVideoInfo

Modifies a broadcast video channel.  This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaModifyBroadcastVideoInfo() `

| Parameters | Description |
| --- | --- | num | media ID
| str | location |
| str | name |
| table | The table will have key of location, name, description and genre of the broadcast video channel modifications. |


### Returns

`None`


### Usage Note

A modify call does not change the media’s ID number where a delete or add call will. Modify calls are useful if programming relies on the current Media ID. For example, if a button push has is programmed to play the media, and a modify call is used, the media’s current ID is maintained and programming is not impacted.