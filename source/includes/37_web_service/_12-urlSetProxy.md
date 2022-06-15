## urlSetProxy

This function is to set server related security information that may be needed in future related url calls. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:urlSetProxy ()`


| Parameter | Description |
| --- | --- |
| str | url to be used for supplied credentials bool |
| num | port corresponding to the url |
| str |  username to be used for the url |
| str |  password to be used for the urlfailOnHttpError (boolean) - True/False. Defaults to True. |


### Returns

`None`


## Usage Note

Control4 Web Service APIs, specifically those beginning with [C4:url][1], send the following default Headers with the HTTP(s) request:

```html
Host: <DNS name or IP of server>,
Accept: "/",
Accept-Encoding: "deflate, gzip"
Connection: "close", is suggested and
```

It is recommend that these Headers NOT be overwritten. Note that a user-agent string is not included in the default Headers. However, including one within a driver is suggested as it makes diagnostics easier for servers.


### Examples

`C4:urlSetProxy("www.mywebsite.com", 8080, "me", "mypassword")`


[1]:	https://snap-one.github.io/docs-driverworks-api/#url-interface