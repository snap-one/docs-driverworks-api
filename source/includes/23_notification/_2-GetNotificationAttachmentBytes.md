
## GetNotificationAttachmentBytes

If the .jpeg file is stored in the memory of the device, the GetNotificationAttachmentBytes API should be included in your driver to return the file. Note that this API has the potential to block data if the driver takes too long to execute the function. If it takes more than one second, a log entry will be created in the director log warning that the driver took too long. This is also logged in the driver debug log file. The log entry for this is: 

`“The driver: \<driver name\>(\<device id\>) took more than 1 second to get the notification extractnotifcation bytes.”` 


### Example


```lua

function GetNotificationAttachmentBytes()
  local imageData = ??? -- Get image from somewhere

    return C4:Base64Encode(imageData)
end
```

To assist with implementation, please see the notification driver.c4z file in the Samples folder of this SDK.