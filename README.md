# LightningStorm Python

Official python implementation of the [LightningStorm](https://github.com/lightningstorm-project/lightningstorm) peer-to-peer meta-protocol.

## Internal Python API

```python
from uuid import UUID

from lightningstorm.core.cloud import Cloud
from lightningstorm.core.cloud import Node
from lightningstorm.core.raindrop import MemoryRaindrop


# peer1
peer1_node1 = Node(uuid=UUID("889e2473-9552-4643-80c8-502335fc5b62"))
peer1_cloud1 = Cloud(
    uuid=UUID("646f6476-9b81-4e47-9e3d-daeb5e8a8599"), nodes=[peer1_node1]
)

# peer2
peer2_node1 = Node(uuid=UUID("41497db1-e0e8-470c-9ffe-c18ff49e1bcf"))
peer2_cloud2 = Cloud(
    uuid=UUID("c6a2455d-0e36-4fcf-8945-2351ec3415d4"), nodes=[peer2_node1]
)

# raindrop from peer1 to peer2
raindrop_1to2 = MemoryRaindrop(
    uuid=UUID("e96e58c7-0df4-4bb0-9b28-c90e5de940bb"), payload=b"any binary payload\xF0\xFE"
)

# load raindrop
peer1_node1.load_raindrop(raindrop_1to2)

# share raindrop with peer2
peer1_node1.share_raindrop(
    raindrop_uuid=raindrop_1to2.uuid, peers_cloud_uuid=[peer2_cloud2.uuid]
)

# list raindrops from peer1 to peer2
peer1_node1.list_raindrops_to_peer(peer2_cloud2.uuid)
```

### Raindrop Headers

```python
>>> raindrop_1to2.get_headers()
{
    'UUID': 'e96e58c7-0df4-4bb0-9b28-c90e5de940bb',
    'Created-Date': '2020-03-22T02:57:42.965815+00:00',
    'Content-Type': 'application/octet-stream',
    'Content-Lenght': '20'
}
```

### Raindrop payload

```python
>>> raindrop_1to2.payload
b'any binary payload\xf0\xfe'
```

### Raindrop serialization

#### MIME - Multipurpose Internet Mail Extensions / "HTTP-like" message format

```python
raindrop_1to2.to_mime()
```
```HTTP
UUID: e96e58c7-0df4-4bb0-9b28-c90e5de940bb
Created-Date: 2020-03-22T03:27:33.798618+00:00
Content-Type: application/octet-stream
Content-Lenght: 20

any binary payload��
```
