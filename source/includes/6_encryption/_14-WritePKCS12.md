## WritePKCS12

Writes a certificate and private key to a specified #PKCS12 file.

The Lua PKCS #12 interface enables drivers to manage certificates and private keys using the PKCS #12 file format. These files are encrypted and protected by a password. This ensures that cryptographic assets are secure and are not easily recovered.

###### Available in 3.1.2.


### Signature

`C4:WritePKCS12(filename, password, certificate, key, label, options)`


| Parameter | Description | 
| --- | --- |
| str | Path to the #PKCS12 file that will be created |
| str | The password for securing the file. |
| str | The PEM-encoded certificate to be stored in the file. |
| key | The PEM-encoded private key to be stored in the file. |
| str  | An optional string containing the label, or "friendly name". |


### Returns

Success returns `true`.

Failure: Returns multiple values consisting of false and string.

| Value | Description | 
| --- | --- |
| false | Indicates that the write operation failed |
| string | A description of the error that occurred. |
|


### Example

```lua
local filename = "Foo.p12"
local password = "PaSsWoRd"
local label = "This is my excellent certificate"

local certificate = [[`
     -----BEGIN CERTIFICATE-----
MIIDLTCCAhUCCQC5eca/KJpLETANBgkqhkiG9w0BAQsFADCBkTEVMBMGA1UEAwwM
Y29udHJvbDQuY29tMQ0wCwYDVQQIDARVdGFoMQswCQYDVQQGEwJVUzEdMBsGA1UE
CgwUQ29udHJvbDQgQ29ycG9yYXRpb24xFDASBgNVBAsMC0VuZ2luZWVyaW5nMScw
JQYJKoZIhvcNAQkBFhhlbmdpbmVlcmluZ0Bjb250cm9sNC5jb20wHhcNMTQwNzA3
MjEzMTA4WhcNNDExMTIyMjEzMTA4WjCBojELMAkGA1UEBhMCVVMxDTALBgNVBAgM
BFV0YWgxDzANBgNVBAcMBkRyYXBlcjEdMBsGA1UECgwUQ29udHJvbDQgQ29ycG9y
YXRpb24xFDASBgNVBAsMC0VuZ2luZWVyaW5nMRUwEwYDVQQDDAxjb250cm9sNC5j
b20xJzAlBgkqhkiG9w0BCQEWGGVuZ2luZWVyaW5nQGNvbnRyb2w0LmNvbTCBnzAN
BgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAvHAzmw+A4y9051EeycTm6vqcG+F1+lGI
17jNc85f+IL0PCswOAg5fEuRUHmj3uL3ayxxCbncUiXOyVnoTMHEvoz+sTtaUQOv
EgaYavSORv4rQcOc8UUhotujQ04ru13M00UzxkcgUTcQYpZ+IVoN6K3WOYJ9D2Ht
9BXpvb08mdUCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAmMloM/SyJoC4JwZx6o3p
NfRBmtXZNK7GaHUe49d1o68IGzwhEg9lOYC9oD6krRonN80AczSW0igN/gHxYtti
1Rf/YhYH/GW+n4p5tCOVRYhJxuqGSaycK5+t1Bs4BibYN2p7+p1PI2kpEGPCb+tp
HpM2wX1TUrI01VeB94roVAhkhNRO4xsgsgcaQPvBNFHJylbn2vmFEIwlJLB4G+sr
VNTlaC7uANjuBoFjopyQNLhxl/oPahI1k2z8ccGQjRjxKp5T/S8hKVniGr47m9eu
WSFPDl5gqSkPwHE1RGqh2i8axBaJ97Y0MhAbRmNY2sDv7kxhC+qCKn4Xm1yEi1Mn
Lw==
     -----END CERTIFICATE-----
```
