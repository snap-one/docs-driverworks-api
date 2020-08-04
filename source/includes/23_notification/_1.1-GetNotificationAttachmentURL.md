
## GetNotificationAttachmentURL

If the .jpeg file from the device is stored on the web or in a cloud, the GetNotificationAttachmentURL API should be included in your driver to return the URL of the file.


### Example

```lua
function GetNotificationAttachmentURL()
  return "http://10.12.80.4:80/snap1vga"
end
```


To assist with implementation, please see the notification driver.c4z file in the Samples folder of this SDK.