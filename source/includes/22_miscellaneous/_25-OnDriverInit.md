## OnDriverInit

Function invoked when a driver is loaded or being updated. This API is provided for the driver developer to initialize all of the driver objects that require initialization.  For further information, please see the [Driver Initialization and Destruction][1] best practices documentation.


###### Available from 2.0.0


### Signature

`OnDriverInit(strDIT) `


| Parameter | Description                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------ |
| str       | This optional parameter indicates the scenario in which the driver is initializing. Scenarios include: |
|           | `DIT_ADDING`: Called as a result of the driver being added to a project.                               |
|           | `DIT_STARTUP`: Called as a result of Director starting or a new project being loaded.                  |
|           | `DIT_UPDATING`: Called as a result of the driver being updated.                                        |

The DIT parameters are available in O.S. 3.2.0 and later.


### Example

```lua
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

[1]:	https://snap-one.github.io/docs-driverworks-fundamentals/#api-specific-information-driver-initialization-and-destruction