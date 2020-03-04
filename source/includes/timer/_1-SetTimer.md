## SetTimer

Creates and starts timer. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:SetTimer(nDelay, fCallback, bRepeat) `	


| Parameter | Description |
| --- | --- |
| num | Numeric value in milliseconds which is the desired timer delay. This value must be greater than 0. |
| func | The function to be called when the timer fires.  The function signature for non-repeating timers is: function(timer) |
| bool | Optional parameter that, if provided and set to true, the timer will fire repeatedly until canceled. |

The function signature for repeating timers is: function(oTimer, nSkips). timer is the same C4LuaTimer object that is returned from this function. skips (repeating timers only) indicates how many times director skipped calling the function. This can happen if the timer is set up to fire rapidly, but director was too busy to serve the timer in a timely manner. For instance, if the timer was set up for 250ms and director was busy for 600ms before serving the timer, skips would be set to 2, indicating that it missed serving the timer twice since the last time it was served or since it was first started.
bRepeat - boolean - Optional parameter that, if provided and set to true, the timer will fire repeatedly until canceled.



### Returns

C4LuaTimer object with the following method(s):

`oTimer.Cancel()` - This function cancels the timer.


### Usage Note

These timers do not trigger a call into the global OnTimerExpired function. To avoid potentially overwhelming Director with fast repeating timers, the C4:SetTimer() API will skip serving timers if it gets behind. If the timer handler cares, it will receive a second argument “skips” with the number of callbacks that director was not able to serve in a timely manner. This means that it is not guaranteed that if you set up a timer to fire 10 times a second, that your callback will actually get called back 10 times per second. It may get called fewer times than that if Director cannot keep up. If your driver needs to know, it can look at that new skips argument. This allows for much better scalability if some driver were to (accidentally) set a repeating timer with a very small value (e.g. 1ms, 10ms, 100ms). Prior to this change it was possible to permanently “lock up” director in such a case, which also could look like a memory leak as timers would get scheduled as a faster pace than were able to be served.


### Examples

Creating a Repeating Timer:

```
Repeating timer example (once a second):
     local cnt = 0
     local rt = C4:SetTimer(1000, function(timer, skips)
         -- timer is the same as what C4:SetTimer() returned
         print("Timer fired, skips: " .. skips)
         cnt = cnt + 1 + skips
         if (cnt > 9) then
             print("Canceling the timer now")
             timer:Cancel()
         end
     end, true)
     -- If you wish to cancel the timer at any time (even before it fired):
     --rt:Cancel()
```

Creating a Simple Timer:

```
-- Simple timer (once a second)
     local t = C4:SetTimer(1000, function(timer)
         -- timer is the same as what C4:SetTimer() returned
         print("Timer fired")
     end)
     -- If you wish to cancel the timer before it fired:
     --t:Cancel()
```

This function replaces the need to write awkward constructs involving the OnTimerExpired entry point and tracking timer handles such as:

```
g_cnt = 0
g_timer = C4:AddTimer(1, "SECONDS", true)

function OnTimerExpired(idTimer)
       if (idTimer == g_timer) then
              print("Timer fired")
              g_cnt = g_cnt + 1
       if (g_cnt > 9) then
              g_timer = C4:KillTimer(g_timer)
       end
end
```
