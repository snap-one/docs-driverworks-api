# Geolocation Interface

#### Configuring Wi-Fi with Director’s Geolocation  Services

Director maintains two different values for location. The first is the project location which is set by the dealer. This value is maintained by the project and is stored in the project database. 

The second is the geo location. This value is retrieved from web services. 

Why does Director now need to manage two different values for location? Historically, Director has always stored the project location. The project location value is used for such things as computing sunrise/sunset times and determining the radio power level for ZigBee devices. However, inadequacies arise when trying to use the project location value to determine radio power levels, particularly for WiFi levels. These inadequacies are largely due to new regulations. These regulations require that the location be determined with a high degree of certainty. As such, Director can no longer rely on the project location value because a dealer may inadvertently set the wrong location or purposefully enter inaccurate location information. 


In order to comply with regulations, Control4 has implemented a new service that returns the geo location. This location is retrieved from a webservice and is based on the IP address. This webservice returns the country code and name, and does so with a high degree of certainty.


#### Director Geo Location Service
After Director has loaded the project and finished initializing drivers, it schedules an initial call to the geo location webservice. It does this by setting a timer. The interval for this timer is maintained by the following Director configuration setting: `geo-initial-interval-seconds`


This configuration setting specifies the number of seconds that Director should wait before making the initial call to the geo location webservice. The default value is 5 seconds.


When the timer fires Director invokes the geo location webservice. The endpoint for this webservice is retrieved from the registry using the following key: `geolocation.service_url`


The default URL for the geo location webservice (stored in the registry) is as follows:

 `https://apiz.control4.com/cs/geolocation/v1/location`


On success, Director retrieves the country code and name from the response and stores them. Regardless of success or failure, Director then schedules another call to the geo location webservice. It does this by setting a timer. The interval for this timer is maintained by the following Director configuration setting: `geo-interval-minutes`


This configuration setting specifies the number of minutes until the next call to the geo location webservice. The default value is 60 minutes resulting in Director invoking the geo location webservice every hour, by default.

