## OnDriverInit

Function invoked when a driver is loaded or being updated. This API is provided for the driver developer to initialize all of the driver objects that require initialization. 

###### Available from 2.0.0


### Signature

`C4:OnDriverInit() `


| Parameter | Description |
| --- | --- |
| str | This optional parameter indicates the scenario in which the driver is initializing. Scenarios include: |
|  |  `DIT_ADDING`: Called as a result of the driver being added to a project. |
|  |  `DIT_STARTUP`: Called as a result of Director starting or a new project being loaded. |
|  |  `DIT_UPDATING`: Called as a result of the driver being updated. |

The DIT parameters are available in O.S. 3.2.0 and later.


### Usage Note

**Driver Initialization and Destruction**
When a driver is loaded, there are two initialization functions that are called if those functions exist in the driver. They are OnDriverInit and OnDriverLateInit. When a driver is being removed, updated or otherwise removed from memory, OnDriverDestroyed will be called if that function has been implemented within the driver.

Your driver will need to implement these functions in order to complete its initialization process successfully. It’s important to know when these functions are called in order to know how to properly initialize a driver.

There are multiple instances of when a driver is loaded. Driver initialization occurs under the following conditions:

**Driver Added to Project:** When a driver is added to a project, OnDriverInit will be called followed by a call to OnDriverLateInit.

**Project Load: **When a project is loaded, either when director starts up or a new project is loaded, the following occurs:
1. As each driver is loaded, the OnDriverInit function is called.
2. After all the drivers in the project have been loaded, then OnDriverLateInit is called for all the drivers in the project. This ensures that all the driver’s bindings and initialization is complete. Any initialization that requires that all the bindings be bound, or other driver initialization is complete should be done in OnDriverLateInit.

**Driver Update:** When a driver is being updated, prior to the driver being reloaded, OnDriverDestroyed will be called. This will allow the driver to do any necessary cleanup prior to the driver being reloaded. When the driver is reloaded, OnDriverInit will be called followed by a call to OnDriverLateInit.

There may be instances when a driver needs to know under what condition or event caused the Initialization or Destroyed functions to be called. OS Release 3.2.0 introduced a new string parameter to these functions to identify the reason for the call. This parameter, driverInitType (DIT) provides this information.

OnDriverInit and OnDriverLateInit valid values for this parameter are as follows:
•	`DIT_ADDING`: When a driver is being added.
•	`DIT_STARTUP`: When a project is being loaded.
•	`DIT_UPDATING`: When a driver is being updated.

OnDriverDestroyed valid values are as follows:
•	`DIT_LOADED`: When the driver is being removed or director is being shut down.
•	`DIT_UPDATING`: When a driver is being updated.


### Example

```
function OnDriverInit(driverInitType)
         
    -- Fire On Property Changed to set the initial Headers and other
    -- Property global sets, they'll change if Property is changed.
    for k,v in pairs(Properties) do
       OnPropertyChanged(k)
    end

    C4:AddVariable("LIGHT_LEVEL", "0", "INT")
    C4:AddVariable("FIRMWARE_VERSION", "", "STRING")
    C4:AddVariable("EMERGENCY_MODE", "", "BOOL")

    if (driverInitType == "DIT_ADDING") then
        -- Initialization needed only when the driver is added
        -- to a project
    elseif (driverInitType == "DIT_STARTUP") then
        -- Initialization needed only during initial startup
    elseif (driverInitType == "DIT_UPDATING") then
        -- Initialization needed only after a driver update
    end
end
```