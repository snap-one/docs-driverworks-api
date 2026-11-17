## ErrorLog

Function called from DriverWorks driver to write a message at the ERROR log level to the following log files on the controller:

- `/var/log/debug/director.log`
- `/var/log/debug/driver_log.log`

The default log levels on release builds of Control4 OS capture ERROR messages, so ErrorLog messages appear in both files without changing any log level.

To retrieve the log files, download a controller snapshot: in Composer Pro, select **Tools** > **Device Logs**, then select **Download** for the primary controller. The download can take a few minutes. Log files in `/var/log/debug`, including `director.log` and `driver_log.log`, are stored in RAM and are cleared when the controller reboots, so download the snapshot before rebooting. The snapshot is a .zip file that mirrors the controller's log directories (for example, `var/log/debug/driver_log.log`) and includes the rotated, compressed copies of each log (`driver_log.log.1.gz` and so on).

###### Available from 1.6.0


### Signature

`C4:ErrorLog(strLogText)`


### Example

Here is an example  using a variable called "lightLevel" to send an error log when a light level exceeds the value of 100:

```lua
if (lightLevel > 100) then
   C4:ErrorLog("ERROR: light level out of range")
end
```
