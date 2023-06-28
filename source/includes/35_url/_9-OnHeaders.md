## OnHeaders

Sets a callback function that will be called each time all of the headers of a response have been received but, before the response body has been received. This function may be called multiple times, e.g. due to redirects. Note that this method can only be called before a transfer was started.

###### Available from 2.10.5


### Signature

`C4:OnHeaders(func)`


|Parameter | Description |
| --- | --- |
| func |  A callback function of type func (transfer, response, chunk). Returning true from this function aborts the transfer.

### Usage Note

The transfer argument is the C4LuaUrl object that was created by the call to [C4:url()][1].


### Returns

A reference to itself.

The response table contains the following keys:

| Key | Type | Description |
| --- | --- | --- |
| code | num | The status code of the response, e.g. 200, 404,... |
| headers | table | A table of all received headers and their value(s) |

The same response table will be passed to the callbacks set by the following:

[OnBody()][2]

[OnBodyChunk()][3]

[OnDone()][4]

Any modifications to this table will persist but not affect the transfer in any way.


### Example

```lua
OnHeaders(
	function(transfer, response)
		-- transfer is the object returned by C4:url()
		print("OnHeaders: status code: " .. response.code)
		for hdr,val in pairs(resp.headers) do
			print("OnHeaders: header " .. hdr .. " = " .. val)
		end
		-- return true -- to abort the transfer
    end
```

[1]:	https://snap-one.github.io/docs-driverworks-api/#url-interface
[2]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-onbody
[3]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-onbodychunk
[4]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-ondone