## SetTlsPsk

The SetTlsPsk API call allows a driver to use a pre-shared key (PSK) to establish an authenticated and encrypted session with the MQTT broker. This call must be called before the [Connect][1] API call in order for TLS to be used. When a PSK is set the attempt to connect to a remote MQTT broker will fail if it doesn't support TLS, and isn't using the same PSK.


###### Available from 4.0.0


### Signature

`SetTlsPsk(psk, identity, ciphers)`


| Parameters | Description                                                                                                                                                                                                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| psk        | A string containing a representation of the hex value that should be used to authenticate and encrypt the session with TLS. The format of the PSK is a string that represents hex. For example, a valid PSK may be "0102ABCD0405". If an invalid PSK is provided, an error will be returned. |
| identity   | The identity that should be used to authenticate and encrypt the session with TLS.                                                                                                                                                                                                           |
| ciphers    | Optional. A list of ciphers that are allowed to be used with the TLS authentication and encryption.                                                                                                                                                                                          |


### Returns

On success an error code of 0 is returned with no message return value.   On error, a value other than 0 is returned, and the message result will have some information about the error that occurred.


### Usage Note

Only one of SetTlsPsk() or SetTlsCertificate() calls should be used on an MQTT object before calling connect. Using both will result in an undefined behavior.

[1]:	https://snap-one.github.io/docs-driverworks-api-4.0.0-beta/#mqtt-lua-apis-connect