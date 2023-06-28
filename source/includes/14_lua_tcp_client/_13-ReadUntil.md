
## ReadUntil

This method requests to read data until a specific condition is met. This API should not be invoked during OnDriverInit.

###### Available in 1.6.0


### Signature

`C4:ReadUntil(arg) `


| Parameters | Description |
| --- | --- |
| arg | arg can be a string, in which case  the read request will be satisfied until this string was read from the socket.  arg can also be a function, which can arbitrarily decide at what point the read request is satisfied: |
| arg (str) | All data until (and including) the value of this argument will be passed to the [OnRead][1]() callback. |
| arg (function) | The supplied function should have the following signature: function(data). |



### Returns

|Value | Description|
| --- | --- |
| bool | indicates whether the matching condition to satisfy the read request was fulfilled |
| num | bytes that should be removed from the front of the read buffer, regardless of whether the condition is fulfilled. You should return a value if you returned true as first return value, otherwise the entire data will be discarded.
| | The third return value is optional, and if not nil, will be used to replace the data argument of the [OnRead][2] callback handler.  This is useful if the matching process is already rather expensive (e.g. parsing an XML document), as it allows you to transfer that information directly to the OnRead() callback handler without having to do the same work again. |

[1]:	https://snap-one.github.io/docs-driverworks-api/#tcpclient-interface-onread
[2]:	https://snap-one.github.io/docs-driverworks-api/#onread