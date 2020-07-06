## CreateTCPServer

This class does not in any way manage or keep track of connected clients.  If you explicitly [Close][1]() the TCP server or it goes out of scope and gets cleaned up by lua's garbage collector, it does not affect any of the accepted client connections. You can keep track of connected clients by saving them into a map in the OnAccept callback, and setting up a OnDisconnect callback for the connected client connection that removes that client from that map.

Generally, the class cleans up any resources associated with it.  For example, when the object is no longer referenced, it will clean it up.  However, there are a few exceptions:  When the class is performing an asynchronous operation, e.g. a listen request, it will remain alive until the appropriate event callback function is called.  For instance, if you call the [Listen][2]() method, the class will remain alive until it either called the [OnListen][3] (and [OnResolve][4]) callback function, or the [OnError][5] callback function, even if your lua code does not have any reference to the class during that time period.  However, once the OnListen callback was called, the class gets cleaned up unless at that point your lua code somehow references this instance. This API should not be invoked 
during OnDriverInit.

###### Available in 1.6.0


### Example

This is an example of a chat server that accepts a configurable number of clients and shuts the server down after a configurable number of minutes.  It manages all its client connections and shuts them down when the server is being shut down.



```lua
local server = {
       clients = {},
       clientsCnt = 0,
       --socket = nil,
       notifyOthers = function(self, client, message)
              for cli,info in pairs(self.clients) do
                     if (cli ~= client and info.name ~= nil) then
                           cli:Write(message .. "\r\n")
                     end
              end
       end,
       broadcast = function(self, client, message)
              local info = self.clients[client]
              print("broadcast for client " .. tostring(client) .. " info: " ..tostring(info))
              if (info ~= nil and info.name ~= nil) then
                     self:notifyOthers(client, info.name .. " wrote: " .. message .. "\r\n")
                     client:Write("You wrote: " .. message .. "\r\n")
              end
       end,
       haveName = function(self, name)
              for _,info in pairs(self.clients) do
                     if (info.name ~= nil and string.lower(info.name) == string.lower(name)) then
                           return true
                     end
              end
              return false
       end,
       stripControlCharacters = function(self, data)
              local ret = ""
              for i in string.gmatch(data, "%C+") do
                     ret = ret .. i
              end
              return ret
       end,
       stop = function(self)
              if (self.socket ~= nil) then
                     self.socket:Close()
                     self.socket = nil

                     -- Make a copy of all clients and reset the map.
                     -- This ensures that calls to self:broadcast() and self:notifyOthers()
                     -- during the shutdown process get ignored.  All we want the clients to
                     -- see is the shutdown message.
                     local clients = self.clients
                     self.clients = {}
                     self.clientsCnt = 0

                     for cli,info in pairs(clients) do
                           print("Disconnecting " .. cli:GetRemoteAddress().ip .. ":" .. cli:GetRemoteAddress().port .. ": name: " .. tostring(info.name))
                           cli:Write("Server is shutting down!\r\n"):Close(true)
                     end
              end
       end,
       start = function(self, maxClients, bindAddr, port, done)
              local calledDone = false
              self.socket = C4:CreateTCPServer()
                     :OnResolve(
                           function(srv, endpoints)

                                  print("Server " .. tostring(srv) .. " resolved listening address")
                                  for i = 1, #endpoints do
                                         print("Available endpoints: [" .. i .. "] ip=" .. endpoints[i].ip .. ":" .. endpoints[i].port)
                                  end
                           end
                     )
                     :OnListen(
                            function(srv, endpoint)
                                  -- Handling this callback is optional.  It merely lets you know that the server is now actually listening.
                                  local addr = srv:GetLocalAddress()
                                  print("Server " .. tostring(srv) .. " chose endpoint " .. endpoint.ip .. ":" .. endpoint.port .. ", listening on " .. addr.ip .. ":" .. addr.port)
                                  if (not calledDone) then
                                         calledDone = true
                                         done(true, addr)
                                  end
                           end
                     )
                     :OnError(
                           function(srv, code, msg, op)
                                  -- code is the system error code (as a number)
                                  -- msg is the error message as a string
                                  print("Server " .. tostring(srv) .. " Error " .. code .. " (" .. msg .. ")")
                                  if (not calledDone) then
                                         calledDone = true
                                         done(false, msg)
                                  end
                           end
                     )
                     :OnAccept(
                           function(srv, client)
                                  -- srv is the instance C4:CreateTCPServer() returned
                                  -- client is a C4LuaTcpClient instance of the new connection that was just accepted
                                  print("Connection on server " .. tostring(srv) .. " accepted, client: " .. tostring(client))
                                  if (self.clientsCnt >= maxClients) then
                                         client:Write("Sorry, I only allow " .. maxClients .. " concurrent connections!\r\n"):Close(true)
                                         return
                                   end
                                  local info = {}
                                  self.clients[client] = info
                                  self.clientsCnt = self.clientsCnt + 1
                                  client
                                         :OnRead(
                                                function(cli, data)
                                                       -- cli is the C4LuaTcpClient instance (same as client in the OnAccept handler) that the data was read on
                                                       if (string.sub(data, -2) == "\r\n") then
                                                              -- Need to check if the delimiter exists.  It may not if the client sent data without one and then disconnected!
                                                              data = string.sub(data, 1, -3) -- Cut off \r\n
                                                       end
                                                       data = self:stripControlCharacters(data)
                                                       if (info.name == nil) then
                                                              if (#data > 0) then
                                                                     if (self:haveName(data)) then
                                                                           cli:Write("Choose a different name, please:\r\n")
                                                                     else
                                                                           info.name = data
                                                                           self:notifyOthers(cli, info.name .. " joined!\r\n")
                                                                           cli:Write("Thank you, " .. info.name .. "! Type 'quit' to disconnect.\r\n")
                                                                     end
                                                              else
                                                                     cli:Write("Please enter your name:\r\n")
                                                              end
                                                              cli:ReadUntil("\r\n")
                                                       elseif (data == "quit") then
                                                              cli:Write("Goodbye, " .. info.name .. "!\r\n"):Close(true)
                                                       else
                                                              if (#data > 0) then
                                                                     self:broadcast(cli, data)
                                                              end
                                                              cli:ReadUntil("\r\n")
                                                       end
                                                end
                                         )
                                         :OnWrite(
                                                function(cli)
                                                       -- cli is the C4LuaTcpClient instance (same as client in the OnAccept handler).  This callback is called when
                                                       -- all data was sent.
                                                       print("Server " .. tostring(srv) .. " Client " .. tostring(client) .. " Data was sent.")
                                                end
                                         )
                                         :OnDisconnect(
                                                function(cli, errCode, errMsg)
                                                       -- cli is the C4LuaTcpClient instance (same as client in the OnAccept handler) that the data was read on
                                                       -- errCode is the system error code (as a number).  On a graceful disconnect, this value is 0.
                                                       -- errMsg is the error message as a string.
                                                       if (errCode == 0) then
                                                              print("Server " .. tostring(srv) .. " Client " .. tostring(client) .. " Disconnected gracefully.")
                                                       else
                                                              print("Server " .. tostring(srv) .. " Client " .. tostring(client) .. " Disconnected with error " .. errCode .. " (" .. errMsg .. ")")
                                                       end

                                                       if (info.name ~= nil) then
                                                              self:notifyOthers(cli, info.name .. " disconnected!\r\n")
                                                       end
                                                       self.clients[cli] = nil
                                                       self.clientsCnt = self.clientsCnt - 1
                                                end
                                         )
                                         :OnError(
                                                function(cli, code, msg, op)
                                                       -- cli is the C4LuaTcpClient instance (same as client in the OnAccept handler) that the data was read on
                                                       -- code is the system error code (as a number)
                                                       -- msg is the error message as a string
                                                       -- op indicates what type of operation failed: "read", "write"
                                                       print("Server " .. tostring(srv) .. " Client " .. tostring(client) .. " Error " .. code .. " (" .. msg .. ") on " .. op)
                                                end
                                         )
                                         :Write("Welcome! Please enter your name:\r\n")
                                         :ReadUntil("\r\n")
                           end
                     )
                     :Listen(bindAddr, port)
              if (self.socket ~= nil) then
                     return self
              end
       end
}

-- Start the server with a limit of 5 concurrent connections, listen on all interfaces on a randomly available port.  The server will shut down after 10 minutes.
server:start(5, "*", 0, function(success, info)
       if (success) then
              local minutes = 10
              print("Server listening on " .. info.ip .. ":" .. info.port .. ". Will stop in " .. minutes .. " minutes!")
              C4:SetTimer(minutes * 60 * 1000, function()
                     print("Stopping server and disconnecting clients now.")
                     server:stop()
              end)
       else
              print("Could not start server: " .. info)
       end
end)
```

[1]:	https://control4.github.io/docs-driverworks-api/#close
[2]:	https://control4.github.io/docs-driverworks-api/#listen
[3]:	https://control4.github.io/docs-driverworks-api/#onlisten
[4]:	https://control4.github.io/docs-driverworks-api/#onresolve
[5]:	https://control4.github.io/docs-driverworks-api/#onerror