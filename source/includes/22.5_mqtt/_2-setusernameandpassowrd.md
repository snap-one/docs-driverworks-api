## SetUsernameAndPassword

The SetUsernameAndPassword API call is used to configure the user name and password that will be used to connect to the MQTT broker. This call must be called prior to calling the [Connect][1] API, or the attempt to connect to the MQTT broker will not use a user name or password.


###### Available from 4.0.0


### Signature

`SetUsernameAndPassword(username, password)`


| Parameters | Description                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------- |
| username   | The user name that should be used to authenticate to the MQTT broker.  By default, no user name is defined.         |
| password   | Optional. The password that should be used to authenticate to the MQTT broker.  By default, no password is defined. |

### Returns

0 on success.  On error, two values are returned.  The first value is a number indicating the error, the second is a string that describes the error.

[1]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface-connect