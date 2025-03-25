## Valid MQTTv5 properties

MQTTv5 provides properties that can be used to provide meta-data, or fine tune a connection.   There are a number of properties that can be used with different API calls.   However, the ones listed here are ones that we feel driver developers may wish to use.   For a full listing of properties and their usage, please see the MQTT standard at [https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html][1].   Section 2.2.2 will provide a full list of properties known to MQTTv5.

**NOTE:** Properties not listed here can still be used in the appropriate situations.  This list is filtered to remove properties that aren't commonly used.

```lua
-- Creating an MQTTv5 properties table.
-- The property name is always identified by a string.   The type for the value is defined in the tables below or in the MQTT standard.

local myv5props = { CONTENT_TYPE = "application/json", PAYLOAD_FORMAT_INDICATOR = 0 }

```

### Properties that expect an integer

The MQTT standard allows for numeric values that are 1, 2 or 4 byte values.   The MQTT client for Lua will handle making sure that the correct number of bytes are provided for the value, but the lengths are provided so that you can understand the range of valid values involved.

| Property Name                     | Byte(s) | Usable With                             | Brief Description                                                                                                                                                                                       |
| --------------------------------- | ------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PAYLOAD\\\_FORMAT\\\_INDICATOR    | 1       | Publish, Will                           | 0 indicates the payload is unspecified bytes.  1 indicates it is a UTF-8 encoded string.                                                                                                                |
| REQUEST\\\_PROBLEM\\\_INFORMATION | 1       | Connect, OnConnect callback             | 0 indicates that no problem information should be provided on failure.  1 indicates that problem information shopuld be provided.                                                                       |
| RETAIN\\\_AVAILABLE               | 1       | OnConnect callback                      | 0 indicates that retained messages are not allowed with this broker.  1 indicates that retained messages may be used.  If this property is not available, the broker allows retained messages.          |
| WILDCARD\\\_SUB\\\_AVAILABLE      | 1       | OnConnect callback                      | 0 indicates that wildcard subscriptions are not allowed.  1 indicates that wild card subscriptions are allowed.  If not present, wild card subscriptions are allowed.                                   |
| SUBSCRIPTION\\\_ID\\\_AVAILABLE   | 1       | OnConnect callback                      | 0 indicates that subscription identifiers are not allowed by the broker.  1 indicates that subscription identifiers are allowed.  If this property is not present subscription identifiers are allowed. |
| SHARED\\\_SUB\\\_AVAILABLE        | 1       | OnConnect callback                      | 0 indicates that shared subscriptions are not allowed.  1 indicates that shared subscriptions are allowed.  If this property is not present, subscription identifiers are supported.                    |
| MESSAGE\\\_EXPIRY\\\_INTERVAL     | 4       | Publish, Will                           | The length of time, in seconds, that this message is valid for.                                                                                                                                         |
| SESSION\\\_EXPIRY\\\_INTERVAL     | 4       | Connect, Disconnect, OnConnect callback | The number of seconds that should be used for the session expiry interval.  In general, you should not need to set this.                                                                                |
| MAXIMUM\\\_PACKET\\\_SIZE         | 4       | Connect, OnConnect callback             | The maximum size, in bytes, that a single MQTT packet can be.  If no value is provided, the MQTT broker defaults will be used.                                                                          |


### Properties that expect a string

| Property Name       | Usable With                                                                                      | Brief Description                                                                                                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONTENT\\\_TYPE     | Publish, Will                                                                                    | A string that describes the content of the message being published.  It is recommended to use standard HTTP content types, but this value is not checked by the broker.                     |
| RESPONSE\\\_TOPIC   | Publish, Will                                                                                    | A string that indicates the topic that a client should respond to a request on.  This is used with `CORRELATION_DATA` to allow a request-response style of communication over the MQTT bus. |
| CORRELATION\\\_DATA | Publish, Will                                                                                    | Binary data used by the sender of a request message to allow it to determine which response sent on the `RESPONSE_TOPIC` is intended for it.                                                |
| SERVER\\\_REFERENCE | OnDisconnect callback, OnConnect callback                                                        | When a reason code is returned that indicates a different server should be used, this string will contain the information about the new server that should be connected to.                 |
| REASON\\\_STRING    | Disconnect, OnConnect callback, OnPublish callback, OnSubscribe callback, OnUnsubscribe callback | A UTF-8 encoded string providing the reason that a callback was called, or the reason that the client wants to provide when disconnecting.                                                  |


### Properties that expect a table

```lua
-- The MQTTv5 USER_PROPERTY is its own lua table, embedded in a lua table.  Both the key and value need to be defined as strings.

local myv5props = { CONTENT_TYPE = "application/json", USER_PROPERTY = { "key" = "value" } }

```

| Property Name    | Usable With                                                                                                                                      | Brief Description                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| USER\\\_PROPERTY | Connect, Publish, Will, Subscribe, Unsubscribe, Disconnect, OnConnect callback, OnPublish callback, OnSubscribe callback, OnUnsubscribe callback | A key=value pair should be provided to define the user property that should be used. |

### Usage Notes

There are restrictions on which properties can be used with, or returned from, certain calls.   When invalid properties are provided, no error indication is returned, they are simply ignored by the MQTT broker.

It is recommended that you refer to the MQTT standard at [https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html][2] do understand the intention for each property, when it should be used, and how it should be used.  See section 2.2.2, along with the individual calls that they are allowed to be used with for details.

[1]:	https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
[2]:	https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html