## Sending Room Keypress Commands from Receiver Driver


```lua
roomId = C4:RoomGetId()
	tParams = {}
	tParams = {}
-- send 1 keypress to the room’s currently selected device
```

Note that commands not recognized by the room and director will still be sent through to the selected proxy device. The proxy may filter out unknown commands or it may still forward them to the protocol driver.

```lua
roomId = C4:RoomGetId()
tParams = {}
-- send 1 keypress to the room’s currently selected device
C4:SendToDevice(roomId, "FOO", tParams) 
```

Output from Media Player driver when receiver driver sent above commands:

```lua
ReceivedFromProxy called for mediaplayer xbmc with command:PAUSE
..Parameter: ROOM\_ID with value: 39
Received Action Response action id=12 erroCode=0
position= 0 value=0
ReceivedFromProxy called for mediaplayer xbmc with command:FOO
..Parameter: ROOM\_ID with value: 39
```
