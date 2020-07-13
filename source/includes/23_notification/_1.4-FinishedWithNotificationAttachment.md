
## FinishedWithNotificationAttachment

This API has been included in the event that your driver needs to do any sort of clean-up with the stored .jpeg file. It also provides a notification when the original notification has been sent. This is an optional API and only recommended if cleanup is needed. For example, if it is desirable to remove a temporary image file from your system. 

### Example

```lua
function FinishedWithNotificationAttachment()
  -- do any cleanup required here.
end
```


To assist with implementation, please see the notification driver.c4z file in the Samples folder of this SDK.