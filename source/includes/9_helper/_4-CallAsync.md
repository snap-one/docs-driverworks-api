## CallAsync

API that makes calling functions asynchronously much easier. This API should not be invoked during
OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:CallAsync()`


| Parameter | Description |
| --- | --- |
| str | Function to be called asynchronously. |



### Example

```
print("Calling CallAsync()...")
 C4:CallAsync(function()
       print("Callback was executed.")
	
print("Called CallAsync().")
```

Example Output:
```
Calling CallAsync()...
Called CallAsync().
Callback was executed.
```