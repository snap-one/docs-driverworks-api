## DebugLog

Function called from DriverWorks driver to send messages to the following log files: director.log and driver.log. This API can be invoked during OnDriverInit.

###### Available from 1.6.0


### Signature

`C4:DebugLog(strLogText)`


| Parameters | Description |
| --- | --- |
| str | Log text |


### Returns

`None`


### Examples

```lua
function Log:Alert(strDebugText)
   self:Print(0, strDebugText)
end

function Log:Error(strDebugText)
   self:Print(1, strDebugText)
end

function Log:Warn(strDebugText)
   self:Print(2, strDebugText)
end

function Log:Info(strDebugText)
   self:Print(3, strDebugText)
end

function Log:Trace(strDebugText)
   self:Print(4, strDebugText)
end

function Log:Debug(strDebugText)
   self:Print(5, strDebugText)
end
```