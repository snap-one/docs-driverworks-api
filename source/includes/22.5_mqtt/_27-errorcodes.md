## Error Codes and their Meanings

Error codes are values that are returned from the individual API calls. In the MQTT Lua APIs they are denoted by assigning the result of an API call to the 'errorCode' variable. The integer value that is returned as the error code can be provided to the [ErrorCodeToString][1] API call in order to convert it from a numeric code in to a descriptive string. The numeric codes and descriptive strings are defined below:


| Error Code | Description                                                                 |
| ---------- | --------------------------------------------------------------------------- |
| -4         | Continue with authentication.                                               |
| -3         | No subscribers.                                                             |
| -2         | Subscription already exists.                                                |
| -1         | Connection pending.                                                         |
| 0          | No error.                                                                   |
| 1          | Out of memory.                                                              |
| 2          | A network protocol error occurred when communicating with the broker.       |
| 3          | Invalid function arguments provided.                                        |
| 4          | The client is not currently connected.                                      |
| 5          | The connection was refused.                                                 |
| 6          | Message not found (internal error).                                         |
| 7          | The connection was lost.                                                    |
| 8          | A TLS error occurred.                                                       |
| 9          | Payload too large.                                                          |
| 10         | This feature is not supported.                                              |
| 11         | Authorisation failed.                                                       |
| 12         | Access denied by ACL.                                                       |
| 13         | Unknown error.                                                              |
| 14         | System error. This value won't be translated properly by ErrorCodeToString. |
| 15         | Lookup error.                                                               |
| 16         | Proxy error.                                                                |
| 18         | Malformed UTF-8                                                             |
| 22         | Duplicate property in property list.                                        |
| 23         | TLS handshake failed.                                                       |
| 24         | Requested QoS not supported on server.                                      |
| 25         | Packet larger than supported by the server.                                 |
| 26         | OCSP error.                                                                 |

[1]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-errorcodetostring