## tonumberloc

The Lua tonumber() function included in the Lua Library is locale specific. This can cause issues where the
Control4 system is set to a locale where the decimal separator is different from what is returned by the target device.  For example, if the target device sends the Control4 driver a string of  23.4 (23 decimal 4) but the locale expects this to be 23,4 (23 comma 4) then tonumber("23.4") will fail.  This problem often occurs in drivers where the UI uses decimal values and can occur with any proxy. 

Driver writers must ensure that their drivers will not fail in these circumstances. To assist with this, Control4 has provided a function: tonumberloc(). This function is included in the driver templates beginning OS release 2.8.0 and its use ensures this problem does not occur.  Driver writers are advised to usetonumberloc()  in place of tonumber() in their code.

###### Available from 1.6.0.


### Signature

`tonumber_loc()`


### Example

```lua

function tonumber_loc(str, base)
  local s = str:gsub(",", ".") -- Assume US Locale decimal separator
  local num = tonumber(s, base)
  if (num == nil) then
    s = str:gsub("%.", ",") -- Non-US Locale decimal separator
    num = tonumber(s, base)
  end
  return num
end
```