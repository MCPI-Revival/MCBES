from network.protocol import DataPacket
from network.protocol import ProtocolInfo

class SetTimePacket(DataPacket):
    NETWORK_ID = ProtocolInfo.SET_TIME_PACKET
    
    time = None
    
    def decode(self): pass
    
    def encode(self):
        self.putLong(self.time)
