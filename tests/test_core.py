from uuid import UUID
from datetime import datetime, timezone

from lightningstorm.core.cloud import Cloud
from lightningstorm.core.cloud import Node
from lightningstorm.core.raindrop import MemoryRaindrop


def test_p2p():
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
        uuid=UUID("e96e58c7-0df4-4bb0-9b28-c90e5de940bb"),
        payload=b"any binary payload\xF0\xFE",
        created_date=datetime(2020, 1, 1, tzinfo=timezone.utc),
    )
    # load raindrop
    peer1_node1.load_raindrop(raindrop_1to2)
    # share raindrop with peer2
    peer1_node1.share_raindrop(
        raindrop_uuid=raindrop_1to2.uuid, peers_cloud_uuid=[peer2_cloud2.uuid]
    )
    # list raindrops from peer1 to peer2
    assert [raindrop_1to2.get_headers()] == peer1_node1.list_raindrops_to_peer(
        peer2_cloud2.uuid
    )
    # serialize Raindrop to MIME
    assert (
        b"MIME-Version: 1.0\r\nUUID: e96e58c7-0df4-4bb0-9b28-c90e5de940bb\r\nCreated-Date: 2020-01-01T00:00:00+00:00\r\nContent-Type: application/octet-stream\r\nContent-Lenght: 20\r\n\r\nany binary payload\xF0\xFE"
        == raindrop_1to2.to_mime()
    )
