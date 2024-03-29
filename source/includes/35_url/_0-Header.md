# URL Interface

This API Interface replaces the following APIs:

- `C4:urlGet()`

- `C4:urlPost()`

- `C4:urlPut()`

- `C4:urlDelete()`

- `C4:urlCustom()`

C4:url() utilizes a more flexible callback-based object interface. A call to this function returns a C4:url object that can be set up with various callback functions and options. Once set up, a call to its methods: [Get()][1], [Post()][2], [Put()][3], [Delete()][4], or [Custom()][5] initiates the transfer.

###### Available from 2.10.5


To the right is a basic example of how this interface can be used:

```lua
local t = C4:url()
 :OnDone(
  function(transfer, responses, errCode, errMsg)
   if (errCode == 0) then
    local lresp = responses[#responses]
    print("OnDone: transfer succeeded (" .. #responses .. " responses received), last response code: " .. lresp.code)
    for hdr,val in pairs(lresp.headers) do
     print("OnDone: " .. hdr .. " = " .. val)
    end
    print("OnDone: body of last response: " ..tostring(lresp.body))
   else
    if (errCode == -1) then
     print("OnDone: transfer was aborted")
    else
     print("OnDone: transfer failed with error " .. errCode .. ": " .. errMsg .. " (" .. #responses .. " responses completed)")
    end
   end
  end)
 :SetOptions({
  ["fail_on_error"] = false,
  ["timeout"] = 30,
  ["connect_timeout"] = 10
 })
 :Get("http://www.example.com", { ["Expect"] = "100-continue" })
print("scheduled url transfer with id " .. t:TicketId())
```

The C4:url Object that is returned supports the APIs defined in this section.

[1]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-get
[2]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-post
[3]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-put
[4]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-delete
[5]:	https://snap-one.github.io/docs-driverworks-api/#url-interface-custom