from network.protocol import DataPacket
from network.protocol import ProtocolInfo

class LoginPacket(DataPacket):
    NETWORK_ID = ProtocolInfo.LOGIN_PACKET
    
    username = None
    protocol1 = None
    protocol2 = None
    
    def decode(self): 
        self.username = self.getString()
        self.protocol1 = self.getInt()
        self.protocol2 = self.getInt()
        if self.protocol1 != ProtocolInfo.PROTOCOL_VERSION:
            self.setBuffer(None, 0)
            return false
        
    def encode(self): pass
