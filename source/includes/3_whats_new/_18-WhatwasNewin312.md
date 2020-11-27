
## What was New in 3.1.2

**New APIs that were Added**

### Encryption Interface

The Encryption Interface has been enhanced to include two new APIs which will generate a certificate signing request (CSR) which, when sent to a certificate authority, will return a digital identity certificate that meets the encryption criteria defined by that certificate authority. See GenerateCSR RSA and GenerateCSR ECC for more information.

PKCS12 APIs
The new Lua PKCS #12 APIs enables drivers to manage certificates and private keys using the PKCS #12 file format. These files are encrypted and protected by a password. This ensures that cryptographic assets are secure and are not easily recovered. See LoadPKCS12 and WritePKCS12.
