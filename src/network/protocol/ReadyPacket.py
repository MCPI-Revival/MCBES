from network.protocol import DataPacket
from network.protocol import ProtocolInfo

class ReadyPacket(DataPacket):
    NETWORK_ID = ProtocolInfo.READY_PACKET
    
    status = None
    
    def decode(self):
        self.status = self.getByte()
        
    def encode(self): pass
