## SetTlsInsecure

Use the SetTlsInsecure API to prevent checking equality of broker Common name and host connection string. Call this API before Connect.


###### Available from 4.0.0


### Signature

`SetTlsInsecure(insecure)`


| Parameters | Description                                                                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| insecure   | A boolean value. If the value is false the client will ignore the DNS and/or common name checks commonly performed during a TLS authentication. |


### Returns

On success an error code of 0 is returned with no message return value.   On error, a value other than 0 is returned, and the message result will have some information about the error that occurred.

