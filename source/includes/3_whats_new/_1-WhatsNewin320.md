
## What’s New in 3.2.0

**Driver Initialization and Destruction**
New parameters have been added to OnDriverInit, OnDriverLateInit and OnDriver Destroyed. These parameters support instances when driver needs to know under what condition or event caused the Initialization or Destroyed functions to be called. OS Release 3.2.0 introduces a new string parameter to these functions to identify the reason for the call. This parameter, driverInitType (DIT) provides this information.

**Driver Add Driver**
Two new APIs have been delivered with O.S. 3.2.0 to facilitate the ability of driver to add
