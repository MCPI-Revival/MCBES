from network.protocol import DataPacket
from network.protocol import ProtocolInfo

class LoginStatusPacket(DataPacket):
    NETWORK_ID = ProtocolInfo.LOGIN_STATUS_PACKET
    
    status = None
    
    def decode(self): pass
    
    def encode(self):
        self.putInt(self.status)
