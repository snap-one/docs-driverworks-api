## Exit Navigation

This command is sent to the room to change the room from the “In Navigation” mode back to the “Normal” mode.  While in the “Normal” mode, the commands sent to the room are sent to the selected audio or video device.  When in the “In Navigation” mode a set of the navigational commands are sent to the on screen device.

For reference, the set of commands that are forwarded are:

- ”UP" 
- "DOWN" 
- "RIGHT"
- "LEFT"
- "PAGE_UP" _
- "PAGE_DOWN" 
- "CANCEL" "GUIDE"
- "START_UP" 
- "START_DOWN" 
- "START_RIGHT" 
- "START_LEFT" 
- "START_PAGE_UP” 
- "START_PAGE_DOWN” 
- "ENTER" 
- "STOP_UP" 
- "STOP_DOWN" 
- "STOP_RIGHT" 
- "STOP_LEFT" 
- "STOP_PAGE_UP" 
- "STOP_PAGE_DOWN" 
- "BACK"

Sending the “CONTROL4” command to the room will have it select the bound on screen navigation and enter the “In Navigation” mode.

Sending the `EXIT_NAVIGATION` command will have the room go back to the “Normal” mode.

##### Available from 1.6.0


### Example

	roomId = C4:RoomGetId()
	-- now tell the room to enter "In Navigation" mode
	tParams = {}
	C4:SendToDevice(roomId, "CONTROL4", tParams) 
	-- now go back to normal mode
	C4:SendToDevice(roomId, "EXIT_NAVIGATION", tParams)