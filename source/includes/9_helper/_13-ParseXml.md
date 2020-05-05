## ParseXML

Helper function which turns a XML document into a .lua table of parsed XML data. This API can be invoked during
OnDriverInit.

###### Available from 2.7.0


### Signature

`C4:ParseXml (str)`


| Parameter | Description |
| --- | --- |
| str | XML in string format |


### Returns

| Value | Description |
| --- | --- | 
| Table | Lua Table. |


### Example

```
     function ParseProxyCommandArgs(tParams)
       local args = {}
       local parsedArgs = C4:ParseXml(tParams["ARGS"])
       for i,v in pairs(parsedArgs.ChildNodes) do
              args[v.Attributes["name"]] = v.Value
       end
       return args
      
end
```
