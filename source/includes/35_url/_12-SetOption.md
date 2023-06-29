## SetOption

Sets one option specified by name to value. Note that this method can only be called before a transfer was started. 

###### Available from 2.10.5


### Signature

`C4:SetOption(name, value)`


| Parameter | Description |
| --- | --- |
| str | String value of the name of the parameter. |
| bool | Value - Boolean value (number or string) of the parameter. |

Below is a list of valid option names and their values

`fail_on_error`
boolean:

Defaults to true.  If any response returns with an error code, the entire transfer fails with an error.  If set to false, allows the driver to e.g. read the HTTP response body of a 403 error response.

`timeout`
number:

In seconds.  Defaults to 300 or whatever value was set through C4:urlSetTimeout().  This is how many seconds, total, the entire transfer is allowed to take.

`connect_timeout`
number:

In seconds. Defaults to 5.  This is how many seconds it is allowed to take to establish the connection to the host.

`ssl_verify_host`
boolean:

Defaults to true.  Verify the host against the system's CA bundle when using the https protocol.

`ssl_verify_peer`
boolean:

Defaults to true.  Verify the peer against the system's CA bundle when using the https protocol.

`ssl_cabundle`
string:

A filename relative to the .c4z that specifies a CA bundle to use instead of the system's.  It is not recommended to use this option except for very special use cases because CA bundles require regular updates.

`ssl_cert`
ssl\_cert:

A filename relative to the .c4z that specifies a SSL client certificate to use for authentication to the host.

`ssl_cert_type`
string:

Defaults to "PEM".  The format of the SSL certificate that the file specified by the "ssl\_cert" option is in.  Valid values are: "PEM" (default), "DER", "P12".

`ssl_key`
string:

A filename relative to the .c4z that specifies the private key for the client certificate specified by the "ssl\_cert" option.

`ssl_passwd`
string:

If the private key specified by the "ssl\_key" option is encrypted, this option specifies the password.

`ssl_cacerts`
table:

A table of filenames relative to the .c4z that specify additional certificates to be added to the CA bundle used to verify the host and/or peer.  This allows e.g. extending the CA bundle to be able to verify against self-signed or company-signed certificates.


### Returns

A reference to itself.