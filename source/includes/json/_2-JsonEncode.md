## Json:Encode

JSON function that takes the data in the Lua tCommand table and encodes it into a JSON formatted command string
representing a Lua object. 
On success, this function returns a single value which is as designed. On failure, the function returns two
values:

1. nil
2. A string describing the error.

This API should not be invoked during OnDriverInit.


| Parameter | Description |
| --- | --- |
| value | The Lua object to be encoded. Must be one of the following types: number, string, boolean, table. Tables can contain any combination of types (including nested tables) provided that all  items are one of the following types: number string, boolean. Note that c4:JsonEncode will fail  if any table  (or nested table) contains any of the following types: lightuserdata, userdata, function, thread. |
| formatted | Optional. A boolean flag value indicating whether the resulting JSPN string is formatted using newlines and indentations. The default value is False when omitted. |
encodeArrays | Optional. A boolean flag value indicating whether the tables are encoded as JSON arrays. The default value is False when omitted. |
| symmetric | Optional. A boolean flag value indicating whether the resulting JSON objects consist of name/value pairs in which the name must be a string (i.e, double quotes). 

Where necessary, the encoder uses the following fabricated names:

| Primitive Type | Fabricated Name |
| --- | --- |
| Number | :number: |
| String | :string: |
| Boolean | :boolean: |
| Array Index | :index: |


### Examples

```
Primitive
local Foo = "Bar"
local Result = c4:JsonEncode(Foo)
```

The preceding example yields the following JSON string: {":string:":"Bar"} This occurs because "Foo" is a primitive type (i.e., String). Unfortunately, the name of a single primitive value is unknown to the encoder so it must use a fabricated name that identifies the type. This is necessary because the JSON specification requires that all JSON objects consist of name/value pairs in which the name must be a string (i.e., double quotes).

Note that you'll need to use a Lua table in order to provide a JSON string that includes the name of the value.
Consider the following example.

```
Table
local MyTable = {
	Foo = "Bar"
}
```

`C4:JsonEncode(MyTable)`

The preceding example produces the following JSON string: {“Foo”:”Bar”} It is also possible to control whether the resulting JSON string is formatted using newlines and indentations.

```
Unformatted
local Foo = {
	Biz = "Baz",
	Qux = "Norf"
}
```

`C4:JsonEncode(Foo)`

The preceding example yields the following JSON string: {“Biz”:”Baz”,”Qux”:”Norf”}. This might be acceptable when the string is to be used in processes that don't involve humans, such as invoking  a REST service. If readability is important, however, provide the formatted (second) parameter.

```
Formatted
local Foo = {
	Biz = "Baz",
	Qux = "Norf"
}
```

`C4:JsonEncode(Foo, true)`

With this example, the resulting JSON string is formatted as:

```
{
	"Biz" : "Baz"
	"Qux" : "Norf"
} 
```

The encodeArrays (third) parameter provides control over how tables are encoded. In certain cases it might be necessary to specify that tables are encoded as JSON arrays. Note that a Lua table is considered to be an array when each key is a non-negative integer greater than zero (k \> 0). Consider the following code.

```
Object
local Foo = {
	"One",
	"Two",
	"Three",
	"Four",
}
```

`C4:JsonEncode(Foo, true)`

By default, tables are encoded using JSON objects, so the preceding example produces the following formatted 
JSON string:

```
{
	"1" : "One"
	"2" : "Two"
	"3" : "Three"
	"4" : "Four"
}
```

This encoding results for two reasons: First, the table is a Lua array. Each entry corresponds to a numeric key. Second the JSON specification requires that an object consist of name/value pairs in which each name must be a string (i.e., double quotes). As a result, each numeric key is converted to a string. This same table can also be represented as a JSON array.

```
Array
local Foo = {
	"One",
	"Two",
	"Three",
	"Four",
}
```

`C4:JsonEncode(Foo, true, true)`

With the encodeArrays (third) parameter set to true, the encoder yields the following JSON string: [ “One”,
“Two”, “Three”, “Four” ]

It is important to note that the encodeArrays parameter affects only tables that are Lua arrays. Consider the following code.

```
Non-Array
local Foo = {
	Biz = "Baz",
	Quz = "Norf"
}
```

`C4:JsonEncode(Foo, true, true)`

Although the encodeArrays parameter was set to true, the resulting JSON string is encoded as JSON object:

```
{
	"Biz" : "Baz",
	"Qux" : "Norf"

}
```

This occurs because the Lua table was not an array (i.e., contained at least one non-numeric key). Attempting to encode this table as an array would result in an invalid JSON string.

The symmetric (fourth) parameter specifies whether to use symmetric encoding. When symmetric encoding is enabled, the encoder places certain markers within the resulting JSON string. These markers make it possible to decode a JSON string back into the original (equivalent) object. Symmetric encoding (markers) is necessary due to ambiguities that arise when encoding a Lua object. Consider the following code.

```
Non-Symmetric
local Foo = {
	"One",
	{
		Two = "Two",
		Three = "Three",
	}
}
```


`C4:JsonEncode(Foo, true, false)`

While this accurately represents the Lua object as a JSON string, given the rules of Lua arrays and JSON, it cannot be decoded back into its original (equivalent) table. Rather, decoding this string will produce the following Lua table.

```
local Bar = {
	["1"] = "one",
		["2"] = {
		Two = "Two",
		Three = "Three",
	}
}
```

Note that the original numeric keys are now strings. Enable symmetric encoding corrects this problem by introducing markers into the resulting JSON string.

```
Symmetric
local Foo = {
	"One",
	{
		Two = "Two",
		Three = "Three",
    }
}
```

`C4:JsonEncode(Foo, true, false, true)`

With the symmetric parameter set to true, the encoder produces the following JSON string:

```
{
	":index:1 : "One",
	":index:2" : "Two" : {
		"Three" : "Three",
		"Two" : "Two"
	}
}
```

Note the use of the ":index:" markers. These markers specify that the first element, "One", is located at the first numeric index. Similarly, the second element, "Two", is located at the second numeric index. Decoding this JSON string produces the original Lua table. It is important to note that Lua doesn't guarantee any particular order when enumerating the elements of a table. As described in the documentation for the Lua next function. The order in which the indices are enumerated is not specified, even for numeric indices.