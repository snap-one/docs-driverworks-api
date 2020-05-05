## SendZigbeePacket
This function sends a raw Zigbee packet to a Zigbee Binding. This functionality supports both the current Control 4 (EmberNet) as well as ZigBee Pro 1.1 transports. This API should not be invoked during OnDriverInit.

###### Available from 1.6.0.


### Signature

`C4:SendZigbeePacket (strPacket,nProfileID, nClusterID, nGroupID, nSourceEndpoint, ndestinationEndpoint)`


| Parameter | Description |
| --- | --- |
| str | ZigBee supported command packet containing user data. |
| num | Profile ID associated with the data packet |
| num |Source Cluster library ID included within the Profile |
| num | Zigbee device group ID |	
| num | Endpoint designated as the source of the data packet delivery.|
| num |  Endpoint designated as the recipient of the data packet delivery. |


### Returns

`None`


### Usage Note

The following parameters are ignored when using the Control 4 (Embernet) Zigbee stack: 
- nProfileID
- nClusterID
- nGroupID
- nSouceEndpoint
- nDestinationEndpoint. 

Packet data is still sent in the strPacket parameter. If using ZigBee Pro, all data (including strPacket) must conform to ZigBee Pro format. 


### Example

```
g_SequenceNumber=g_sequenceNumber + 1
strPacket = "0" .. Chartype .. string.format(%04x",g_SequenceNumber) .. 	c4.dm.lv 100"
```