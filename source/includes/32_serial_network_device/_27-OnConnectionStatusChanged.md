## OnConnectionStatusChanged

Function called by director when the status of a network binding connection changes.

###### Available from 1.6.0


### Signature

`OnConnectionStatusChanged(idBinding, nPort, strStatus) `


| Parameter | Description |
| --- | --- |
| num | ID of the network binding whose status has changed |
| num | Port number whose status has changed |
| str | Status: “OFFLINE” or “ONLINE” |


### Example

```lua
function OnConnectionStatusChanged(idBinding, nPort, strStatus)
  if (idBinding == 6001) then
    if (strStatus == "ONLINE") then
      -- Connect was successful.  Send URL packet.
      -- Other actions…
      -- Send 'queued' HTTP request to WeatherBug:
      C4:SendToNetwork(6001, 80, g_URLPacket)
    else
      -- OFFLINE... This means the receive buffer is full and ready to 	
	process...
      -- Other actions…
    end
  end
end
```

