## Working with Files


The lua-openssl library was modified such that all file operations (i.e., create, open, etc.) occur relative to a well-known directory alias. The DriverWorks API provides the following directory aliases to drivers:


C4Z: Points to a driver's "c4z" directory. This directory consists of the name of the driver file without the .c4z extension. For example, given a driver filename of my\_test\_driver.c4z, using this alias resolves to the following directory:
…/drivers/c4z/my\_test\_driver/


LOGGING: Points to the system logging directory. Using this alias resolves to the following directory:
/var/log/debug/


MEDIA: Points to the system media directory. Using this alias resolves to the following directory:
/media/

SANDBOX: Points to a driver's "sandbox" directory. This directory consists of the Device ID. For example, given a driver with a Device ID of 42, using this alias resolves to the following directory:
.../lua/sandbox/42/

A driver can use any of these aliases by prefixing the filename using the following syntax:
\<ALIAS\>:/\<filename\>

Note that using an alias is optional; the SANDBOX alias is used by default when no alias is given.

**The following characters are disallowed in directory/file names:**

- Non-printable characters (ASCII values \< 32 / 0x20)
- Angle brackets: \<. \>
- Asterisk: \* 
-  Backslash: \\
- Colon: :
- Double quote: "
- Pipe: |
- Question mark: ?
- Tilde: `~`

See the examples of using Aliases to the right.  

```xml
-- Creating a file in the "sandbox". Note the the following two examples are equivalent (SANDBOX is used by default when no alias is given):

local openssl = require 'openssl'
 
local file, error_message, error_code = openssl.bio.file("cert.pem", "w+b")
if (file == nil) then
    error_message = "Error creating cert.pem: " .. error_message
end


local openssl = require 'openssl'
 
local file, error_message, error_code = openssl.bio.file("SANDBOX:/cert.pem", "w+b")
if (file == nil) then
    error_message = "Error creating cert.pem: " .. error_message
end
```


```xml
-- Opening a file in the "sandbox":


local openssl = require 'openssl'
 
local file, error_message, error_code = openssl.bio.file("SANDBOX:/cert.pem", "r")
if (file == nil) then
    error_message = "Error opening cert.pem: " .. error_message
end
```


```xml
-- Opening a file in the "c4z" directory:


local openssl = require 'openssl'
 
local file, error_message, error_code = openssl.bio.file("C4Z:/image.jpg", "r")
if (file == nil) then
    error_message = "Error opening image.jpg: " .. error_message
end
```
