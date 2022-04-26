## PersistData

The Lua Table ‘PersistData’ is available for drivers to keep persistent data across director restarts.  Any values placed into the PersistData table will exist in the PersistData table when the driver is loaded after a director restart.

Note: we do not guarantee that binary data will be persisted correctly.  If you wish to persist binary data in the PersistData table, it is recommended that you encode it to be 7-bit safe, by using something like `C4:Base64Encode`.

##### Available from 1.6.0


### Signature

`PersistData = {}`


### Usage Note

It is recommended to use the [PersistSetValue][1] and [PersistGetValue][2] calls if they're supported in your O.S. These calls were introduced with OS 2.10.0. They immediately write to the state database.The PersistData table only is only written out when Director cycles through each driver to save its state. Because of this, latency issues can occur when using PersistData.

[1]:	https://control4.github.io/docs-driverworks-api/#persistsetvalue
[2]:	https://control4.github.io/docs-driverworks-api/#persistgetvalue