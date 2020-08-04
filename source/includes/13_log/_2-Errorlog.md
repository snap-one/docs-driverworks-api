## ErrorLog

Function called from DriverWorks driver to send messages to the following log files: director.log and driver.log.

###### Available from 1.6.0


### Signature

`C4:ErrorLog(strLogText)`


### Example

Here is an example  using a variable called "lightLevel" to send an error log when a light level exceeds the value of 100:

```lua
If (lightLevel > 100) then
   C4:ErrorLog(“ERROR: light level out of range”)
end
```
