from network.protocol import DataPacket
from network.protocol import ProtocolInfo

class StartGamePacket(DataPacket):
    NETWORK_ID = ProtocolInfo.START_GAME_PACKET
    
    seed = None
    unknown1 = None
    gamemode = None
    eid = None
    x = None
    y = None
    z = None
    
    def decode(self): pass
    
    def encode(self):
        self.putLong(self.seed)
        self.putInt(self.unknown1)
        self.putInt(self.gamemode)
        self.putInt(self.eid)
        self.putFloat(self.x)
        self.putFloat(self.y)
        self.putFloat(self.z)
