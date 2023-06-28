## urlCancel

Function to cancel an ongoing transfer. Note that if a transfer is canceled, neither the ReceivedAsync() entry point nor the callback function specified in the [C4:url][1] call will be called.  Also, the ticketId is only valid from the point the C4:url function is called until either the [ReceivedAsync()][2] entry point or the callback function was called. A call to C4:urlCancel() will also invalidate that ticketed. This API should not be invoked during OnDriverInit

###### Available from 2.7.0.


### Signature

`C4:urlCancel(ticketId)`


| Parameter | Description |
| --- | --- |
| num | Number representing the ticket ID value. |


### Returns

| Parameter | Description |
| --- | --- |-
| bool | True if the specified transfer was canceled. |


### Usage Note

Control4 Web Service APIs, specifically those beginning with [C4:url][3],  send the following default Headers with the HTTP(s) request:

```html
Host: <DNS name or IP of server>,
Accept: "/",
Accept-Encoding: "deflate, gzip"
Connection: "close", is suggested and
```


### Example

To the right is an example that does a C4:urlGet() and waits only a maximum of one second for a response before canceling:

```lua
local transferTicketId, timer
transferTicketId = C4:urlGet("http://www.example.com", {}, true, function(ticketId, strData, responseCode, tHeaders, strError)
        if (timer ~= nil) then
                  -- Cancel the timer if the transfer completed first
                  timer:Cancel()
                  timer = nil
                end
               
                if (strError == nil) then
                         print("C4:urlGet() completed with response code " .. tostring(responseCode))
                else
                         print("C4:urlGet() failed with error: " .. strError)
                end
end)
timer = C4:SetTimer(1000, function(tmr)
        local success = C4:urlCancel(transferTicketId)
        print("C4:urlGet() took too long, C4:urlCancel() returned " .. tostring(success))
end)
 
--[[
   Example output:
     If the timer expired before the transfer completed:
        C4:urlGet() took too long, C4:urlCancel() returned true
 
     If the transfer completed before the timer expired:
        C4:urlGet() completed with response code 200
--]]

```


[1]:	https://snap-one.github.io/docs-driverworks-api/#url-interface
[2]:	https://snap-one.github.io/docs-driverworks-api/#web-service-interface-receivedasync
[3]:	https://snap-one.github.io/docs-driverworks-api/#url-interface