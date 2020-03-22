from typing import List, Dict
from uuid import UUID

from ..node import Node
from ..raindrop import AbstractRaindrop


class Cloud:
    def __init__(self, uuid: UUID, nodes: List[Node]):
        self.uuid = uuid
        self.nodes = nodes
        # self._raindrops_to_other_peer_clouds: Dict[UUID, AbstractRaindrop] = defaultdict(list)
        # register cloud in nodes
        for node in nodes:
            node._register_cloud(self)

    # def share_raindrop(self, raindrop_uuid: UUID, to_clouds_uuid: List[UUID]):
    #     self._raindrops_to_other_peer_clouds[to_clouds_uuid].append()
