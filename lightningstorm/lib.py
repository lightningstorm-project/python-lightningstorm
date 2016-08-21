
class Storage:
    'Abstract Base Class for node storage'
    
    def store_raindrop(self, metadata, payload):
        'returns raindrop UUID'
        raise NotImplementedError
    
    def retrieve_raindrop(self, uuid):
        'returns a tuple containing metadata and file-like object represent the payload'
        raise NotImplementedError
    
    def search_raindrops(self, query):
        'searches for raindrops'
        raise NotImplementedError
    
    def list_raindrops(self, offset=0, limit=10):
        "returns a list of raindrop's UUIDs"
        raise NotImplementedError

class DevelopmentStorage(Storage):
    def __init__(self):
        pass
