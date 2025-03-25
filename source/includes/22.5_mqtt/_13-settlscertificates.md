## SetTlsCertificates

The SetTlsCertificates API call allows a driver to require certificate based TLS authentication and encryption when connecting to the MQTT broker.   If the only parameter set is the cafile, then the session will be encrypted, but not necessarily authenticated.   Use of the certfile, keyfile, and possibly the password, parameters are necessary in order to have both authentication and encryption.


###### Available from 4.0.0


### Signature

`SetTlsCertificates(cafile, certfile, keyfile, password)`


| Parameters | Description                                                                                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cafile     | The file name and path to load the root CA certificate (and related chain, if needed) from.                                                              |
| certfile   | Optional. The file name and path of the "user" certificate that will be used to authenticate and encrypt this connection.                                |
| keyfile    | Optional. The private key that matches the "user" certificate that will be used to authenticate and encryption this connection.                          |
| password   | Optional. If the keyfile is encrypted, a password must be specified in order to be able to use the private key in the TLS authentication and encryption. |


### Returns

On success an error code of 0 is returned with no message return value.   On error, a value other than 0 is returned, and the message result will have some information about the error that occurred.


### Usage Note

Only one of SetTlsPsk() or SetTlsCertificate() calls should be used on an MQTT object before calling connect.   Using both will result in an undefined behavior.
