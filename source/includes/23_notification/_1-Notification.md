
## Notification Interface


Beginning with OS 3, device drivers have the ability to include .jpeg files within notifications. These images are displayed as part of the notification. The .jpeg file can be retrieved from a cloud service that supports the device, from the device itself or from a location on a Control4 Controller. 

Leveraging this functionality in a driver requires the following:

1. Configuration: New Driver XML implementation to support attachment notifications and attachment source locations
2. Execution: New API implementation for each source location needed.

### Configuration

Required Driver XML: In order for a driver to support attachments within the notifications sent by the Notification Agent, the following XML element must be included and set to True:

`<notification_attachment_provider>True</notification_attachment_provider>`

Once set to True, the Notification Agent in ComposerPro now includes a new attachment field.

There are three types of .jpeg attachments that can be included in the Push Notification: Memory, File or Snapshot (URL). Note that any combination of the three may be implemented in the driver XML. This is largely dependent upon the device's capabilities. When the following XML is added to the driver these options are available through the Add button:

```xml
<notification_attachments>
              <attachment>
                    <id>1001</id>
                    <type>IMAGE_JPEG</type>
                    <description>Current Snapshot</description>
                    <source>MEMORY</source>
              </attachment>
              <attachment>
                    <id>1002</id>
                    <type>IMAGE_JPEG</type>
                    <description>Snapshot (FILE)</description>
                    <source>FILE</source>
              </attachment>
              <attachment>
                     <id>1003</id>
                     <type>IMAGE_JPEG</type>
                     <description>Snapshot (URL)</description>
              </attachment>
 </notification_attachments>
```


After clicking the Add button and opening the driver, which is a security camera in this example, we can see the three image types. When the correct type for the device the driver supports is selected, the attachment field is populated. 


### Execution

The following APIs have been delivered in OS 3 to support the return of the .jpeg files. Each API has been engineered to deliver the file based on the location of where the file is stored. They are called when the Notification is triggered. Currently, there are three options for file storage: URL, File or Memory

URL
If the .jpeg file from the device is stored on the web or in a cloud, the GetNotificationAttachmentURL API should be included in your driver to return the URL of the file.

```
function GetNotificationAttachmentURL()
	return "http://10.12.80.4:80/snap1vga"
end
```

File
If the .jpeg file is placed on the Control4 controller by the driver, the GetNotificationAttachmentFile API should be included in your driver to return the file.

```
function GetNotificationAttachmentFile()
	return "image.jpg"
end
```


### Memory

If the .jpeg file is stored in the memory of the device, the GetNotificationAttachmentBytes API should be included in your driver to return the file. Note that this API has the potential to block data if the driver takes too long to execute the function. If it takes more than one second, a log entry will be created in the director log warning that the driver took too long. This is also logged in the driver debug log file. The log entry for this is: 

“The driver: \<driver name\>(\<device id\>) took more than 1 second to get the notification extractnotifcation bytes.” 

```
function GetNotificationAttachmentBytes()
	local imageData = ??? -- Get image from somewhere

    return C4:Base64Encode(imageData)
end
```

Note that in the example above, the image is Base64 encoded. This is a requirement. 

Finally, an API has been included in the event that your driver needs to do any sort of clean-up with the stored .jpeg file. It also provides a notification when the original notification has been sent. This is an optional API and only recommended if cleanup is needed. For example, if it is desirable to remove a temporary image file from your system. 

```
function FinishedWithNotificationAttachment()
  -- do any cleanup required here.
end
```

To assist with implementation, please see the notification driver.c4z file in the Samples folder of this SDK.