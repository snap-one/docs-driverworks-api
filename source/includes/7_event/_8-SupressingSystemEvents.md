## Suppressing System Events

The `suppress_connection_events` is an optionally used device driver property that dictates whether or not Director will fire the OnDeviceOnline and OnDeviceOffline system events. While these events are not specifically handled within a driver, they can impact system performance. This is especially true when a large amount of media is present or media availability (regardless of a device’s online status) is a requirement. When these events are fired, the Room Driver clears its media cache. The media cache then must be rebuilt when a device comes back online. Unless the exercise of clearing and rebuilding the cache is needed, setting the`suppress_connection_events` property to “True” is recommended.

There are two ways to implement `suppress_connection_event`. First, a driver developer can add the `suppress_connection_events` tag to the port section in the connections area of their driver. For example, to the right is an entry for an HC-250 that defines Director’s connection to Navigator:

	<port>
	 <name>Navigator</name>
	 <number>5115</number>
	 <auto_connect>True</auto_connect>
	 <monitor_connection>False</monitor_connection>
	 <keep_connection>True</keep_connection>
	 <keep_alive>True</keep_alive>
	 <suppress_connection_events>True</suppress_connection_events>
	 <delimiter>0d0a</delimiter>
	</port>

The second way to use the `suppress_connection_events` option is in Lua drivers. The NetConnect() function has an optional parameter that specifies whether Director should suppress OnDeviceOnline and OnDeviceOffline events for the connection. By default, Director does suppress events for all connections created this way. The events can be enabled by passing “false” for this parameter.

See the following APIs in the Serial Network Device Interface:

[NetConnect][1]

[OnConnectionStatusChanged][2]



[1]:	https://control4.github.io/docs-driverworks-api/#netconnect
[2]:	https://control4.github.io/docs-driverworks-api/#onconnectionstatuschanged