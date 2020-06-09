from .Binary import Binary

class BinaryStream:
    buffer = ""
    offset = None
    channel = 0
    
    def __int__(self, buffer = "", offset = 0):
        self.buffer = buffer
        self.offset = offset
    
    def reset(self):
        self.buffer = ""
        self.offset = 0
        
    def setChannel(self, channel):
        self.channel = int(channel)
        return self
    
    def getChannel(self):
        return self.channel

    def setBuffer(self, buffer = "", offset = 0):
        self.buffer = buffer
        self.offset = int(offset)
        
    def getOffset(self):
        return self.offset
    
    def getBuffer(self):
        return self.buffer
    
    def get(self, len):
        if len < 0:
            self.offset = len(self.buffer) - 1;
            return ""
        elif len == True:
            str = self.buffer[0:self.offset]
            self.offset = len(self.buffer)
            return str
        buffer = self.buffer[self.offset:self.offset+len]
        self.offset += length
        return buffer
    
    def put(self, str):
        self.buffer += str
        
    def getBool(self):
        return self.get(1) != b'\x00'
    
    def putBool(self, v):
        self.buffer += (b"\x01" if v else b"\x00")
        
    def getByte(self):
        self.offset += 1
        return ord(self.buffer[self.offset])
    
    def putByte(self, v):
        self.buffer += chr(v)
        
    def getLong(self):
        return Binary.readLong(self.get(8))
    
    def putLong(self, v):
        self.buffer += Binary.writeLong(v)
        
    def getLLong(self):
        return Binary.readLLong(self.get(8))
    
    def putLLong(self, v):
        self.buffer += Binary.writeLLong(v)
        
    def getInt(self):
        return Binary.readInt(self.get(4))
    
    def putInt(self, v):
        self.buffer += Binary.writeInt(v)
        
    def getLInt(self):
        return Binary.readLInt(self.get(4))
    
    def putLInt(self, v):
        self.buffer += Binary.writeLInt(v)
    
    def getShort(self):
        return Binary.readShort(self.get(2))
    
    def putShort(self, v):
        self.buffer += Binary.writeShort(v)
        
    def getLShort(self):
        return Binary.readLShort(self.get(2))
    
    def putLShort(self, v):
        self.buffer += Binary.writeLShort(v)
        
    def getSignedShort(self):
        return Binary.readSignedShort(self.get(2))
    
    def getSignedLShort(self):
        return Binary.readSignedLShort(self.get(4))
    
    def getFloat(self):
        return Binary.readFloat(self.get(4))
    
    def putFloat(self, v):
        self.buffer += Binary.writeFloat(v)
        
    def getLFloat(self):
        return Binary.readLFloat(self.get(4))
    
    def putLFloat(self, v):
        self.buffer += Binary.writeLFloat(v)
        
    def getRoundedFloat(self, accuracy):
        return Binary.readRoundedFloat(self.get(4), accuracy)
    
    def getRoundedLFloat(self, accuracy):
        return Binary.readRoundedLFloat(self.get(4), accuracy)
    
    def getTriad(self):
        return Binary.readTriad(self.get(3))
    
    def putTriad(self, v):
        self.buffer += Binary.writeTriad(v)
        
    def getLTriad(self):
        return Binary.readLTriad(self.get(3))
    
    def putLTriad(self, v):
        self.buffer += Binary.writeLTriad(v)  

    def getString(self):
        self.get(self.getShort())
        
    def putString(self, v):
        self.putShort(len(v))
        self.put(v)
        
    def getDataArray(self, length = 10):
        data = []
        i = 1
        while (i <= length) and (not self.feof()):
            i = i + 1
            data = get(self.getTriad())
        return data
    
    def putDataArray(self, array = []):
        for v in array:
            self.putTriad(len(v))
            self.put(v)
      
    def getSlot(self):
        id = self.getShort()
        cnt = self.getByte()
        return Item(id, self.getShort(), cnt)
    
    def getSlot(self, item: Item):
        self.putShort(item.getId())
        self.putByte(item.getCount())
        self.putShort(item.getDamage())
        
    def feof(self):
        try:
            self.buffer[self.offset]
            return True
        except IndexError:
            return False
