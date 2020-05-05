## GetDeviceData

This API returns data found in the driver's device data, \<devicedata\> XML. The Device ID of the driver value must be passed to return the XML content. An optional string value parameter can be passed to retrieve specific XML data.

###### Available from 2.10.0


### Signature

`C4:GetDeviceData()`


| Parameters | Description |
| --- | --- |
| num | Device ID of the driver. |
| str |  tagName is an optional parameter that can be passed to return specific devicedata. |

### Usage Note

For example, if the “string parameter is passed as “version”, the value for the devicedata's \<version\>\</version\> XML tag will be returned. 


### Returns

XML data found in the driver's `<devicedata></devicedata>`. 


### Usage Note

If multiple instances of identical XML tags exist in the \<devicedata\> section for the driver, only the first instance of that XML data will be returned. Also, the GetDeviceData API only has the ability to return data from the first two levels of XML.


### Examples

For example purposes, consider the following, sample XML taken from a Pool Controller's  \<devicedata\>\</devicedata\>. This Pool Controller has a DeviceID of 8 in the project:

```
<devicedata>
	<copyright>Copyright 2016 Control4 Corporation.  All rights reserved.</copyright>
	<creator>Control4</creator>
	<created>8/26/2014 2:09 PM</created>
	<modified>11/17/2015 11:00 AM</modified>
	<version>7</version>
	<control>lua_gen</control>
	<controlmethod>ip</controlmethod>
	<driver>DriverWorks</driver>
	<proxies qty="1">
		<proxy proxybindingid="5001" primary="True">pool</proxy>
	</proxies>
	<capabilities>
		<pool_pumpmodes>Off,On</pool_pumpmodes>
		<spa_pumpmodes>Off,On</spa_pumpmodes>
		<temp_min>34</temp_min>
		<temp_max>104</temp_max>
		<pool_heat_modes>
			<mode>
				<id>1</id>
				<text>Heater</text>
			</mode>
			<mode>
				<id>2</id>
				<text>Solar Heater</text>
			</mode>
		</pool_heat_modes>
		<spa_heat_modes>
			<mode>
				<id>1</id>
				<text>Heater</text>
			</mode>
		</spa_heat_modes>
	</capabilities>
</devicedata>
```

If `C4:GetDeviceData` is executed with only the Device ID value, as:

`C4:GetDeviceData(8)`

All of the XML found in the \<devicedata\> section of the driver is returned. 

`C4:GetDeviceData` can also be executed with the optional tagName parameter to return specific XML data. For example, If `C4:GetDeviceData` is executed with the Device ID value and the version tag, as:

`C4:GetDeviceData(8, “version”)`

The return value will be: 7

Similarly, the API can return all of the supported pump modes by passing C4:GetDeviceData as:

 `C4:GetDeviceData(8, “pool\_pumpmodes”)`
\`
The return values will be: `Off,On`

If we wanted to return all of the pool Controller's capabilities, C4:GetDeviceData is passed as:

`C4:GetDeviceData(8, “capabilities”)`

To the right is the return value: 

```

<pool_pumpmodes>Off,On</pool_pumpmodes>
<spa_pumpmodes>Off,On</spa_pumpmodes>
<temp_min>34</temp_min>
<temp_max>104</temp_max>
<pool_heat_modes>
	<mode>
		<id>1</id>
		<text>Heater</text>
	</mode>
	<mode>
		<id>2</id>
		<text>Solar Heater</text>
	</mode>
</pool_heat_modes>
<spa_heat_modes>
	<mode>
		<id>1</id>
		<text>Heater</text>
	</mode>
</spa_heat_modes
```