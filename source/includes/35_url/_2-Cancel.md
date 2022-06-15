## Cancel

Cancels a transfer that has been started by a call to the [Get()][1], [Post()][2], [Put(][3]), [Delete()][4], or [Custom()][5] methods. The C4LuaUrl object cannot be re-used after canceling a transfer.  A new instance will need to be created by a call to [C4:url()][6].

###### Available from 2.10.5


### Signature

`C4:Cancel()`


### Parameters

`None`


### Returns

Returns a reference to itself.

[1]:	https://snap-one.github.io/docs-driverworks-api/#get
[2]:	https://snap-one.github.io/docs-driverworks-api/#post
[3]:	https://snap-one.github.io/docs-driverworks-api/#put
[4]:	https://snap-one.github.io/docs-driverworks-api/#delete
[5]:	https://snap-one.github.io/docs-driverworks-api/#custom
[6]:	https://snap-one.github.io/docs-driverworks-api/#url-interface