## urlSetTimeout

This function is to set a maximum time value (in seconds) for a transfer operation to take place before a server time out occurs. The value passed in this API is dependent on driver/Director performance. For example, setting this value too low could result in a timeout occurring too quickly resulting in messages missed. Setting it too high could result in lag time and poor user experience. Control4 recommends an initial setting of 20 seconds and adjusting as needed. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:urlSetTimeout(SECONDS) `	


| Parameter | Description |
| --- | --- |
| int |  number of seconds allowed |


### Returns

`None`


### Usage Notes

Starting with the release of OS 2.9.0, urlSetTimeout is optional as a driver no longer has to make this call explicitly. As of 2.9.0, Control4 imposes a 300 second overall timeout to all web requests by default.  A driver may however override this and call C4:urlSetTimeout() to revert back to the behavior described above. 

Control4 Web Service APIs, specifically those beginning with C4:url, send the following default Headers with the HTTP(s) request:

```html
Host: <DNS name or IP of server>,
Accept: "/",
Accept-Encoding: "deflate, gzip"
Connection: "close", is suggested and 
```

It is recommend that these Headers NOT be overwritten. Note that a user-agent string is not included in the default Headers. However, including one within a driver is suggested as it makes diagnostics easier for servers.


### Example

`C4:urlSetTimeout(20)`