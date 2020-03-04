
## AllowExecute

Beginning with OS release 2.6.0, default runtime editing of encrypted drivers has been deprecated. This has been done to better protect encrypted drivers from unwanted code review or hacking. The AllowExecute API allows for the runtime editing of encrypted drivers through its setting. The API defaults to a setting of False. When set to True, the lua command window will not support entry of any data and the lua output window cannot be used as a display. Use of this API allows driver developers to build into their driver the option to enable remote execution permanently or embed the function call within your own debugging functions to allow or disallow executing of commands in Composer. This API can be invoked during OnDriverInit.


### Signature

`C4:AllowExecute()`


| Parameters | Description |
| --- | --- |
| bool | True / False |
