## GetGeoSettings
`C4:GetGeoSettings()` is a Lua function that enables a Lua driver to retrieve the geo location that was retrieved from webservices. For detailed information regarding geolocation configuration, please see the [Director’s Geolocation Services][1] documentation. 


###### Available in 1.6.0.


### Signature
`C4:GetGeoSettings()`


### Parameters
None


### Returns
The method returns multiple values consisting of string, string:

| Value | Description  |
| ----- | ------------ |
| str   | Country code |
| str   | Country name |


### Usage Notes
A driver can retrieve the geo location as follows:

`countryCode, countryName = C4:GetGeoSettings()`

A driver can retrieve the project location as follows:

`countryCode = C4:GetProjectProperty("countrycode")`

`countryName = C4:GetProjectProperty("countryname")`


If a driver falls back to using the project location, it is imperative (due to regulations) that it retry the call to `C4:GetGeoSettings()` on some regular interval. It is recommended that the driver use the same interval as Director, which is 1 hour (by default). The driver can set a timer to retry the call to `C4:GetGeoSettings()`.

[1]:	https://snap-one.github.io/docs-driverworks-fundamentals-4.0.0-beta/#api-specific-information-director-s-geolocation-service