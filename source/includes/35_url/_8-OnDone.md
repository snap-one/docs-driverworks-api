## OnDone

Sets a callback function that will be called when the entire transfer succeeded or failed.  It is only called once at the end of the entire transfer regardless of how many responses have been received. Note that this method can only be called before a transfer was started.

###### Available from 2.10.5


### Signature

`C4:OnDone(func)`


|PArameter | Description |
| --- | --- |
| func | A callback function of type func(transfer, responses, errCode, errMsg). |

### Usage Note

The transfer argument is the C4LuaUrl object that was created by the call to [C4:url()][1]. The responses argument receives a table (array) of the response tables in the order that they were received.  These response tables are the same ones that were passed to the callback functions set by [OnHeaders()][2], [OnBody()][3], and [OnBodyChunk()][4].

If the transfer succeeded, the errCode argument will be 0 and errMsg will be nil.  If the transfer was aborted by one of the callback functions the errCode argument will be -1.  Otherwise, errCode will hold a number with an error code and the errMsg argument will contain a string with details.

Once the transfer has completed (or failed), the C4LuaUrl object cannot be re-used.  A new instance will need to be created by a call to [C4:url()][5].


### Returns

A reference to itself.

[1]:	https://snap-one.github.io/docs-driverworks-api/#url-interface
[2]:	https://snap-one.github.io/docs-driverworks-api/#onheaders
[3]:	https://snap-one.github.io/docs-driverworks-api/#onbody
[4]:	https://snap-one.github.io/docs-driverworks-api/#onbodychunk
[5]:	https://snap-one.github.io/docs-driverworks-api/#url-interface