## OnBodychunk

Sets a callback function that will be called each time a chunk of the response body has transferred.  This does not necessarily correlate to chunks in the context of the HTTP "chunked" transfer encoding. This function may be called multiple times for each response, following the callback function set by OnHeaders() and before the callback function set by [OnBody()][1] and [OnDone()][2]. Note that this method can only be called before a transfer was started. This callback function is not needed for most use-cases.

###### Available from 2.10.5


### Signature

`C4:OnBodyChunk(func)`


| Parameter | Description |
| --- | --- |
| func |  A callback function of type func (transfer, response, chunk). Returning true from this function aborts the transfer. |

### Usage Note

The transfer argument is the C4LuaUrl object that was created by the call to [C4:url()][3].


### Returns

A reference to itself.

The response table contains the following keys:

| Key | Type | Description |
| --- | --- | --- |
| code | num | The status code of the response, e.g. 200, 404,... |
| headers | table | A table of all received headers and their value(s) |

The same response table will be passed to the callbacks set by [OnBody()][4] and [OnDone()][5]. Any modifications to this table will persist, but not affect the transfer in any way.

The chunk argument is a string of the received chunk of the response body.  By using the [OnBodyChunk()][6] callback, it is up to the driver process and/or store the data as needed.  In this case, the interface does not aggregate the response body, and it is not stored in the body key of the response table.

[1]:	https://control4.github.io/docs-driverworks-api/#onbody
[2]:	https://control4.github.io/docs-driverworks-api/#ondone
[3]:	https://control4.github.io/docs-driverworks-api/#url-interface
[4]:	https://control4.github.io/docs-driverworks-api/#onbody
[5]:	https://control4.github.io/docs-driverworks-api/#ondone
[6]:	https://control4.github.io/docs-driverworks-api/#onbodychunk