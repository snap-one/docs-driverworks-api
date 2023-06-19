## RegistryGetValue

Retrieves a value from the Registry.


###### Available from 2.10.4


### Signature

`C4:RegistryGetValue(key)'
`

|Parameters | Description|
| --- | --- |
| num | The key applicable to the value being retrieved. |


### Returns

Upon success, the API returns the value that was decoded from the Registry. The value can be any of the following: number, string ,boolean, table. Upon failure, the API returns nil.