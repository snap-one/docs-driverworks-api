## Sample TCP Connection

To the right is a sample of a Driver's Connection XML. It shows the XML entries required for a static TCP type connection:


```xml
<connection>
    <id>6001</id>
    <connectionname>TCP</connectionname>
    <type>4</type>
    <hidden>True</hidden>
    <consumer>True</consumer>
    <classes>
        <class>
            <classname>TCP</classname>
            <ports>
                <port>
                    <number>6700</number>
                    <suppress_connection_events>True</suppress_connection_events>
                    <auto_connect>True</auto_connect>
                    <monitor_connection>True</monitor_connection>
                    <keep_connection>True</keep_connection>
                    <keep_alive>True</keep_alive>
                    <delimiter>0d0a</delimiter>
                </port>
            </ports>
        </class>
    </classes>
</connection>
```

In the example above we see the following XML elements:

- \<id\> - This is the connection's unique ID value.
- \<connectionname\> - Reflects the type of connection the XML supports.
- \<type\> - The type value of 4 is used for all network connections.
- \<hidden\> - The hidden value indicates if the connection will be displayed in ComposerPro. In this example, the connection will be visible in ComposerPro.
- \<consumer\> - The consumer value of true is used for all network connections.

In the example above, this is followed by the class section of the XML which contains the classname element. Note that the class name element is the same as the connectionname value.

This is followed by all of the port specific information for the connection. This is all that is required to configure a static, TCP connection for your driver.

If a dynamic connection is desired, the port information needs to reside within a table (tPortParams) inside the driver. The following is a sample of a the same connection as above, however it is created dynamically:

```lua
local tPortParams = {
   SUPPRESS_CONNECTION_EVENTS = true,
   AUTO_CONNECT = true,
   MONITOR_CONNECTION = true,
   KEEP_CONNECTION = true,
   KEEP_ALIVE = true,
   DELIMITER = "0d0a"
}
C4:CreateNetworkConnection (6001, '192.168.1.100', "TCP")
C4:NetPortOptions(6001, 6700, "TCP", tPortParams)
C4:NetConnect(6001, 6700)
```


This connection is created using the CreateNetworkConnection API:

`C4:CreateNetworkConnection (6001, '192.168.1.100', "TCP")`

This connection's port parameters are sent using the NetPortOptions API:

`C4:NetPortOptions(6001, 6700, "TCP", tPortParams)`

Finally, the connection is made using the [NetConnect][1] API The use of the NetConnect API is required for the new connection to be made.

[1]:	https://snap-one.github.io/docs-driverworks-api/#serial-and-network-interface-netconnect