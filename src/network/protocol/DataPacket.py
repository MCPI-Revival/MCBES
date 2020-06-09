from utils import BinaryStream

class DataPacket(BinaryStream):
    NETWORK_ID = 0
    isEncoded = false
    
    def pid(self):
        return self.NETWORK_ID
        
    def encode(self): pass
    
    def decode(self): pass
