## List of Room Variables

To the right is an example of subscribing to the currently selected device and the navigator variables of the room.

```
Variable_Current_Selected_Device = VARIABLE_ID_START,
Variable_Current_Audio_Device,
Variable_Current_Video_Device,
Variable_Audio_Volume_Device,
Variable_Video_Volume_Device,
Variable_Current_Media,
Variable_Current_Media_Type,
Variable_Current_Audio_Path,
Variable_Current_Video_Path,
Variable_Current_Video_Audio_Path,
Variable_Power_State,
Variable_Current_Volume,
Variable_Temperature_ID,
Variable_Temperature_Control_ID,
Variable_Security_ID,
Variable_Current_Volume_Device,
Variable_Has_Discrete_Volume,
Variable_Has_Discrete_Mute,
Variable_Is_Muted,
Variable_In_Navigation,
Variable_Use_Default_Volumes,
Variable_Default_Audio_Volume,
Variable_Default_Video_Volume,
Variable_Volume_Linked,
Variable_Linked_Room_List,
Variable_Mute_Linked,
Variable_RoomOff_Linked,
Variable_Selections_Linked,
Variable_Current_Linked_MediaID,
Variable_Room_Hidden,
Variable_Linked,
Variable_Media_Info,
Variable_Last_Device_Group,
Variable_Available_Cameras,
Variable_Pools,
Variable_Scene_Is_Discrete_Volume,
```



### Example

```
roomId = C4:RoomGetId()
-- be notified when the currently selected device is changed
C4:RegisterVariableListener(roomId, 1000)
-- be notified when we are in nav or not
C4:RegisterVariableListener(roomId, 1019)


function OnWatchedVariableChanged(idDevice, idVariable, strValue) 
  print("Variable changed...") 
  print("  device: " .. idDevice) 
  print("  variable: " .. idVariable) 
  print("  value: " .. strValue) 
  print("-----------") 
end 


	C4:SendToDevice(roomId, "CONTROL4", tParams) 
	C4:SendToDevice(roomId, "EXIT_NAVIGATION", tParams) 
```

```
-- Example Output

Variable changed...
device: 5
variable: 1000
value: 7

-----------

Variable changed...
device: 5
variable: 1019
value: 1

-----------

Variable changed...
device: 5
variable: 1019
value: 0
```