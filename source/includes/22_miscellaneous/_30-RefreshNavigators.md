## RefreshNavigators

Tells every Navigator in the project to refresh itself, so that they pick up changes to the project such as added, removed or renamed devices. This API should not be invoked during OnDriverInit.


###### Available from 5.0.0


### Signature

`C4:RefreshNavigators()`


### Parameters

`None`


### Returns

`None`


### Usage Note

Refreshing is expensive: every Navigator in the project (touch screens, mobile apps, remotes) reloads the project, and the system slows down while they do. Call `C4:RefreshNavigators()` only after your driver has changed something Navigators show, and only once for a batch of changes. Never call it on a timer, in a loop, or on every status update.

Calls are counted per driver. Drivers that refresh Navigators too often may be disabled, and their developers may be contacted.

Use this API instead of sending the `PIP` command to Director over the loopback port. That port is being closed to drivers.


### Example

```lua
-- After the driver has finished changing the project, refresh Navigators once
function OnProjectChangesDone()
    C4:RefreshNavigators()
end
```
