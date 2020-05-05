
## Connect

This method initiates a connection request to a host and service/port. If a connection request is already in progress, this function returns nil. This API should not be invoked during OnDriverInit.

###### Available in 1.6.0


### Signature

`C4:Connect(host, service)`


| Parameters | Description |
| --- | --- |
| host | IP address or host name to connect to.  It can also be one of these special values: "!local" or "!loopback" Connect over the loopback device service is the port number or a string with the service (e.g. 80 or "http"). |
 

### Returns

This method returns a reference to itself, or nil in case of an error.