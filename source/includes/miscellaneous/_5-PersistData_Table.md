## PersistData Table

The Lua Table ‘PersistData’ is available for drivers to keep persistent data across director restarts.  Any values placed into the PersistData table will exist in the PersistData table when the driver is loaded after a director restart.

Note: we do not guarantee that binary data will be persisted correctly.  If you wish to persist binary data in the PersistData table, it is recommended that you encode it to be 7-bit safe, by using something like C4:Base64Encode.

##### Available from 1.6.0


### Signature

`PersistData = {}`