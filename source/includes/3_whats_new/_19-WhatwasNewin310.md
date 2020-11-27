
## What was New in 3.1.0

**New APIs that were Added**

ToStringLocaleC - A new helper function which converts a number to a string using the ‘C’ locale regardless of the locale setting of the Control4 Operating System.


**Interfaces that were Modified**

### Zigbee Interface

Future Changes to Zigbee Server-Side Cluster Management


### Encryption Interface

A new Lua Signing API has been added to the SDK. C4:Sign enables drivers to crypto-graphically sign an arbitrary payload using a specified key. The API currently supports both HMAC & RSA signing. Control4 strongly recommends that driver developers implement this new API as soon as possible.


**New Sample Drivers that were Added**

A client side websocket driver has been added to the SDK to assist with websocket support. Sample drivers can be found in the Sample Driver folder at the root level of the SDK.zip.






