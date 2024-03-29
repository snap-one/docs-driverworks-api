## OnBody

Sets a callback function that will be called each time a response body has finished transferring. This function is called after the callback functions set by [OnHeaders()][1] and [OnBodyChunk()][2] but before the callback function set by [OnDone()][3]. Note that this method can only be called before a transfer was started.

###### Available from 2.10.5


### Signature

`C4LuaUrl:OnBody(func)`


| Parameter | Description |
| --- | --- |
| func |  A callback function of type func (transfer, response). Returning true from this function aborts the transfer. |

### Usage Note

 The transfer argument is the C4LuaUrl object that was created by the call to [C4:url()][4].


### Returns

A reference to itself.

The response table contains the following keys:

| Key | Type | Description |
| --- | --- | --- |
| code | num | The status code of the response, e.g. 200, 404,... |
| headers | table | A table of all received headers and their value(s) |
| body | str | The entire response body as a string. This key is absent if a callback was set with OnBodyChunk(). |

The same response table will be passed to the callback set by [OnDone()][5].  Any modifications to this table will persist, but not affect the transfer in any way.

[1]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-onheaders
[2]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-onbodychunk
[3]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-ondone
[4]:	https://snap-one.github.io/docs-driverworks-api/#url-interface
[5]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-ondone