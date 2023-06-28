
## What’s New in 3.3.1

**Encryption Interface**

The [GenerateCSR ECC][1] and [GenerateCSR RSA][2] APIs have been modified. Upon success, they now return strings containing the CSR/ECC, public key and private key. Upon failure, nil is returned.


** Helper Interface**

As part of Control4’s plan to tighten driver security, the io.popen() call is in the process of being removed. The following APIs have been added in support of this effort: 

- [GetHostname][3]
- [PortInUse][4]


**Ping Interface**

The Lua DriverWorks API has been expanded with the addition of the new [C4Ping][5] API. This new API enables drivers to ping a specified endpoint to determine whether it is reachable across the network.


**Server Socket Interface**

The Lua C4:[CreateTLSServer][6] API and [CreateServer][7] API have been modified to accommodate the addition of an identifier that is associated with an instance of a server. This identifier enables a Lua driver to determine which instance of a server is active.


** URL Interface**

As part of Control4’s plan to tighten driver security, the io.popen() call is in the process of being removed. The following APIs have been added or modified in support of this effort: 

- [DownloadFile][8]
- [GetUname][9]
- [GetUptime][10]

[1]:	https://snap-one.github.io/docs-driverworks-api/#encryption-interface-generatecsr_eccc
[2]:	https://snap-one.github.io/docs-driverworks-api/#encryption-interface-generatecsr_rsa
[3]:	https://snap-one.github.io/docs-driverworks-api/#helper-interface-gethostname
[4]:	https://snap-one.github.io/docs-driverworks-api/#helper-interface-portinuse
[5]:	https://snap-one.github.io/docs-driverworks-api/#ping-interface
[6]:	https://snap-one.github.io/docs-driverworks-api/#server-socket-interface-createtlsserver
[7]:	https://snap-one.github.io/docs-driverworks-api/#server-socket-interface-createserver
[8]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-downloadfile
[9]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-getuname
[10]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-getuptime