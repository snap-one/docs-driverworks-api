## OnZigbeePacketIn

Receives an unsolicited zigbee packet from the device or a response to a command that was sent.

###### Available from 1.6.0.


### Signature

`OnZigbeePacketIn(strPacket,nProfileID, nClusterID, nGroupID, nSourceEndpoint, ndestinationEndpoint)`


| Parameter | Description |
| --- | --- |
| str | ZigBee supported command packet containing user data. |
| num | Profile ID associated with the data packet |
| num |Source Cluster library ID included within the Profile |
| num | Zigbee device group ID |
| num | Endpoint designated as the source of the data packet delivery. |
| num |  Endpoint designated as the recipient of the data packet delivery. |


### Returns

`None`


### Usage Note

The following parameters are ignored when using the Control 4 (Embernet) Zigbee stack: 

- nProfileID
- nClusterID
- nGroupID
- nSouceEndpoint
- nDestinationEndpoint

Packet data is still sent in the strPacket parameter. If using ZigBee Pro, all data (including strPacket) must conform to ZigBee Pro format. 


### Example

```lua

function OnZigbeePacketIn (strPacket, idProfileID, idClusterID,
  idGroupID, sourceEndpoint,destinationEndpoint)
  print("OnZigbeePacketIn;" .. strPacket)
end
```