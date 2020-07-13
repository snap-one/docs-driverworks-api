
## GetNotificationAttachmentFile

If the .jpeg file is placed on the Control4 controller by the driver, the GetNotificationAttachmentFile API should be included in your driver to return the file.


### Example

```lua
function GetNotificationAttachmentFile()
	return "image.jpg"
end
```


To assist with implementation, please see the notification driver.c4z file in the Samples folder of this SDK.