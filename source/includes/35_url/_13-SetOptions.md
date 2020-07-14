## SetOptions

This API is similar to the [SetOption()][1] method, but allows the driver to pass in a table of options and their values. Note that this method can only be called before a transfer was started.

###### Available from 2.10.5


### Signature

`C4:SetOptions(options)`


| Parameter | Description |
| --- | --- |
| table | Table of options and their values:|

Below is a list of valid option names and their values


`response_headers_duplicates` 
boolean:

If set to true and duplicate response headers are received, the tHeader table will have an array of string values for this header. If set to false (default) and duplicate response headers are received, only the last header received will be saved to the tHeader table. This option defaults to false.

`cookies_enable`
 boolean:

If set to true, enables the use of cookies.  If the `cookies_use_jar` option is set to true, this causes cookies to be stored in the driver's cookie jar. If set to false (default) and a Set-Cookie header is received, the cookie will neither be stored in the driver's cookie jar, nor will it be used with any redirect request that may automatically be performed. This option defaults to false.

`cookies_use_jar` 
boolean:

If set to true (default), uses cookies in the driver's cookie jar. If set to false, this transfer does not use any cookies that may be stored in the driver's cookie jar. This option defaults to true.

`cookies_save_to_jar`
boolean:

If set to true (default), saves any new cookies to the driver's cookie jar. This may also delete expired cookies from the cookie jar.
If set to false, any cookies received from this transfer will not be saved to the jar.
This option defaults to true.

`cookies_clear_session`
boolean:

If set to true, clears any "session" cookies (cookies with no expiration time) from this transfer prior to making the request.  This does not remove them from the driver's cookie jar, but if the `cookies_save_to_jar"`option is set to true, it will remove them from the cookie jar once the transfer completes. If set to false (default), session cookies are used for this transfer. This option defaults to false.


### Returns

A reference to itself.

[1]:	https://control4.github.io/docs-driverworks-api/#setoption