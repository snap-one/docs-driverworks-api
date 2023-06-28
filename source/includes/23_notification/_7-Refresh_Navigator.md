
## Refresh Navigator Example

The following is an example of how to be notified when the “Refresh Navigator” call is made. When bindings, device names, or device media has changed, a “Refresh Navigator” call is made. This event is an alert for the Navigators that any cached data about the project or media may now be invalid.

Specifically the event for “Refresh Navigator” is the “OnPIP” event.  To get this event,  we make use of the generic event registration calls:

[RegisterSystemEvent][1]
[UnregisterSystemEvent][2]
[UnregisterAllSystemEvents][3]


### Example

`C4:RegisterSystemEvent(C4SystemEvents["OnPIP"], 0)`

The C4SystemEvents variable is the array of all event name to ID’s.

Use deviceId 0 to register for device specific events for all devices.  Some events are system wide and will be sent regardless of the device id that was registered, others use the device id to filter who gets what events.

Your driver will need to implement the “OnSystemEvent” method.


### Example

```lua
function OnSystemEvent(data)
  print("System Event occurred - data: " .. data)
end
```

The “data” passed to the callback function is event specific and can be provided on an event by event basis as needed.  In most cases, it can be ignored.

See [Registering for System Events][4] for additional information.

[1]:	https://snap-one.github.io/docs-driverworks-api/#event-interface-registersystemevent
[2]:	https://snap-one.github.io/docs-driverworks-api/#event-interface-unregistersystemevent
[3]:	https://snap-one.github.io/docs-driverworks-api/#event-interface-unregisterallsystemevents
[4]:	https://snap-one.github.io/docs-driverworks-api/#event-interface-registering-for-system-events