from struct import unpack, pack, calcsize
from re import match
import sys

class Binary:

    def checkLength(string, expect):
        length = len(string)
        assert (length == expect), 'Expected ' + str(expect) + 'bytes, got ' + str(length)

    @staticmethod
    def readTriad(str: bytes) -> int:
        Binary.checkLength(str, 3)
        return unpack('>L', b'\x00' + str)[0]

    @staticmethod
    def writeTriad(value: int) -> bytes:
        return pack('>L', value)[1:]

    @staticmethod
    def readLTriad(str: bytes) -> int:
        Binary.checkLength(str, 3)
        return unpack('<L', b'\x00' + str)[0]

    @staticmethod
    def writeLTriad(value: int) -> bytes:
        return pack('<L', value)[0:-1]
    
    @staticmethod
    def readBool(b: bytes) -> int:
        return unpack('?', b)[0]

    @staticmethod
    def writeBool(b: int) -> bytes:
        return b'\x01' if b else b'\x00'
  
    @staticmethod
    def readByte(c: bytes) -> int:
        Binary.checkLength(c, 1)
        return unpack('>B', c)[0]
    
    @staticmethod
    def readSignedByte(c: bytes) -> int:
        Binary.checkLength(c, 1)
        return unpack('>b', c)[0]

    @staticmethod
    def writeByte(c: int) -> bytes:
        return pack(">B", c)
    
    @staticmethod
    def readShort(str: bytes) -> int:
        Binary.checkLength(str, 2)
        return unpack('>H', str)[0]
    
    @staticmethod
    def readSignedShort(str: bytes) -> int:
        Binary.checkLength(str, 2)
        if calcsize == 8:
            return unpack('>H', str)[0] << 48 >> 48
        else:
            return unpack('>H', str)[0] << 16 >> 16

    @staticmethod
    def writeShort(value: int) -> bytes:
        return pack('>H', value)
    
    @staticmethod
    def readLShort(str: bytes) -> int:
        Binary.checkLength(str, 2)
        return unpack('<H', str)[0]
    
    @staticmethod
    def readSignedLShort(str: bytes) -> int:
        Binary.checkLength(str, 2)
        if calcsize == 8:
            return unpack('<H', str)[0] << 48 >> 48
        else:
            return unpack('<H', str)[0] << 16 >> 16

    @staticmethod
    def writeLShort(value: int) -> bytes:
        return pack('<H', value)
    
    @staticmethod
    def readInt(str: bytes) -> int:
        Binary.checkLength(str, 4)
        return unpack('>L', str)[0]

    @staticmethod
    def writeInt(value: int) -> bytes:
        return pack('>L', value)

    @staticmethod
    def readLInt(str: bytes) -> int:
        Binary.checkLength(str, 4)
        return unpack('<L', str)[0]

    @staticmethod
    def writeLInt(value: int) -> bytes:
        return pack('<L', value)

    @staticmethod
    def readFloat(str: bytes) -> int:
        Binary.checkLength(str, 4)
        return unpack('>f', str)[0]
    
    @staticmethod
    def readRoundedFloat(str, accuracy):
        return round(Binary.readFloat(str), accuracy)

    @staticmethod
    def writeFloat(value: int) -> bytes:
        return pack('>f', value)

    @staticmethod
    def readLFloat(str: bytes) -> int:
        Binary.checkLength(str, 4)
        return unpack('<f', str)[0]
    
    @staticmethod
    def readRoundedLFloat(str, accuracy):
        return round(Binary.readLFloat(str), accuracy)

    @staticmethod
    def writeLFloat(value: int) -> bytes:
        return pack('<f', value)
    
    
    @staticmethod
    def printFloat(value):
        return match(r"/(\\.\\d+?)0+$/", "" + value).group(1)

    @staticmethod
    def readDouble(str: bytes) -> int:
        Binary.checkLength(str, 8)
        return unpack('>d', str)[0]

    @staticmethod
    def writeDouble(value: int) -> bytes:
        return pack('>d', value)

    @staticmethod
    def readLDouble(str: bytes) -> int:
        Binary.checkLength(str, 8)
        return unpack('<d', str)[0]

    @staticmethod
    def writeLDouble(value: int) -> bytes:
        return pack('<d', value)

    @staticmethod
    def readLong(str: bytes) -> int:
        Binary.checkLength(str, 8)
        return unpack('>L', str)[0]

    @staticmethod
    def writeLong(value: int) -> bytes:
        return pack('>L', value)

    @staticmethod
    def readLLong(str: bytes) -> int:
        Binary.checkLength(str, 8)
        return unpack('<L', str)[0]

    @staticmethod
    def writeLLong(value: int) -> bytes:
        return pack('<L', value)
