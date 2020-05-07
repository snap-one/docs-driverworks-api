## Decode

```lua
local data = 'SGVsbG8gd29ybGQ='
local data_encoding = 'BASE64'
local decoded_data, err = C4:Decode (data, data_encoding)
print (type (decoded_data), decoded_data)
```

> Output:

```lua
string	Hello World
```

Decodes a given string that was previously encoded with the specified data encoding.

###### Available in 1.6.0.


### Signature

`C4:Decode (data, data_encoding)`


| Parameter| Description |
| --- | --- |
| str | Data to decode |
| str | data\_encoding:  `string`: 'NONE' / 'HEX' / 'BASE64’ |



### Returns

`result, err`

A successful operation will return `nil` for *err*.  If an error occurs, then *result* will be nil and *err* will contain the description of the error.

| Value | Description |
| --- | --- | 
| str | result: Decoded data |
| str | err: Description of any error that occurred |