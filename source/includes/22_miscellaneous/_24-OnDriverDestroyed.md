## OnDriverDestroyed

Called when a driver is deleted from a project, updated within a project or Director is shut down. All of the driver's timers will be killed within the OnDriverDestroyed function. For further information, please see the [Driver Initialization and Destruction][1] best practices documentation.


###### Available from 1.6.0


### Signature

`OnDriverDestroyed(strDIT) `


| Parameter | Description                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------ |
| str       | This optional parameter indicates the scenario in which the driver is initializing. Scenarios include: |
|           | `DIT_UPDATING`: Called as a result of the driver being updated.                                        |
|           | `DIT_LOADED`: Called manually after the driver has already been loaded.                                |

The DIT parameters are available in O.S. 3.2.0 and later.


### Example

```lua
-- Release things this driver had allocated...

function OnDriverDestroyed()
    if (driverInitType == "DIT_UPDATING") then
        -- Invoked prior to a driver being updated
    elseif (driverInitType == "DIT_ LOADED") then
        -- Invoked prior to the driver being unloaded or
        -- removed from a project.
    end
end
```

[1]:	https://snap-one.github.io/docs-driverworks-fundamentals-4.0.0-beta/#api-specific-information-driver-initialization-and-destruction