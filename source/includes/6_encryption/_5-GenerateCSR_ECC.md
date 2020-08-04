## GenerateCSR ECC

This API will generate a certificate signing request (CSR) which, when sent to a certificate authority, will return a digital identity certificate that meets the encryption criteria defined by Elliptic-curve cryptography (ECC) standard. The use of this API assumes a thorough knowledge of public-key cryptosystems and the ECC cryptosystem definition.

###### Available in 3.1.2.


### Signature

`C4:GenerateCSP_ECC(digest, curve, subject, tx509_exts) `


| Parameter | Description |
| --- | --- |
| digest | The algorithm used by the certificate. For example, SHA256. See the [C4:GetSupportedDigests][1]()API for information on retrieving digests. |
| curve | The elliptical curve encoding format for the certificate. |
| subject | The person, organization or device required by the certificate. For example: `"/C=US/ST=Utah/L=SLC/O=Foo/OU=Controller Certificates/CN=foo.bar.com` |
| `tx509_exts` | Optional  table of key/value pairs. Used in the event that the desired certificate contains X.509 encryption data. 


### Returns

`None`


### Examples

Generate a CSR using ECC requirements:

`local csr = C4:GenerateCSR_ECC("SHA256", "secp256k1", "/C=US/ST=Utah/L=Draper/O=Control4/OU=Controller Certificates/CN=foo.bar.com")`

The resulting CSR is generated:

```lua
 -----BEGIN CERTIFICATE REQUEST-----
MIIB0TCCAXcCAQAweDELMAkGA1UEBhMCVVMxDTALBgNVBAgMBFV0YWgxDzANBgNV
`BAcMBkRyYXBlcjERMA8GA1UECgwIQ29udHJvbDQxIDAeBgNVBAsMF0NvbnRyb2xs`
`ZXIgQ2VydGlmaWNhdGVzMRQwEgYDVQQDDAtmb28uYmFyLmNvbTCB9TCBrgYHKoZI`
zj0CATCBogIBATAsBgcqhkjOPQEBAiEA////////////////////////////////
/////v///C8wBgQBAAQBBwRBBHm+Zn753LusVaBilc6HCwcCm/zbLc4o2VnygVsW
`+BeYSDradyajxGVdpPv8DhEIqP0XtEimhVQZnEfQj/sQ1LgCIQD/////////////`
`///////+uq7c5q9IoDu/0l6M0DZBQQIBAQNCAAQXXbHNU5r5vYzZRYhPZGKFcSBe`
I+D0y0pvyw+tUo8eGO9QjHqmw6A0vm5OyRR3C9qDH8msuDO1ZgieUkCfnfYSoAAw
CgYIKoZIzj0EAwIDSAAwRQIgMvJKuHT2E+um/iXdUNhJK61jSI1ygcjR77lCZM2E
`aRkCIQCcZLJvubYxdGxB0q7ApSBujF/L6/UtL/gjuolLE6JUaw==`
  -----END CERTIFICATE REQUEST----- 
```

Generate a CSR using ECC requirements with the optional X.509 parameter:

`local csr = C4:GenerateCSR_ECC("SHA256", "secp256k1", "/C=US/ST=Utah/L=Draper/O=Control4/OU=Controller Certificates/CN=foo.bar.com", {subjectKeyIdentifier = "hash", subjectAltName = "DNS:acs.qacafe.com, DNS:www.acs.qacafe.com"})`

The resulting CSR is generated:

```lua
-----BEGIN CERTIFICATE REQUEST-----
MIICIzCCAcgCAQAweDELMAkGA1UEBhMCVVMxDTALBgNVBAgMBFV0YWgxDzANBgNV`
BAcMBkRyYXBlcjERMA8GA1UECgwIQ29udHJvbDQxIDAeBgNVBAsMF0NvbnRyb2xs
ZXIgQ2VydGlmaWNhdGVzMRQwEgYDVQQDDAtmb28uYmFyLmNvbTCB9TCBrgYHKoZI`
zj0CATCBogIBATAsBgcqhkjOPQEBAiEA////////////////////////////////
/////v///C8wBgQBAAQBBwRBBHm+Zn753LusVaBilc6HCwcCm/zbLc4o2VnygVsW
+BeYSDradyajxGVdpPv8DhEIqP0XtEimhVQZnEfQj/sQ1LgCIQD/////////////
///////+uq7c5q9IoDu/0l6M0DZBQQIBAQNCAASu8/6lwqmnPbMLCvXIIU38ZmAo
LjjaMLNhzAgAnWYz/lzg3h8FXcuC/W6jv83inkfgu/4Zutp/GxAQLBqA+lkeoFEw
TwYJKoZIhvcNAQkOMUIwQDALBgNVHQ4EBGhhc2gwMQYDVR0RBCpETlM6YWNzLnFh
Y2FmZS5jb20sIEROUzp3d3cuYWNzLnFhY2FmZS5jb20wCgYIKoZIzj0EAwIDSQAw
RgIhAI78Y9z3cIlRinJVmyx7I+7uA37HEfofzdSktra4Lm5nAiEAxTep97UadRb1
phLqvILbPqe2Lsm8JyCg/yEn5JlfncA=
 -----END CERTIFICATE REQUEST-----
```

[1]:	https://control4.github.io/docs-driverworks-api/#getsupporteddigests