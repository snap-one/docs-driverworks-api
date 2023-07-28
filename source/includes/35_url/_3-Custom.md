## Custom

Starts a HTTP transfer with a custom request method as specified by the method argument.

###### Available from 2.10.5


### Signature

`C4LuaUrl:Custom(url, method, data, headers)`


| Parameter | Description |
| --- | --- |
| url | String of the URL to perform the PUT method on. |
| str | String of the request method. |
| str | String of the request body to be sent. |
| table | A table of request headers and values to be sent. |