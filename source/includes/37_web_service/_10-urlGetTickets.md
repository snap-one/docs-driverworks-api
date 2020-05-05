## urlGetTickets

This method returns an array with the ticket ids of all ongoing transfers. This API should not be invoked during OnDriverInit.

###### Available from 2.8.1.

### Signature

`C4:urlGetTickets()`	


### Parameter

`None`


### Returns

Ticket IDs


### Usage Note

Control4 Web Service APIs, specifically those beginning with C4:url , send the following default Headers with the HTTP(s) request:

```
Host: <DNS name or IP of server>,
Accept: "/",
Accept-Encoding: "deflate, gzip"
Connection: "close", is suggested and 
```

It is recommend that these Headers NOT be overwritten. 

Note that a user-agent string is not included in the default Headers. However, including one within a driver is suggested as it makes diagnostics easier for servers.

