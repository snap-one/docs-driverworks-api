## urlClearCookies

Function to clear all cookies from a driver's cookie jar.

###### Available from 2.9.0.


### Signature

`C4:urlClearCookies() `	


### Parameters

`None`


### Returns

| Value | Description |
| --- | --- |
| num | The number of cookies that were removed. |



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