## OnDriverLateInit

Invoked by lua gen when a driver is loaded. This API is provided for the driver developer to contain all of the driver objects that will require initialization.

###### Available from 2.0.0


### Signature

`C4:OnDriverInit() `


### Usage Note

The steps to initialize a driver are:

1. Initialize Events
2. Initialize Properties table
3. Call OnDriverInit()
4. Initialize all Global Variables – these should be initialized via OndriverInit (see below)


### Example

```
function OnDriverInit()
         OnDriverUpdate()
         
         -- All other initialization that does not need to be initialized with driver update
         -- Fire On Property Changed to set the initial Headers and other Property global sets, they'll change if Property is changed.

         for k,v in pairs(Properties) do
           OnPropertyChanged(k)
         end

         C4:AddVariable("LIGHT_LEVEL", "0", "INT")
         C4:AddVariable("FIRMWARE_VERSION", "", "STRING")
         C4:AddVariable("EMERGENCY_MODE", "", "BOOL")
```
