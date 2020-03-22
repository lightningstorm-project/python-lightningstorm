from typing import Dict, List
from uuid import UUID
from collections import defaultdict

from ..raindrop import AbstractRaindrop


class Node:
    def __init__(self, uuid: UUID, raindrops: Dict[UUID, AbstractRaindrop] = None):
        self.uuid = uuid
        self._cloud = None
        self._raindrops_to_other_peer_clouds: Dict[UUID, UUID] = defaultdict(  # type: ignore
            list  # type: ignore
        )
        if raindrops:
            self.raindrops = raindrops
        else:
            self.raindrops = {}

    def _register_cloud(self, cloud):
        self._cloud = cloud

    def load_raindrop(self, raindrop: AbstractRaindrop):
        self.raindrops[raindrop.uuid] = raindrop

    def share_raindrop(self, raindrop_uuid: UUID, peers_cloud_uuid: List[UUID]):
        for peer_cloud_uuid in peers_cloud_uuid:
            self._raindrops_to_other_peer_clouds[peer_cloud_uuid].append(raindrop_uuid)  # type: ignore

    def list_raindrops_to_peer(self, peer_cloud_uuid: UUID) -> List[Dict[str, str]]:
        return [
            r.get_headers()
            for r in [
                self.raindrops[raindrop_uuid]
                for raindrop_uuid in self._raindrops_to_other_peer_clouds[peer_cloud_uuid]  # type: ignore
            ]
        ]
