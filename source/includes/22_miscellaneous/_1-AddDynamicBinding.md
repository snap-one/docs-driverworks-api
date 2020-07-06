
## AddDynamicBinding

Function called by a DriverWorks driver to add a dynamic binding (a binding added at runtime).  This is typically done by security panels or other devices whose number of bindings are unknown when the driver is created.

###### Available from 1.6.0


### Signature

`C4:AddDynamicBinding(idBinding, strType, bIsProvider, strName, strClass, bHidden, bAutoBind)`


| Parameters | Description |
| --- | --- |
| num | ID of the dynamic binding. |
| str | Type of dynamic binding. Valid types include: CONTROL, PROXY |
| bool | Provider: Whether the binding is a Provider or a Consumer binding. |
| str | Name of binding that will appear in Composer’s connections page. |
| str | Class of dynamic binding that is being created. |
| bool | Hidden: Whether the dynamic binding is hidden. Should typically be false. |
| bool | AutoBind: Whether the dynamic binding should be auto-bound. Should typically be false |


### Example
Dynamically create 4 Zone Contact Bindings for a Security Driver:

	C4:AddDynamicBinding(101, "CONTROL", true, "Zone 1", "CONTACT_SENSOR", false, false)
	C4:AddDynamicBinding(102, "CONTROL", true, "Zone 2", "CONTACT_SENSOR", false, false)
	C4:AddDynamicBinding(103, "CONTROL", true, "Zone 3", "CONTACT_SENSOR", false, false)


### Usage Note

Currently, the AddDynamicBinding API does not work for Audio, Video and Room Control bindings.

It is the responsibility of the DriverWorks driver to maintain the Dynamic bindings and to restore them from persistent data upon the driver being initialized. If this is not done, the bindings will not be available after a Director restart.

If dynamic bindings have been connected in Composer, if they are properly restored by the DriverWorks driver, the connections made between the bindings will be automatically restored.

To the right is an example of how to create and save bindings for three security contacts:

	if (nil == PersistData) then
	  PersistData = {}
	end
	
	PersistData["zonebindings"] = {}
	PersistData["zonebindings"][101] = "Zone 1"
	
	C4:AddDynamicBinding(101, "CONTROL", true, "Zone 1", "CONTACT_SENSOR", false, false)
	PersistData["zonebindings"][102] = "Zone 2"
	
	C4:AddDynamicBinding(102, "CONTROL", true, "Zone 2", "CONTACT_SENSOR", false, false)
	PersistData["zonebindings"][103] = "Zone 3"
	C4:AddDynamicBinding(103, "CONTROL", true, "Zone 3", "CONTACT_SENSOR", false, false)
	

The next is an example of how to restore saved bindings. This code should be in the main body of the script section of the driver, not within any declared function:

	if (PersistData ~= nil) then
	  for key,value in pairs(PersistData["zonebindings"]) do 
	    C4:AddDynamicBinding(key, "CONTROL", true, value, "CONTACT_SENSOR", false, false)
	  end
	end


A sample driver using AddDyamicBinding can be found in the Samples folder of the SDK.

### Warning

No events will be sent prior to OnDriverLateInit. If an Event is required this method must be invoked in OnDriverLateInit.




