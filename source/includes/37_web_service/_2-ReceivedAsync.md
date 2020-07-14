## ReceivedAsync

This function is used in conjunction with [urlGet][1] and [urlPost][2]. It handles the data contained in the data ticket. As soon as data is returned from getUrl, Director will call this in the Lua code. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`function ReceivedAsync(ticketId, strData, responseCode, tHeaders, strError)`	


### Parameters

`None`


### Returns
| Parameter | Description |
| --- | --- |
| num | Number representing the data ticket |
| str | String representing the data contained in the ticket |
| code| Response code |
| table |  Lua table of response headers |
| str | String representing the error content |


### Example

```lua
function ReceivedAsync(ticketId, strData)
  callType = g_ticketToTypeMap[ticketId]
  --print("ra - ct = " .. callType .. " id is " .. ticketId .. " data is<< " .. strData .. " >>")
  if (callType == "root") then
        g_shoutCastHtmlParsed = parsestr(strData)
  elseif (callType == "playlist") then
                stationUrl = GetStationUrlFromHtml(strData)
			if (stationUrl) then
                   print("Adding station " .. stationUrl)
                         AddStationToDb(stationUrl, ticketId)
         else
                -- must have been a genre item they clicked on
            genreTable = parsestr(strData)
            ShowSubGenres("Add Genre", genreTable)
                end
  else
                print("ReceivedAsync called with unexpected id of " .. ticketId) -- ..  and data of " .. strData)
  end
end
```

[1]:	https://control4.github.io/docs-driverworks-api/#get
[2]:	https://control4.github.io/docs-driverworks-api/#post