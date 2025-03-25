
## What’s New in 4.0.0

### Additions to the Helper Interface

The Helper Interface has been enhanced with APIs delivered to assist with replacing older devices with newer devices or to migrate configuration settings from one device to another. These APIs include:

[GetBoundPartner][1]

[GetCapabilityById][2]

[GetProtocolDeviceById][3]


### Encryption Interface

In conjunction with the release of O.S. 4.0.0, low level AES, Blowfish, Camellia, CAST, DES, IDEA, RC2, RC4, RC5 and SEED cipher functions have been deprecated and are no long supported with the [C4:Encrypt][4] function. For more information, please see the release notes for OpenSSL 3.0: [https://openssl-library.org/news/openssl-3.0-notes/index.html][5]


### Miscellaneous Interface
The GetText API has been deprecated in conjunction with O.S. 4.0.0


### MQTT Interface

A [MQTT client API][6] for lua\_gen has been delivered in this release. MQTT is a lightweight publish and subscribe messaging protocol that is intended to connect remote devices using small amounts of code and minimal network bandwidth. Note that the Control4 hosted MQTT Server/Broker is not available to 3rd-party developers and there are no future plans to release it. This client API documentation is provided for the use of driver developers connecting to 3rd-party device(s) or service(s) that provide their own MQTT server/broker. 


### Timer Interface

The [GetTime ][7]API was enhanced with two new parameters: units and fractional. These arguments were added to give driver developers greater control over the values that are returned.


### UDP Functionality

Several Lua API's were modified in this release to provide enhanced capabilities for UDP connections. This is part of an ongoing effort to eliminate the use of LuaSocket. The following API's were modified:

[SendBroadcast][8]

[ServerSend][9]

[ReceivedFromNetwork][10]

[1]:	https://snap-one.github.io/docs-driverworks-api/#helper-interface-getboundpartner
[2]:	https://snap-one.github.io/docs-driverworks-api/#helper-interface-getcapabilitybyid
[3]:	https://snap-one.github.io/docs-driverworks-api/#helper-interface-getprotocoldevicebyid
[4]:	https://snap-one.github.io/docs-driverworks-api/#encryption-interface-encrypt
[5]:	https://openssl-library.org/news/openssl-3.0-notes/index.html
[6]:	https://snap-one.github.io/docs-driverworks-api/#mqtt-interface
[7]:	https://snap-one.github.io/docs-driverworks-api/#timer-interface-gettime
[8]:	https://snap-one.github.io/docs-driverworks-api/#serial-and-network-interface-sendbroadcast
[9]:	https://snap-one.github.io/docs-driverworks-api/#server-socket-interface-serversend
[10]:	https://snap-one.github.io/docs-driverworks-api/#serial-and-network-interface-receivedfromnetwork