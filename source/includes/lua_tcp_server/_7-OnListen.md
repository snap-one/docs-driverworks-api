## OnListen

This method sets a callback method that will be called once the TCP server starts listening.  This callback is called once the host/service has been resolved and the endpoints has been chosen.  It is optional to implement this callback method.

###### Available in 1.6.0


### Signature

`C4:OnListen(func)`


| Parameters | Description |
| --- | --- |
| func | should have this function signature: function (server, endpoint)
| server | This C4LuaTCPServer instance
| endpoint | Table with the following fields indicating the endpoint the server is listening on: 
| | ip (string) | The IP address the server is listening on |
| | port (number) The port number the server is listening on |

`Returns`

This method returns a reference to itself.