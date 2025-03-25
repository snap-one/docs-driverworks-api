## Callback Handlers

The MQTT Lua API calls are all asynchronous. Because of this, a set of callbacks are used to let the driver know when things have happened.  Below is a list of the available callbacks and how they are used.  

To make use of these callbacks, the object member defined in "Event Callbacks" should be called with the name of the callback that should be called when this callback is triggered. The name of the callback function does not have to match the name defined in the "Callback Signature", but the parameters that the call expects must be the same.

For example, if you wanted to connect a function called "myCallbackFunction" to the OnConnect callback, and have it print the parameters when it is called, see the code example to the right.

```lua
-- OnConnect Callback Handler Example

function myCallbackFunction(reasonCode, flags)

     print("Reason code: " .. reasonCode)

     print("Flags: " .. flags)

end


-- Create the MQTT object

mqttObject = C4:MQTT()


-- To set the function above to be called when a connect event happens:

mqttObject:OnConnect(myCallbackFunction)
```


Code similar to that in the example to the right would return in the "myCallbackFunction" being called after the Connect() API is called. The reasonCode that is passed in to the callback function will be an integer that indicates the status of the connection attempt. It can be turned in to a descriptive string by using the mqttObject::ReasonCodeToString(reasonCode) API.




