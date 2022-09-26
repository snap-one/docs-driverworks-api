## SetOnResult

SetOnResult
Sets the callback that is invoked to notify a driver about the result of "pinging" a specified endpoint.

### Signature

`C4:SetOnResult (callback)`


| Parameter | Description |
| --- | --- |
| str | Endpoint. The endpoint to ping.|
| int | Rounds. The number of times to "ping" the specified endpoint when there is no response. |


### Parameters

Callback: A callback function to be invoked to notify a driver about the result of "pinging" a specified endpoint.


### Returns

The SetOnResult method returns a single result:
- The instance of the C4Ping object on which SetOnResult was invoked.