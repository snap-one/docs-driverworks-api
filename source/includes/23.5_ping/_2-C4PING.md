## C4Ping

The C4Ping object enables a Lua driver to "ping" a specified endpoint, generally to determine whether the endpoint is reachable across the network. This is accomplished by sending an ICMP "Echo" packet to the specified endpoint and awaiting a response. The C4Ping object provides the following methods: Ping and SetOnReset

### Ping

The Ping method "pings" a specified endpoint by sending one, or more, ICMP "Echo" packets to the endpoint. There is one method that sets a callback function that enables a driver to receive the result of "pinging" a specified endpoint: SetOnresult. SetOnResult sets a callback that is invoked to notify a driver about the result of "pinging" a specified endpoint.

A driver can specify the number of rounds, or attempts, to "ping" a specified endpoint. The C4Ping object will "ping" an endpoint until it reaches the specified number of rounds. Each round is spaced 5 seconds apart. If the C4Ping object fails to receive a response after reaching the specified number of rounds, it invokes the OnResult callback to notify the caller about the failure.


### Signature

`C4:Ping (str, int)`


| Parameter | Description |
| --- | --- |
| str | Endpoint. The endpoint to ping.|
| int | Rounds. The number of times to "ping" the specified endpoint when there is no response. |


### Returns
The Ping method may return multiple values. 
On success, Ping returns the following: 
- The instance of the C4Ping object on which Ping was invoked.

On failure, Ping returns the following:
- nil
- A string describing the failure.
