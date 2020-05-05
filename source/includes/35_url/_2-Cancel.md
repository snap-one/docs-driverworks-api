## Cancel

Cancels a transfer that has been started by a call to the Get(), Post(), Put(), Delete(), or Custom() methods. The C4LuaUrl object cannot be re-used after canceling a transfer.  A new instance will need to be created by a call to C4:url().

###### Available from 2.10.5


### Signature

`C4:Cancel()`


### Parameters

`None`


### Returns

A reference to itself.
