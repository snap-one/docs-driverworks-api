## GetNetworkConnections

Function that returns a table containing all of the device connections as well as data for each individual connection.

###### Available from 3.0.0


### Signature

`C4:GetNetworkConnections()`


| Parameter | Description                                                                                 |
| --------- | ------------------------------------------------------------------------------------------- |
| table     | Table containing connection information for the device and Information for each connection. |


### Usage Note
Note that table data will vary based on device. Below are examples of each of the connection types supported by the function. Note the type table element. This is a numeric value between 0 and 8. The values are:

- 0 = unknown
- 1 = UUID
- 2 = Internet Protocol (IP)
- 3 = Zigbee
- 4 = HOSTNAME
- 5 = Secure Socket layer (SSL)
- 6 = SSL\_HOSTNAME
- 7 = Unix Domain Socket
- 8 = ZWave



### Returns

Network Binding information for the device.


### Examples

The examples shown to the right return tables for each connection type:

Home Controller using a **UUID** connection. Note the state of 1 which indicates an active connection:

```lua
UUID
firmware:  
address:  127.0.0.1
type:  1
bindingid:  6001
deviceid:  63
state:  1
gateway:  
name:  Home Controller EA5
port:  5116
```

Control4 8-Channel Relay using an **IP** connection. Note the state of 0 which indicates as inactive connection:

```lua
IP
address:  
type:  2
state:  0
deviceid:  43
firmware:  
gateway:  
name:  8-Channel Relay P1S3
bindingid:  6001
```

Control4 Configurable Keypad using a **Zigbee** connection:

```lua
Zigbee
firmware:  4.1.22
address:  000fff000077f532
type:  3
bindingid:  6001
deviceid:  75
state:  1
gateway:  
name:  Configurable Keypad
port:  7900
```

HOSTNAME - A **HOSTNAME** connection type returns a valid URL such as:

 `http://control4.com`

A driver that uses an **SSL** connection:

```lua
SSL
address:  192.168.1.123
type:  5
state:  1
deviceid:  216
firmware:  
gateway:  
name:  Driver Properties
bindingid:  6001
```

SSL HOSTNAME - An SSL HOSTNAME connection type returns a valid, secure URL such as:

 `https://control4.com`

UNIX DOMAIN SOCKET - A Unix Domain Socket connection type returns connection information between processes executing on the same Host, such as Director.

 **Z-Wave** Dimmer: 

```lua
Z-Wave
device_lights:  green
network_status:  online
state:  1
firmware:  
type:  8
uuid:  zwave:cd94eba9:11
security_status:  notSupported
address:  cd94eba9:11
driver_enabled:  1
deviceid:  25
wake_status:  awake
device_status:  ready
gateway:  
name:  Leviton Z-Wave DZPD3 Lamp Dimmer Module
port:  0
```