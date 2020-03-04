## Encode

```lua
local data = 'Hello World This Is London Calling'
local data_encoding = 'BASE64'
local encoded_data, err = C4:Encode (data, data_encoding)
print (type (encoded_data), encoded_data)
```

> Output:

```lua
string	SGVsbG8gd29ybGQ=
```

Encodes a given string with the specified data encoding.

###### Available in 1.6.0.


### Signature

`C4:Encode (data, data_encoding)`


| Parameter | Description |
| --- | --- |
| str data | Data to encode. |
| str | data\_encoding: 'NONE' / ‘HEX' / ‘BASE64' |


### Returns

`result, err`

A successful operation will return `nil` for *err*.  If an error occurs, then *result* will be nil and *err* will contain the description of the error.

| Value | Description |
| --- | --- |
| str | result: Encoded data |
| str | err: Description of any error that occurred |