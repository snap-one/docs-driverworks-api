## LoadPKCS12

Load a certificate and private key from a #PKCS12 file.

The Lua PKCS #12 interface enables drivers to manage certificates and private keys using the PKCS #12 file format. These files are encrypted and protected by a password. This ensures that cryptographic assets are secure and are not easily recovered.

###### Available in 3.1.2.


### Signature

`C4:LoadPKCS12(filename, password) `


| Parameter | Description | 
| --- | --- |
| str | Path to the #PKCS12 file to load |
| str | The password for unlocking the file. |


### Returns

Success returns multiple values consisting of: true, string, string.

| Value | Description | 
| --- | --- |
| true | Indicates that the load operation was successful. |
| string | The PEM-encoded certificate. |
| string | The PEM-encoded private key. |

Failure returns multiple values consisting of: false, string

|Value | Description |
| --- | --- |
| false | Indicates that the load operation failed |
| str | A description of the error that occurred |


### Example

	local filename = "Foo.p12"
	local password = "PaSsWoRd"
	
	result, cert, key = C4:LoadPKCS12(filename, password)
	   if (result) then
	   print("Success!")
	 else
	   print("Something horrible has happened: ", cert)
	end
