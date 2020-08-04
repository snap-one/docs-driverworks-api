## ExecuteCommand

Function called by Director when a command is received for this DriverWorks driver. This includes commands created in Composer programming. This API should not be invoked during OnDriverInit. 

###### Available in 1.6.0.

### Signature

`ExecuteCommand(strCommand, tParams)`


|Parameter | Description|
| --- | --- |
|str | Command to be sent|
| table | Lua table of parameters for the sent command |


### Returns

`None`

### Usage Note

Prior to Operating System 2.10, overuse of C4:InvalidateState()was an issue as persisting extraneous data through a driver had performance implications. Beginning with Operating System 2.10, it is no longer necessary to cause driver data to be persisted. Drivers should use the PersistSetValue and PersistGetValue functions to store data that will be required across system restarts.

### Examples:

Print all commands received for this protocol driver, including all parameters:

```lua
function ExecuteCommand (strCommand, tParams)
 print("ExecuteCommand: " .. strCommand)
 if (tParams \~= nil) then
   for ParamName, ParamValue in pairs(tParams) do 
     print(ParamName, ParamValue) 
   end
 end
end
```

This sample function evaluates the commands received from Director and calls the correct function. It also looks for LUA\_ACTION commands, which are sent from Composer’s Actions tab and processes them:

```lua
function ExecuteCommand(strCommand, tParams)
print("ExecuteCommand function called with : " .. strCommand)
  if (tParams == nil) then
    if (strCommand =="GET\_PROPERTIES") then
      GET\_PROPERTIES()
    else
      print ("From ExecuteCommand Function - Unutilized command: " .. strCommand)
    end
  end
  if (strCommand == "LUA\_ACTION") then
    if tParams \~= nil then
      for cmd,cmdv in pairs(tParams) do 
        print (cmd,cmdv)
        if cmd == "ACTION" then
          if cmdv == "Reset Security System" then
            ResetSecuritySystem()
          else
            print("From ExecuteCommand Function - Undefined Action")
            print("Key: " .. cmd .. "  Value: " .. cmdv)
          end
        else
          print("From ExecuteCommand Function - Undefined Command")
          print("Key: " .. cmd .. "  Value: " .. cmdv)
        end
      end
    end
  end
end
```