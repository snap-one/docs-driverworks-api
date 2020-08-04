## GetDevices

The GetDevices API provides the ability to return a table of devices based on driver names and/or device ID values. Additionally, the use of the location parameter further limits the list returned based on locations found within a project.

###### Available from 2.10.0


### Signature

`GetDevices(tFilter, locationFilter)`


### Parameters

tFilter:  (optional) The tFilter is a table of key/value pairs that specify the filters used within the search. The search can be filtered by .c4i or .c4z driver names and/or device id values.  To filter by driver names, add an entry in the table called C4iNames. The value is a string consisting of a comma delimited list of .c4i or .c4z names such as:

 `control4_sr250.c4i, control4_sr150.c4i`.  

An example of a table would be: 

`tFilter = {C4iNames = "control4_sr260.c4i,control4_sr250.c4i,control4_sr150.c4i"}`

To filter by device id values rather than driver names, add an entry in the table called DeviceIds. The value is a string consisting of a comma delimited list of ID values representing Proxy IDs or Device IDs such as: “22,23,24”. An example of a table would be:
  
`tFilter = {DeviceIds = "22,34,56"}`

Note that the tFilter parameter is an optional parameter of the GetDevices function. Also, empty filter tables  tFilter = {} can be passed within the function. This will result in all devices being included when the function is executed.

locationFilter: The locationFilter parameter is a comma delimited list of project location IDs. Only devices matching the filter criteria used in the first parameter and belonging to one of the locations in the list will be included when the function is executed. Locations IDs include Sites, Buildings, Floors and Rooms.


### Returns

| Value | Description |
| --- | --- |
| table | tReturn: Varies  based on not only the parameters passed in it, but the types of drivers in the project. Driver types that should be considered when viewing return data include: Combo Drivers, Proxy/Protocol Driver and Multi-Proxy Drivers. |

To better understand how driver data is arranged in tables and how the data is returned by the GetDevices API, the following section consists of example data returned from the function. 

### Example 1

Return Example for All Drivers including Combo Drivers
GetDevices returns a table with an entry for each device found. The key of the entry is the ID number of the device. The value is a table that contains additional information about the device. The table contains the following key-value pairs:

| Key | Value |
| --- | --- |
| driverFileName |  `<driver_filename>` |
| deviceName | `<device_filename>` |
| roomID |  `<room_ID>` |
| roomName | `<room_name>` |

To the right is an example where you would like to get a list of all the remotes in the project. Passing driver names, you would use GetDevices in the following manner:

```lua
-- Example 1

tFilter = {
	C4iNames = "control4_sr260.c4i,
		control4_sr250.c4i, 
		control4_sr150.c4i"}

tResult = C4:GetDevices(tFilter)
```

The table that is returned by the GetDevices command (that was stored in tReturn) is to the right :

```lua
 -- Example 1 Return
   
    [27] = {
        driverFileName = "control4_sr150.c4i",
        deviceName = "System Remote Control SR-150",
        roomId = "26",
        roomName = "Master"
    },
    [17] = {
        driverFileName = "control4_sr260.c4i",
        deviceName = "System Remote Control SR260",
        roomId = "16",
        roomName = "Dining"
    },
    [21] = {
        driverFileName = "control4_sr150.c4i",
        deviceName = "System Remote Control SR-150",
        roomId = "20",
        roomName = "Laundry"
    },
    [25] = {
        driverFileName = "control4_sr250.c4i",
        deviceName = "System Remote Control SR-250",
        roomId = "24",
        roomName = "Bathroom"
    },
    [19] = {
        driverFileName = "control4_sr150.c4i",
        deviceName = "System Remote Control SR-150",
        roomId = "18",
        roomName = "Kitchen"
    },
    [14] = {
        driverFileName = "control4_sr260.c4i",
        deviceName = "System Remote Control SR260",
        roomId = "13",
        roomName = "Living"
    }
}
```

In this  example, note the value of 27. This is the index into the table that, in this example, contains a list of key/value pairs of device information for the remote with device id of 27. Based on our return table, we can see the project has six remotes and we can also see which room those remotes are located as well as the location ID value and their respective device name.

### Example 2

Return Example for a Proxy Driver 
Proxy Drivers return a table as described in the previous example with the addition of an extra key/value pair. The additional information is the protocol information for the driver. In the table returned, the additional key is the driverFilename and its value is the string of the protocol's name. The return table structure looks like this:

| Key | Value |
| --- | --- |
| driverFileName | `<driver_filename>` |
| deviceName  |`<device_filename>` |
| roomID | `<room_ID>` |
| roomName | `<room_name>` |

In addition to key value pairs above, a protocol sub-table is also returned that contains the protocol information. This table contains another table with the file name of the protocol and the device name: …

| Protocol | Table |
| --- | --- |
| deviceId | `table` |
| driverFileName |  `<protocol_filename> ` |
| deviceName | `<name_of_devie>` |

For example, if you would like to get a list of all lights in the project, you could execute GetDevices  passing the `light_v2.c4z"`as the tFilter parameter.  `light_v2.c4z `is the proxy file name used by the lights:

``C4:GetDevices(`light_v2.c4z`)``

The table that is returned by the GetDevices command looks like this:

```lua
-- Example 2

{
    [11] = {
        deviceName = "Keypad Dimmer Light",
        protocol = {
            [10] = {
                driverFileName = `combo_dimmer.c4i`,
                deviceName = "Keypad Dimmer Light"
            }
        },
        roomName = "Foyer",
        roomId = "9",
        driverFileName = "light_v2.c4i"
    }
}
```

Based on this return table, we can see that the project has one light., located in the Foyer, which happens to have a location ID of 9. Additionally, we can see the protocol sub-table that  is returned with the driver filename and the device name.

Example 3: Return Example for a Protocol Driver 
Protocol Drivers that have one or more proxies have an additional key-value pair returned from GetDevices. The key is proxies. "proxies" is a table with an entry for each proxy found within the driver.  The key of the entry is the Proxy ID. The value is a table that contains additional information about the proxy, specifically the proxyFilename and deviceName values.

The table contains the following key-value pairs:

| Key | Value |
| --- | --- |
| driverFileName | `<driver_filename>` |
| deviceName | `<device_filename>` |
| roomID |  `<room_ID>` |
| roomName | `<room_name>` |

In addition to key value pairs above, a proxy sub-table is also returned that contains the proxy information. This table contains another table with the file name of the proxy and the device name:

| Key | Value |
| --- | --- |
| deviceId | `table` |
| driverFileName | `<proxy_filename>` |
| deviceName |  `<name_of_devie>` |

If the device utilizes multiple proxies, each of those proxies will be represented here by its respective table.

Consider an example where you would like to get a list of all of the keypad dimmers in the project.  These dimmer devices rely on two proxies: a proxy for the dimmer portion of the device `light_v2 proxy` as well as a proxy for the keypad capabilities `keypad_proxy`. To do this, you can pass the proxy id value used by the dimmers in the tFilter parameter:

```lua
tFilter = {
	c4iNames = "combo_dimmer.c4i"}

tResult = C4:GetDevices(tFilter)

The tReturn table would look like this:
{
    [10] = {
        deviceName = "Keypad Dimmer Light",
        proxies = {
            [11] = {
                driverFileName = "light_v2.c4i",
                deviceName = "Keypad Dimmer Light"
            },
            [12] = {
                driverFileName = "keypad_proxy.c4i",
                deviceName = "Keypad"
            }
        },
        roomName = "Foyer",
        roomId = "9",
        driverFileName = "combo_dimmer.c4i"
    }
}
```

Based on this return table, we can see to the right that the project has one light, located in the Foyer, which happens to have a location ID of 9. Additionally, we can see the two proxy sub-tables that are returned with the driver filename.







