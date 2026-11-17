## DebugLog

Function called from DriverWorks driver to write a message at the DEBUG log level to the following log files on the controller:

- `/var/log/debug/director.log`
- `/var/log/debug/driver_log.log`

A message is written to a log file only when that log is set to DEBUG or a more detailed level (TRACE). By default, release builds of Control4 OS log `director.log` at ERROR and `driver_log.log` at WARN, so DebugLog messages do not appear until the log level is raised.

To raise the log level, use C4 ToolBox:

1. In Composer Pro, select **Tools** > **C4 ToolBox**. Under **Support Functions**, select **Logging**.
2. In **Logging Options**, select **Enable Debug Logs**.
3. In **Choose a Control4 Device**, select **Search Network**. If the controller isn't found, select **Add IP** and enter its IP address.
4. Select the primary controller (listed in green) and select **Enable Debug Logs**.

When testing is complete, select **Reset Logs to Default Level** in **Logging Options** and choose the same controller.

To raise only the Director log, in Composer Pro, select **Tools** > **System Diagnostics**, select the **Logging** tab, and set **Logger** to `director` and **Log Level** to `debug`. DebugLog messages then appear in `director.log`. `driver_log.log` is not one of the loggers listed in System Diagnostics. Because `director.log` fills and rotates quickly, use a controller snapshot rather than **Start Tail** to review the messages.

To retrieve the log files, download a controller snapshot: in Composer Pro, select **Tools** > **Device Logs**, then select **Download** for the primary controller. The download can take a few minutes. Log files in `/var/log/debug`, including `director.log` and `driver_log.log`, are stored in RAM and are cleared when the controller reboots, so download the snapshot before rebooting. The snapshot is a .zip file that mirrors the controller's log directories (for example, `var/log/debug/driver_log.log`) and includes the rotated, compressed copies of each log (`driver_log.log.1.gz` and so on).

This API can be invoked during OnDriverInit.

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