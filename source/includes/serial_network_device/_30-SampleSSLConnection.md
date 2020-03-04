## Sample SSL (Multi-Port) Connection

To the right is a sample of a Driver's Connection XML. It shows the XML entries required for a static SSL type connection using two ports (443 and 444):


```
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

This connection using the first port is created using the CreateNetworkConnection API: 

`C4:CreateNetworkConnection (6001, '192.168.1.100', "SSL")`

This connection's port parameters are sent using the NetPortOptions API:

`C4:NetPortOptions(6001, 443, "SSL", tPortParams)`

Finally, the connection is actually made using the NetConnect API. The use of the NectConnect API is required for the new connection to be made:

 `C4:NetConnect(6001, 443)`

This connection using the second port is created using the CreateNetworkConnection API:

`tPortParams["AUTO_CONNECT"] = false`

This connection's port parameters are sent using the NetPortOptions API:

`C4:NetPortOptions(6001, 444, "SSL", tPortParams)`

Finally, the connection is made using the NetConnect API The use of the NectConnect API is required for the new connection to be made:

 `C4:NetConnect(6001, 444)`