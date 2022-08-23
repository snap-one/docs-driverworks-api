## PersistSetValue

Persists a value associated with the specified name to the database. Note that existing values are overwritten. This API can be used before OnDriverLateInit.

###### Available from 2.10.0

### Signature

`C4:PersistSetValue(name, value, encrypted) `


| Parameter | Description |
| --- | --- |
| str | A string containing the name of the value. |
| value | The value to be persisted. The type can be any one of the following: number, string, boolean, table. |
|boolean| encrypted. Optional. A flag indicating whether the value is encrypted in the database.|


### Returns

None


### Usage Note

The value parameter type depends on the value that was set previously and can be one of the following: number, string, boolean, table.If the value parameter is a table, then the elements within the table must be one of the following types: number, string, boolean, table, nil. Tables can contain any combination of types, including nested tables. However, C4:PersistSetValue will fail if the table, or any nested table, contains any elements of the following types: lightuserdata, userdata, function, thread.


PersistSetValue uses its own thread for pushing values to the database. This thread doesn't start running until just before OnDriverLateInit. All values destined for the database are queued up so is lost. However, there is a window of time during which calling [C4:PersistGetValue][1] might not return values set previously with C4.PersistSetValue.

Persisting an empty value does not remove a value from the database. Use [C4:PersistDeleteValue][2] to remove a value.

### Example

```lua
C4:PersistSetValue("Foo", "Bar")
local Foo = C4:PersistGetValue("Foo")
print(Foo)

...

local Foo = {
    Biz = "Baz",
    Qux = "Norf
}

C4:PersistSetValue("Foo", Foo)

local Bar = C4:PersistGetValue("Foo")
print(Bar["Biz"])
print(Bar["Qux"])
```

[1]:	https://snap-one.github.io/docs-driverworks-api/#persistgetvalue
[2]:	https://snap-one.github.io/docs-driverworks-api/#persistdeletevalue