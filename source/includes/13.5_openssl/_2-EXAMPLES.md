## Example

Please see the example to the right using the  Lua opensll-pkey for public or private key processing.  

Providing example of all of the OpenSSL functions is beyond the scope of the SDK.  For more examples, please visit the [lua-openssl documentation website.][1]





```xml
pkey = require 'openssl'.pkey
 
-- Generate Private/Public key pair
local private_key = pkey.new('ec', 'prime256v1', 'compressed', 'explicit') -- Generate Ecliptic Curve private key, with explicit curve parameters included
local public_key = private_key:get_public() -- Generate public key based on private key
 
local private_key_export = private_key:export('pem', 'true') -- Export text version of key (PEM format)
local public_key_export = public_key:export('pem', 'true')
 
print(private_key_export)
print(public_key_export)
 
-- Derive a shared secret from received public key and my own private key
local peer_key = pkey.read("-----BEGIN PUBLIC KEY-----\n" .. ReceivedPublicKey .. "\n-----END PUBLIC KEY-----\n")
local shared_secret = pkey.derive( private_key, peer_key )
```

[1]:	https://zhaozg.github.io/lua-openssl/modules/pkey.html