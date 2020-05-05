## MediaModifySongInfo

This API should not be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:MediaModifySongInfo() `

| Parameters | Description |
| --- | --- |
| num | media ID |
| str | location |
| str | name |


### Returns

`None`


### Usage Note

A modify call does not change the media’s ID number where a delete or add call will. Modify calls are useful if programming relies on the current Media ID. For example, if a button push  is programmed to play the media, and a modify call is used, the media’s current ID is maintained and programming is not impacted.


### Example

`C4:MediaModifySongInfo(mediaId1, "http://127.0.0.1/music/songtest", "Test of modified song")`