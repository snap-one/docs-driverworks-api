## Sample SSL (Multi-Port) Connection

To the right is a sample of a Driver's Connection XML. It shows the XML entries required for a static SSL type connection using two ports (443 and 444):


```xml
<connection>
    <id>6001</id>
    <facing>6</facing>
    <connectionname>Hopper Control Connection</connectionname>
    <type>4</type>
    <consumer>True</consumer>
    <classes>
        <class>
            <classname>SSL</classname>
            <ports>
                <port>
                    <number>443</number>
                    <auto_connect>False</auto_connect>
                    <monitor_connection>False</monitor_connection>
                    <keep_connection>False</keep_connection>
                    <delimiter>0d</delimiter>
                    <certificate>./DISH.cert</certificate>
                    <private_key protected = "True">./DISH.cert</private_key>
                    <cacert>./DISH.cert</cacert>
                </port>
                <port>
                    <number>444</number>
                    <auto_connect>False</auto_connect>
                    <monitor_connection>False</monitor_connection>
                    <keep_connection>False</keep_connection>
                    <delimiter>0d</delimiter>
                    <certificate>./DISH.cert</certificate>
                    <private_key protected = "True">./DISH.cert</private_key>
                    <cacert>./DISH.cert</cacert>
                </port>
            </ports>
        </class>
    </classes>
</connection>
```

This connection using the first port is created using the [CreateNetworkConnection][1] API: 

`C4:CreateNetworkConnection (6001, '192.168.1.100', "SSL")`

This connection's port parameters are sent using the [NetPortOptions][2] API:

`C4:NetPortOptions(6001, 443, "SSL", tPortParams)`

Finally, the connection is actually made using the [NetConnect][3] API. The use of the NectConnect API is required for the new connection to be made:

 `C4:NetConnect(6001, 443)`

This connection using the second port is created using the [CreateNetworkConnection][4] API:

`tPortParams["AUTO_CONNECT"] = false`

This connection's port parameters are sent using the [NetPortOptions][5] API:

`C4:NetPortOptions(6001, 444, "SSL", tPortParams)`

Finally, the connection is made using the NetConnect API The use of the [NectConnect][6] API is required for the new connection to be made:

 `C4:NetConnect(6001, 444)`

[1]:	https://control4.github.io/docs-driverworks-api/#createnetworkconnection
[2]:	https://control4.github.io/docs-driverworks-api/#netportoptions
[3]:	https://control4.github.io/docs-driverworks-api/#netconnect
[4]:	https://control4.github.io/docs-driverworks-api/#createnetworkconnection
[5]:	https://control4.github.io/docs-driverworks-api/#netportoptions
[6]:	https://control4.github.io/docs-driverworks-api/#netconnect