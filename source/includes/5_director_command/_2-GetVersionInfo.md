## GetVersionInfo

Function that returns the version of Director that is currently running. This API can be invoked during OnDriverInit.

###### Available in 1.60.


### Signature

`C4:GetVersionInfo()`


### Parameters

`None`


### Returns

| Value | Description |
| --- | --- |
| buildtime | HH:MM:SS |
| builddate | mm  dd yyyy |
| version | 1.7.0.222 |
| buildtype | DEBUG |


### Example
```lua

local tVers = C4:GetVersionInfo()
local strVers = tVers["version"]

local major, minor, rev, build = string.match(strVers, "(%d+)\.(%d+)\.(%d+)\.(%d+)")

print("Major: " .. major .. " Minor: " .. minor .. " Rev: " .. rev .. " Build: " .. build)

if (tonumber(major) < 2) then
  if (tonumber(minor) < 8) then
    print("This Code requires at least version 1.8 to operate properly.  You are currently running version " .. strVers)
  end
end GetVersionInfo
```

