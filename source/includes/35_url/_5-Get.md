## Get

Starts a HTTP GET transfer. Note that the maximum amount of data that can obtained using this function is 4,194,304 bytes. For downloading larger amounts of data to storage, please see the [C4:DownloadFile][1] function.

###### Available from 2.10.5


### Signature

`C4LuaUrl:Get(url, headers)`


| Parameter | Description |
| --- | --- |-
| url | String of the URL to perform the  GET E method on. |
| table | A table of request headers and values to be sent. |


### Returns

A reference to itself.

[1]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-downloadfile