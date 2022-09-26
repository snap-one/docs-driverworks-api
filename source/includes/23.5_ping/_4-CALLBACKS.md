
## C4Ping Callbacks
The C4Ping object provides a callback that notifies a driver about  the result of "pinging" a specified endpoint: OnResult


### OnResult
The OnResult callback is invoked to notify a driver about the result of "pinging" a specified endpoint.

### Signature

`C4:OnResult (instance, bool, str)`


| Parameter | Description |
| --- | --- |
|instance| `[C4Ping]`: The instance of the C4Ping object that has finished "pinging" a specified endpoint.|
|boolean| A boolean value indicating whether "pinging" the specified endpoint was successful. This can be one of the following values:
- false: "pinging" a specified endpoint failed. The endpoint is not reachable across the network.
- true: "pinging" a specified endpoint was successful. The endpoint is reachable. |
|string| error: A string describing the error when "pinging" the specified endpoint has failed. When successful, the value of the error argument is nil.|