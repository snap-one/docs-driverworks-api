
## What’s New in 3.4.1

**lua-openssl Interface**

This release incudes support of an extended [Lua OpenSSL interface][1].  

Historically, new cryptographic functions were added to the DriverWorks API upon request. However, this approach is untenable as it is impossible to  anticipate the future needs of drivers to perform cryptographic operations. Adding support for a more complete interface makes virtually the entire OpenSSL API available to drivers. This ensures that driver developers have what they need without having to request new APIs to be added.


[1]:	https://snap-one.github.io/docs-driverworks-api/#lua-openssl-interface