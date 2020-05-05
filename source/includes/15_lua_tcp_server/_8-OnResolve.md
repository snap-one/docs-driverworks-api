## OnResolve
This method sets a callback method that will be called once the host/service has been resolved.  If implemented, it allows you to choose a particular endpoint to listen on, or to cancel the listen request.

###### Available in 1.6.0


### Signature

`C4: OnResolve(func)`


| Parameters | Description |
| --- | --- |
| func | should have this function signature: function (server, endpoints, choose) |
| server | This C4LuaTCPServer instance |
|endpoints | Array of tables describing all endpoints that the host/service could be resolved to. Each entry has the following: |
| | ip (string) The IP address the server is listening on |
| | port (number) The port number the server is listening on |

Note that choose is a completion function with this signature: function(index) Using this closure is optional and can be used to delay making a choice.  The index argument is of type number, and it is optional.  If not provided, default behavior is requested (first endpoint, if available).  If the index argument is provided, it should be an index into the endpoints array.  If the index argument is 0, the listen request will be canceled and the OnError callback will be called with an invalid argument error (code 22).


### Returns

This method returns a reference to itself.
