## AddVariable

Function called from a DriverWorks driver to create a Control4 variable for the driver. Note that Variables need to be added in OnDriverInit. Programming attached to variables added after OnDriverInit may not work properly on Director restart.

###### Available from 1.6.0.


### Signature

`C4:AddVariable(identifier, strValue, strVarType, [bReadOnly], [bHidden]) `


| Parameter | Description |
| --- | --- |
| identifier | A string or number that uniquely identifies the variable to be added. If a number it must be greater than zero. |
| strValue | String. If strVartype equals “BOOL” then “1” = true, “0” = false. Note, that valid values are 0 and 1 and need to be passed as strings. |
| strVarType | String. See variable types below. |
| bReadOnly | Boolean. ReadOnly: Optional, defaults to FALSE |
| bHidden | Boolean. Hidden: Optional, defaults to FALSE.  A flag indicating whether the variable is hidden. 

### Returns
| Value | Description |
| --- | --- |
| num |ID of variable that was added.|
| bool | Indicates if the variable was added successfully.|


### Usage Notes

There is no limit to the string length for a variable created using AddVariable. This can be done inside a driver programmatically or within Composer Pro.

Valid variable types are: 

- BOOL: If strVartype equals “BOOL” then “1” = true, “0” = false. Note, that valid values are 0 and 1 and need to be passed as strings.
- DEVICE: Device ID. 
- FLOAT: Sets to a floating point number.
- INT: Sets to a whole number.
- MEDIA: Supports selectable Media through ComposerPro. Note that the media data returned by the API is in XML format.
- NUMBER: Sets to a Number.
- ROOM:  Room ID for a specific room or another driver’s room variable.
- STRING: Sets to a string value.

While the following variable type can be successfully passed within the API, functionality will be supported in a future release.

- STATE
- TIME
- ULONG
- XML
- LEVEL
- LIST


### Returns

| Value | Description |
| --- | --- |
| True | Indicates that the variable was added successfully. |
| ID | ID of the variable that was added. |
| False | Indicates that the variable could not be added. Failure generally occurs when either the name or ID is not unique.


### Usage Note

If the variable ID is identified by number, then this matches the value specified in the identifier argument.


### Usage Note

Variables should always be added in the same order. Control4 Composer programming is based on VariableID’s, which are allocated in order during AddVariable calls. In other words, if you add a set of variables then later delete them and re-add different variables or in a different order, Composer programming will be incorrect.

When adding a variable by name (i.e.,identifier parameter is a string), the ID of the variable is computed. The default value of the first variable added by name is 1001, then 1002 for the second variable, and so forth. If the computed ID matches that of an existing variable, then the next available unique ID in the sequence is selected. For example, consider the following code to the right:

```lua
local result, id = C4:AddVariable(1002, "Foo", "STRING")
print(result, id)
 
result, id = C4:AddVariable("Biz", "Baz", "STRING")
print(result, id)
 
result, id = C4:AddVariable("Yaz", "Yap", "STRING")
print(result, id)

Executing this code prints the following:

true    1002
true    1001
true    1003
```


Note that when adding the third variable ("yaz"), the computed ID is 1003. This occurs because on line 1 we added a variable with ID 1002. As a result, the next available ID is 1003.

When adding a variable by number (i.e., identifier is a number), the name of the variable is computed to be a string representation of the specified ID. Note that the computed name must be unique among all existing variables. The following code illustrates this problem:


```lua
local result, id = C4:AddVariable("1001", "Foo", "STRING")
print(result, id)

result, id = C4:AddVariable(1001, "Bar", "STRING")
print(result, id)
﻿
Executing this code prints the following:
true,    1001
false
```

The second call to C4:AddVariable fails because on line 1 we added a variable with name "1001".