## PersistGetValue

Returns the value associated with the specified name. This API can be used before OnDriverLateInit.

###### Available from 2.10.0

### Signature

`C4:PersistGetValue()`


| Parameter | Description |
| --- | --- |
| str |  A string containing the name of the value. |
| bool  | Boolean indicating whether the value is encrypted. If true, the value is decrypted before it is returned |


### Returns

| Parameter | Description |
| --- | --- |
| value |  The value associated with the specified name, or nil if no value was found. Can be : number, string, boolean, table. |


### Example

`local Foo = C4:PersistGetValue("Foo") `