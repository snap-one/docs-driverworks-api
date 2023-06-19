## GetPrivateKeyPassword

This function allows Director to request the private key password from a driver. Implementing GetPrivateKeyPassword within a driver permits a password to be returned for a connection which requires client certificate. When implemented correctly (see Usage Notes below), this function should return the string value of the SSL Certificate password. When using a protected certificate it is highly recommend that the driver be encrypted as there is no protection from this function being called by an end user. 


###### Available from 1.6.0


### Signature

`C4:GetPrivateKeyPassword(Binding, Port)`


| Parameter | Description |
| --- | --- |
| num | Binding ID of the network connection with the password-protected certificate. |
| num | Port number for the network connection with the password-protected certificate. |


### Returns

| Value | Description |
| --- | --- |
| str | String value of the SSL Certificate password |


### Usage Notes

**SSL Connection Setup:**
An example “class” of connections that enable the declaration of an SSL connection within a driver file is defined to the right. The code example declares an SSL connection bound to port 2112.

```xml
<class>
 <classname>SSL</classname>
 <ports>
  <port>
    <number>2112</number>
    <auto_connect>true</auto_connect>
    <monitor_connection>true</monitor_connection>
    <keep_connection>true</keep_connection>
    <certificate>./cert/cert.pem</certificate>
    <private_key protected="True">./cert/key.pem</private_key>
    <cacert>./cert/cacert.pem</cacert>
    <verify_mode>peer</verify_mode>
    <method>tlsv12</method>
  </port>
 </ports>
</class>
```

In the driver’s XML definition,  the `<port></port>`section in the example has numerous parameters. Several of these are required for SSL Certificate support. Those parameters are:

`certificate` - Path to the certificate to use for the connection. The path is relative to driver’s C4Z location. In this example, a directory at the root of the .c4z file named cert has been created that contains the SSL files.

`private_key` - Path to the private key to use for the connection. The path is also relative to the driver’s C4Z location and we can see in the example that the key file resides in the cert directory.

If the client cert id password protected, (attribute of True)  then Director will call GetPrivateKeyPassword to retrieve the password from the driver. See the example to the right.

```lua
function GetPrivateKeyPassword(Binding, Port)
   return 'TheKey'
end
```


`cacert` - Path to the CA (certificate authority) certificate to use for the connection. As with the cert.pem and key.pem files, in our example cacert.pem resides in the created cert directory.

Note that It is not required to split the `<certificate>, <private_key>` and `<cacert>` elements out into separate driver files to work properly.  If the SSL cert files are maintained in individual driver files, their respective directory names must be passed in the connection XML.

`verify_mode` - Specifies the verification mode to use for the connection. The verify mode corresponds to those supported by OpenSSL. Note that Control4 currently supports only the peer verification mode `SSL_VERIFY_PEER`. Value values include:

- none
- peer

If this property is omitted, then Director defaults to use no verification (“none”).

`method` - Specifies the method to use for establishing the connection. Valid values include:

- sslv2
- sslv23
- sslv3
- tlsv1
- tlsv11
- tlsv12

If this property is omitted, then Director defaults to using sslv23 (which is the OpenSSL default).

**.c4zproj Update:**
Once the SSL connection XML is correctly configured to include the driver directory that contains your SSL cert files, it will be necessary to update your driver’s c4zproj manifest XML to include the new directory. Based on the example above, the addition of the following line is required within the `<Items></Items>`section of the manifest :

`<Item type="dir" c4zDir="cert" name="cert" recurse="true" exclude="false" />`
