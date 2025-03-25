## ServerSend

This function is used to send data over an open Server Socket connection. Note the varying parameters when using TCP vs. UDP below. This API should not be invoked during OnDriverInit.

###### Available from 2.10.0
###### Enhanced in 4.0.0 with address param for UDP version.


### Signature
TCP Version:
`C4:ServerSend(nHandle, payload,)`	

| Parameter | Type | Description                                                                                                                                                       |
| --------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nHandle   | num  | The handle that identifies the client connection to use for sending the payload. This value is always sent as the first parameter to the OnServerDataIn callback. |
| payload   | str  | The data to be sent.                                                                                                                                              |

### Signature
UDP Version:
`C4:ServerSend(port, payload, address)`

| Parameter | Type | Description                                                                                                                                                                                                                                                                                                                                           |
| --------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nHandle   | num  | The port of the endpoint to which the payload is sent.                                                                                                                                                                                                                                                                                                |
| payload   | str  | A string containing the data to be sent. Note that there is risk of fragmentation for payloads that exceed the minimum guaranteed MTU size of 576 bytes. Nevertheless, fragmentation depends on many factor such as the configuration of networking gear, and the devices involved. We generally have no control over networking so plan accordingly. |
| address   | str  | The IP address of the remote endpoint to which the payload is sent.                                                                                                                                                                                                                                                                                   |


### Returns

`None`


### Example

This function shows sending data over a Server Socket:

`C4:ServerSend(nHandle, strData)`

