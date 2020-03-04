## ReceivedFromProxy

Function called by Director when a proxy bound to the specified binding sends a BindMessage to the DriverWorks driver. This API should not be invoked during OnDriverInit.

###### Added in OS 1.6.0


### Signature

`ReceivedFromProxy(idBinding, strCommand, tParams)`


| Parameter | Description |
| --- | --- |
| num | Binding ID of the proxy that sent a BindMessage to the DriverWorks driver. |
| str | Command that was sent |
| table | Lua table of received command parameters |


### Returns

`None`


### Examples

```
function ReceivedFromProxy(idBinding, strCommand, tParams)
 print("ReceivedFromProxy [" .. idBinding .. "]: " .. strCommand)
 if (tParams ~= nil) then
      for ParamName, ParamValue in pairs(tParams) do
           print(ParamName, ParamValue)
      end
 end
end
```

Map the idBinding to a variable for proxy; evaluate the command coming in – if its a simple command, get the command equivalent out of the CMDS table, otherwise call a function to process the command. 

```
function ReceivedFromProxy(idBinding, strCommand, tParams)
   proxy = "Undefined"
   if idBinding == 5001 then
      proxy = "Receiver"
   elseif idBinding == 5002 then
      proxy = "Tuner"
   end
   print("ReceivedFromProxy [" .. idBinding .. "]: " .. strCommand .. " for " .. proxy)
   cmd = CMDS[strCommand] 
   if (cmd ~= nill) then
     print(  "Received from Proxy: " .. strCommand .. "; Send to Device: " .. cmd)
     emit(cmd)
   else
     CommandInterpreter(strCommand, tParams)
  end
end
```



