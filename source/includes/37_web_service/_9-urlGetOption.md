## urlGetOption

Function to retrieve cookies from the driver's cookie jar filtered by a specific domain.

###### Available from 2.9.0.

### Signature

`C4:urlGetOption (option)`	


| Parameter | Description |
| --- | --- |
| num | Returns the number of concurrent transfers allowed per hostbool |
| bool | Returns whether HTTP pipelining is enabled. |


### Returns

Value of the option parameter passed


### Usage Note

Control4 Web Service APIs, specifically those beginning with [C4:url][1], send the following default Headers with the HTTP(s) request:

```html
Host: <DNS name or IP of server>,
Accept: "/",
Accept-Encoding: "deflate, gzip"
Connection: "close"
```

It is recommend that these Headers NOT be overwritten. 

Note that a user-agent string is not included in the default Headers. However, including one within a driver is suggested as it makes diagnostics easier for servers.

[1]:	https://control4.github.io/docs-driverworks-api/#url-interface