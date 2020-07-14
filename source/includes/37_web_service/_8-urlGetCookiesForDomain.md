## urlGetCookiesForDomain

Function to retrieve cookies from the driver's cookie jar filtered by a specific domain.

###### Available from 2.9.0.


### Signature

`C4:urlGetCookiesForDomain (domain)`	


| Parameter | Description |
| --- | --- |
| str | Optional. A specific domain. |


### Returns

| Value | Description |
| --- | --- |
| table |Table of a map of domain names to a map of cookie names to cookie table objects. |


### Usage Note

Each cookie table has the following fields defined:

-  domain (str): The domain that this cookie belongs to
- path (str): The path that this cookie belongs to
- name (str): The name of this cookie
- value (str): The value of this cookie
- secure (boolean): If set to true, this cookie is only used for https requests
- wildcard (boolean): If set to true, this cookie is used for any subdomains
- expires (number): Expiration date/time in number of seconds since the Epoch.  If this value is 0, this is  session cookie.


### Usage Note

Control4 Web Service APIs, specifically those beginning with [C4:url][1], send the following default Headers with the HTTP(s) request:

```html
Host: <DNS name or IP of server>,
Accept: "/",
Accept-Encoding: "deflate, gzip"
Connection: "close", is suggested and 
```

It is recommend that these Headers NOT be overwritten. 

Note that a user-agent string is not included in the default Headers. However, including one within a driver is suggested as it makes diagnostics easier for servers.


### Example

```lua
for name,cookie in pairs(C4:urlGetCookiesForDomain("example.com")) do
    print("cookie[" .. cookie.domain .. "][" .. name .. "]: path: " .. cookie.path .. " value: " .. cookie.value)
end

```



[1]:	https://control4.github.io/docs-driverworks-api/#url-interface