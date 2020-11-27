
## What’s New in 3.2.0

**Driver Initialization and Destruction**

New parameters have been added to [OnDriverInit][1], [OnDriverLateInit][2] and [OnDriver Destroyed][3]. These parameters support instances when driver needs to know under what condition or event caused the Initialization or Destroyed functions to be called. OS Release 3.2.0 introduces a new string parameter to these functions to identify the reason for the call. This parameter, driverInitType (DIT) provides this information.

**Driver Add Driver**

Two new APIs have been delivered with O.S. 3.2.0 to facilitate the ability of driver to add another driver to a project as well as the ability to add a location within the project. See the [AddDevice][4] and [AddLocation][5] APIs for more information.

[1]:	https://control4.github.io/docs-driverworks-api/#ondriverinit
[2]:	https://control4.github.io/docs-driverworks-api/#ondriverlateinit
[3]:	https://control4.github.io/docs-driverworks-api/#ondriverdestroyed
[4]:	https://control4.github.io/docs-driverworks-api/#adddevice
[5]:	https://control4.github.io/docs-driverworks-api/#addlocation