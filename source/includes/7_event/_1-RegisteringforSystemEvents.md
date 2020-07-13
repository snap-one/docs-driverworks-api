## Registering for System Events

The management of registering for notifications which occur when system events are fired is made possible through several APIs and callback functions. The following is an example of how to be notified when the “Refresh Navigator” call is made. When bindings, device names, or device media has changed, a “Refresh Navigator” call is is fired. This event is an alert for the Navigators that any cached data about the project or media may now be invalid.

Specifically the event for “Refresh Navigator” is the “OnPIP” event.  To get this event,  we make use of the following generic event registration calls:

[RegisterSystemEvent][1]

`C4:RegisterSystemEvent(eventId, deviceId)`

Creates a registration for a notification when a system event fires.

| Parameter | Description |
| --- | --- |
| eventID (num) | ID value of the event. See list below. |
| deviceID (num) | ID value of the device. |

### Example
`C4:RegisterSystemEvent(C4SystemEvents["OnPIP"], 0)`


The C4SystemEvents variable is the array of all event name to ID’s. Use deviceId 0 to register for device specific events for all devices. Some events are system wide and will be sent regardless of the device id that was registered, others use the device id to filter who gets what events.

Additionally, your driver will need to implement the [OnSystemEvent ][2]method. See the example to the right:


**Useful System Event ID Values**

00 through 05: Internal System Events

06 ((DE\_PIP, OnPIP))

07 through 16:  Internal System Events

17 ((DE\_NETWORK\_BINDING\_ADDED, OnNetworkBindingAdded))

18 ((DE\_NETWORK\_BINDING\_REMOVED, OnNetworkBindingRemoved)

19 ((DE\_NETWORK\_BINDING\_REGISTERED, OnNetworkBindingRegistered))

20 ((DE\_NETWORK\_BINDING\_UNREGISTERED, OnNetworkBindingUnregistered))

21 through 47: Internal System Events

48 ((DE\_DEVICE\_ONLINE, OnDeviceOnline))

49 ((DE\_DEVICE\_OFFLINE, OnDeviceOffline))

50 and 51: Internal System Events

52 ((DE\_ZIPCODE\_CHANGED, OnZipcodeChanged))

53 ((DE\_LATITUDE\_CHANGED, OnLatitudeChanged))

54 ((DE\_LONGITUDE\_CHANGED, OnLongitudeChanged)

55 through 57: Internal System Events

58 ((DE\_LOCALE\_CHANGED, OnLocaleChanged))

59 through 86: Internal System Event

90 ((DE\_DIRECTOR\_IP\_ADDRESS\_CHANGED, OnDirectorIPAddressChanged))

Note that the OnProjectChanged event was deprecated in 2.10.X due to the architectural change of using a database for persistence.  There are specific events available for things such as device add, remove, and rename. These are:

* OnItemAdded
* OnItemRemoved
* OnItemNameChanged

[1]:	https://control4.github.io/docs-driverworks-api/#registersystemevent
[2]:	https://control4.github.io/docs-driverworks-api/#onsystemevent