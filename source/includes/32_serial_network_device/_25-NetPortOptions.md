## NetPortOptions

Function to configure a connection's Port settings.  The use of this API is contingent upon the use of the [CreateNetworkConnection][1] and [NetConnect][2] APIs. Connections are created using the CreateNetworkConnection API and Connections are made using the NetConnect API. This API should not be invoked during OnDriverInit.

###### Available from 2.8.0

### Signature

`C4:NetPortOptions(idBinding, nPort, strIPType,tPortParams)`


| Parameter | Description |
| --- | --- |
| num | Binding ID of the network interface to disconnect from |
| num | Network port. |
| str | Network Connection type. For example, TCP/SSL or UDP. |
| table | lua table of Key/Value pairs that contain all of the parameters for the specific Port. These parameters include: |

- AUTO CONNECT - Corresponds to the `<auto_connect>` setting defined in the .c4i file. Specifies that Director should automatically attempt the connectIon.

- MONITOR CONNECTION - Corresponds to the `<monitor_connection>` setting defined in the .c4i file. Specifies that Director should monitor the connectIon by periodically polling. Director invokes the OnPoll method for a driver to inform the driver that it should poll the connectIon.

- KEEP CONNECTION - Corresponds to the `<keep_connectIon>` setting defined in the .c4i file. Specifies that Director should automatically attempt to reestablish a connectIon if it drops.

- KEEP ALIVE - Corresponds to the `<keep_alive>` setting defined in the .c4i file. Specifies that Director should enable TCP keep-alive for the connectIon.

- DELIMITER - String Delimiter to separate messages. If no delimiter is specified, packets are delivered as they are received.

- CERTIFICATE - Path to the  certificate to use for the connection. The path is relative to the driver’s .c4z location.

- PRIVATE KEY - Path to the private key to use for the connection. The path is relative to the driver’s .c4z location.

- MIRROR UDP PORT - The use of the mirror udp port parameter defaults to false. Setting this to true will use the value assigned in the nPort parameter of the  NetPortOptions function (which is the destination port) as the source port value. Meaning that the data packets will be sent from and received on port  values that are the same. Note that MIRROR UPD PORT is only available through Port Options on Dynamically created connections. Statically created connection do not support he use of MIRROR UPD PORT being set to true.

- PROTECTED - If the “protected” value is “True”, then Director will invoke the following callback to retrieve the password from the driver:

	  `function GetPrivateKeyPassword(Binding, Port)`
	 `return “TheKey”`
	  `end`

- CACERTFILE - Path to the CA (certificate authority) certificate to use for the connection. The path is relative to the driver’s C4Z location.

- VERIFY MODE - Specifies the verification mode to use for the connection. The verify mode corresponds to those supported by OpenSSL. A detailed description of the verification modes can be found here: https://www.openssl.org. Note that Control4 currently supports only the peer verification mode (SSL VERIFY PEER). Values include: none and peer. Note that if this property is omitted, then Director defaults to use no verification (“none”).

- VERIFY METHOD - Specifies the method to use for establishing the connection. A detailed description of the various methods can be found at https://www.openssl.org Valid values include: sslv2, sslv23, sslv3, tlsv1 &  tlsv1\_1\_. Note that if this property is omitted, then Director defaults to using sslv23 (which is the OpenSSL default).

- suppressconnectionevents - true or false to suppress connections. For more information see: [Suppressing System Events][3]

To the right is a sample tPortParams table using default values:

```lua
local tPortParams =  {
   AUTO_CONNECT = false,
   MONITOR_CONNECTION = true,
   KEEP_CONNECTION = true,
   KEEP_ALIVE = true,
   DELIMITER = "",
   CERTIFICATE = './client.pem',
   PRIVATE_KEY = './client_key.pem',
   MIRROR_UDP_PORT = false,
   PROTECTED = false,
   CACERTFILE = './root.pem',
   VERIFY_MODE = 'none',
   METHOD = 'tlsv1',
   SUPPRESS_CONNECTION_EVENTS = false
}
```


### Usage Note

UDP Connection: The use of the mirror udp port parameter defaults to false. Setting this to true will use the value assigned in the nPort parameter of the NetPortOptions function (which is the destination port) as the source port value. Meaning that the data packets will be sent from and received on port values that are the same.


### Returns

`None`

[1]:	https://snap-one.github.io/docs-driverworks-api/#createnetworkconnection
[2]:	https://snap-one.github.io/docs-driverworks-api/#createnetworkconnection
[3]:	https://snap-one.github.io/docs-driverworks-api/#suppressing-system-events