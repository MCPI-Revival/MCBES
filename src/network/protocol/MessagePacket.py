from network.protocol import DataPacket
from network.protocol import ProtocolInfo

class MessagePacket(DataPacket):
    NETWORK_ID = ProtocolInfo.MESSAGE_PACKET
    
    message = None
    
    def decode(self): pass
    
    def encode(self):
        self.putString(self.message)
