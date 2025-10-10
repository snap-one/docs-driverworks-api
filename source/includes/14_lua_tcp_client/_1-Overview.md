## CreateTCPClient

Generally, the class cleans up any resources associated with it.  For example, when the object is no longer referenced, it will cleans it up.  However, there are a few exceptions:  When the class is performing an asynchronous operation, e.g. a connect request, it will remain alive until the appropriate event callback function is called. This method closes an established connection, or cancels a pending resolve or connection request. If a resolve or connection request is canceled, the OnError callback function will get called. This API should not be invoked during OnDriverInit. Once you call this method, no more data will be read from the socket and you can no longer write additional data to the socket. Also, the OnWrite callback will not be called anymore, even if the flush argument is set to true.

For instance, if you call the [Connect][1]() method, the class will remain alive until it either called the [OnConnect][2] (and [OnResolve][3]) callback function, or the [OnError][4] callback function, even if your lua code does not have any reference to the class during that time period.  The same applies to the time period between calling one of the Read() methods and the corresponding OnRead() or OnError() callback, and in between calling the Write() method and the OnWrite() or OnError() callback. This API should not be invoked during OnDriverInit.

###### Available in 1.6.0

### Example

```lua
function PullHttpPage(host, path, timeout, done)
 local timer
 local completed = false
 local complete = function(data, errMsg)
  if (not completed) then
   completed = true
   if (timer ~= nil) then
    timer:Cancel()
   end
   done(data, errMsg)
  end
 end
 local readingHeaders, needBytes, response, allReceived
 local cli = C4:CreateTCPClient()
  :OnConnect(function(client)
   local remote = client:GetRemoteAddress()
   print("Connected to " .. remote.ip .. ":" .. remote.port)
   client:Write("GET " .. path .. " HTTP/1.0\r\nHost: " .. host .. "\r\n\r\n"):ReadUntil("\r\n")
   readingHeaders = true
   needBytes = nil
   response = ""
   allReceived = false
   -- start reading data
   client:ReadUntil("\r\n")
  end)
  :OnResolve(function(client, endpoints, choose)
   -- Implementing this callback is optional
   print("Resolved.  Artificially delay choosing endpoint by one second...")
   C4:SetTimer(1000, function(_)
    --choose(1) -- This would choose the first endpoint in the endpoints array
    --choose(0) -- Abort the connection request
    choose() -- Default behavior, this chooses the first endpoint (if available)
   end)
  end)
  :OnDisconnect(function(client, errCode, errMsg)
   if (errCode ~= 0) then
    complete(nil, "Disconnected with error " .. errCode .. ": " .. errMsg)
   elseif (needBytes == nil) then
    complete(nil, "Disconnected and no or invalid response received")
   elseif (needBytes > 0) then
    complete(nil, "Disconnected and received partial response")
   end
  end)
  :OnRead(function(client, data)
   if (readingHeaders) then
    if (data ~= "\r\n") then
     -- Look for the Content-Length header
     local sep = string.find(data, ":", 1, true)
     if (sep ~= nil and sep > 1) then
      local header = string.lower(string.sub(data, 1, sep - 1))
      local value = string.sub(data, sep + 1, -2)
      if (header == "content-length") then
       needBytes = tonumber(value)
      end
     end
     client:ReadUntil("\r\n")
    else
     readingHeaders = false
     if (needBytes ~= nil and needBytes > 0) then
      -- Got all headers, now read the body
      client:ReadUpTo(needBytes)
     else
      -- No body to read
      client:Close()
      if (needBytes == 0) then
       complete("")
      end
     end
    end
   else
    -- Append the body data
    response = response .. data
    needBytes = needBytes - string.len(data)
    if (needBytes > 0) then
     -- We haven't received everything, read more
     client:ReadUpTo(needBytes)
    else
     -- We received the entire body
     client:Close()
     complete(response)
    end
   end
    end)
  :OnError(function(client, errCode, errMsg)
   complete(nil, "Error " .. errCode .. ": " .. errMsg)
  end)
  :Connect(host, 80)
 if (timeout > 0) then
  timer = C4:SetTimer(timeout, function()
   cli:Close()
   complete(nil, "Timed out!")
  end)
 end
end
print("Downloading http://example.com/ ...")
PullHttpPage("example.com", "/", 5000, function(info, err)
 if (info ~= nil) then
  print("GOT: " .. tostring(info))
 else
  print("ERROR: " .. err)
 end
end)
```

[1]: https://snap-one.github.io/docs-driverworks-api/#tcpclient-interface-connect
[2]: https://snap-one.github.io/docs-driverworks-api/#tcpclient-interface-onconnect
[3]: https://snap-one.github.io/docs-driverworks-api/#tcpclient-interface-onresolve
[4]: https://snap-one.github.io/docs-driverworks-api/#tcpclient-interface-onerror
