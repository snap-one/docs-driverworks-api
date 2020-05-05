## RegistrySetValue

Sets the value of a Registry key/value pair. The value is updated if the specified key/value pair exists. A key/value pair is created by the API if it does not exist. 

###### Available from 2.10.4


### Signature

`C4:RegistrySetValue(key, value)`


| Parameter | Description |
| --- | --- |
| key  | `number`: The name of the key to which the specified value is associated. |
| value | The name of the key to which the specified value is associated. |


### Returns

Upon success, the API returns the value that was decoded from the Registry. The value can be any of the following: number, string ,boolean, table. Upon failure, the API returns nil.