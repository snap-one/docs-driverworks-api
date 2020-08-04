## GenerateCSR RSA

This API will generate a certificate signing request (CSR) which, when sent to a certificate authority, will return a digital identity certificate that meets the encryption criteria defined by the Rivest–Shamir–Adleman (RSA) standard. The use of this API assumes a thorough knowledge of public-key cryptosystems and the RSA cryptosystem definition.


###### Available in 3.1.2.


### Signature

`C4:GenerateCSP_RSA(digest, sizeCert, subject, tx509_exts)`


| Parameter | Description |
| --- | --- |
| digest | The algorithm used by the certificate. For example, SHA256. 
| | See the [C4:GetSupportedDigests()][1]API for information on retrieving digests. |
| sizeCert | The Key size of the certificate. For example, 2048. |
| subject | The person, organization or device required by the certificate. |
| `tx509_exts` | Optional  table of key/value pairs. Used in the event that the desired certificate contains X.509 encryption data. 


### Returns

`None`

### Examples

Generate a CSR using RSA requirements:

`local csr = C4:GenerateCSR_RSA("SHA256", 2048, "/C=US/ST=Utah/L=Draper/O=Control4/OU=Controller Certificates/CN=foo.bar.com")`

The resulting CSR is generated:

	BEGIN CERTIFICATE REQUEST-----
	MIICvTCCAaUCAQAweDELMAkGA1UEBhMCVVMxDTALBgNVBAgMBFV0YWgxDzANBgNV
	BAcMBkRyYXBlcjERMA8GA1UECgwIQ29udHJvbDQxIDAeBgNVBAsMF0NvbnRyb2xs
	ZXIgQ2VydGlmaWNhdGVzMRQwEgYDVQQDDAtmb28uYmFyLmNvbTCCASIwDQYJKoZI
	hvcNAQEBBQADggEPADCCAQoCggEBALzSLHvRT8QcVbfFlxCCUkGEL2irn8r6DxBM
	+XEK6/xXeAVZ/oWRAiGOHBNeqmdaUz0ib4ANdTHn8jEUB2t38cDVEJ88o4BiE+/D
	rpmUphIKXh3Hp57PwyC0EKHQ2POq6e75AxOMouCdtbbLgBDxmD6WWM6ojEwphEQ2
	M6JM6ZJA9pDQ/UanbGWruvKFEm9AUdo+hAjoFgObDqhWLLIwXFeSyz6y/0aymBam
	jtO/ovOS/5moNy+ENBeOsLC2ayCn4Fquj77Y825Ye9kYPkiVkkcEtawAEEFebZJY
	pUE8SwBOYjjHYJoWFDv+vcxWBFlc0ECTFKeB9Bd4vi2TF+IlwpsCAwEAAaAAMA0G
	CSqGSIb3DQEBCwUAA4IBAQBv4Z7e1cD1gbNy0PXYyugQpbG19umTcZkQN+BlK5TY
	+VcNLKK/56IPaxX7ZeHpe3DQPOXnTmc/+wVremZ6h7TwSxUOBFY9DjVUuh0thWsB
	t+xUzWt4Oae0ymP8JF83b9RZl1EGGsAsQopB+Uu4P9VgwjHm9PTXVBheofbZ/yXp
	oeom+w0fl+/qCcIjvDAGh8ODz4gfk6Mjl1iiQykOyWeGhZiGyd6G80IAF1pjciVS
	O94cvy6o9EAAgujSCmCZFOgx3kwOfLZ/r1rq5jRvyyjK7wzL7bZHHjBJBLpe/tx0
	AV+GeKVQe0nHme1tt1n+ZC5mIZ0q7qjKL3wwl4ckwTg/
	      -----END CERTIFICATE REQUEST——

Generate a CSR using RSA requirements with the optional X.509 parameter:

`local csr = C4:GenerateCSR_RSA("SHA256", 1024, "/C=US/ST=Utah/L=Draper/O=Control4/OU=Controller Certificates/CN=foo.bar.com", {subjectKeyIdentifier = "hash", subjectAltName = "DNS:acs.qacafe.com, DNS:www.acs.qacafe.com"})`

The resulting CSR is generated:

	 -----BEGIN CERTIFICATE REQUEST-----
	MIICCTCCAXICAQAweDELMAkGA1UEBhMCVVMxDTALBgNVBAgMBFV0YWgxDzANBgNV
	BZXIgQ2VydGlmaWNhdGVzMRQwEgYDVQQDDAtmb28uYmFyLmNvbTCBnzANBgkqhkiG
	9w0BAQEFAAOBjQAwgYkCgYEA3djqm4PIBftyev9W0W4U+2XlwKHepq2o+dWPSk5s
	/UzNd0TCeYoM02r+sTzQN2lkiGMYoPoKvP6qvQFWBzprtkS40z11S8AYGLqwKvxy
	/MC8YcWjgGgvZB0h51TdW1OFdFT+yL68jnO9rGGIlfHx5DMyYypZf3tJKLczLVrh
	rY0CAwEAAaBRME8GCSqGSIb3DQEJDjFCMEAwCwYDVR0OBARoYXNoMDEGA1UdEQQq
	RE5TOmFjcy5xYWNhZmUuY29tLCBETlM6d3d3LmFjcy5xYWNhZmUuY29tMA0GCSqG
	SIb3DQEBCwUAA4GBAA8Rz0fl6ue23HBENNV151uF0mQ9aT6/Z5S+8w8XTXXmf76B
	OtTWXwPsxfsfxtZgRyKIGS4evUFN9jQIyEJNDj1+gvN2YFcm7bZFnPgq1m2vA3R1
	TI9W6D463RicdNwjO92RYUgSm58Q1tCpyvlQqnedzvihQw1JFRgcIGNhbqI5
	 -----END CERTIFICATE REQUEST-----

[1]:	https://control4.github.io/docs-driverworks-api/#getsupporteddigests